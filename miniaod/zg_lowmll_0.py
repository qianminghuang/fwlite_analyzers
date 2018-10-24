import ROOT
import sys
from DataFormats.FWLite import Events, Handle


events = Events (['root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1478_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1479_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1480_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1481_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1482_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1483_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1484_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1485_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1486_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1487_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1488_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1489_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1490_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1491_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1492_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1493_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1494_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1495_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1496_1685818.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/1685818/s3_ZA_lowmass_1497_1685818.root'])

handlePruned  = Handle ("std::vector<reco::GenParticle>")
handlePacked  = Handle ("std::vector<pat::PackedGenParticle>")
labelPruned = ("prunedGenParticles")
labelPacked = ("packedGenParticles")

# loop over events
count= 0

hist_mll=ROOT.TH1F("mll","mll",100,0,100)

n_4_muon_events = 0

count = 0

for event in events:

    if count % 1000 == 0:
        print count

    count += 1

    event.getByLabel (labelPruned, handlePruned)

    pruned = handlePruned.product()

    n_mu_minus = 0
    n_mu_plus = 0

    for p in pruned :

        if p.pdgId() == 13 and p.statusFlags().isPrompt() and p.status() == 1 and abs(p.mother().pdgId()) != 2212:

            if (p.mother() and abs(p.mother().pdgId()) == 2212) or (p.mother() and p.mother().mother() and abs(p.mother().mother().pdgId()) == 2212) or (p.mother() and p.mother().mother() and p.mother().mother().mother() and abs(p.mother().mother().mother().pdgId()) == 2212):
                continue
            n_mu_minus += 1
            mu_minus_p4 = p.p4()
        elif p.pdgId() == -13 and p.statusFlags().isPrompt() and p.status() == 1 and abs(p.mother().pdgId()) != 2212:  

            if (p.mother() and abs(p.mother().pdgId()) == 2212) or (p.mother() and p.mother().mother() and abs(p.mother().mother().pdgId()) == 2212) or (p.mother() and p.mother().mother() and p.mother().mother().mother() and abs(p.mother().mother().mother().pdgId()) == 2212):
                continue

            n_mu_plus += 1
            mu_plus_p4 = p.p4()  

    assert((n_mu_minus == 1 and n_mu_plus == 1) or (n_mu_minus == 0 and n_mu_plus == 0) or (n_mu_minus == 2 and n_mu_plus == 2))        

    if n_mu_minus == 2 and n_mu_plus == 2:
        n_4_muon_events += 1

    if n_mu_minus == 1 and n_mu_plus == 1:
        hist_mll.Fill((mu_plus_p4+mu_minus_p4).M())

c = ROOT.TCanvas()

hist_mll.Draw()

c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")

print "n_4_muon_events = "+str(n_4_muon_events)
