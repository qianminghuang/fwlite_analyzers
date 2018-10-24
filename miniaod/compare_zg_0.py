import ROOT
import sys
from DataFormats.FWLite import Events, Handle


events_zglowmll = Events (['root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_0_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_1_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_2_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_3_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_4_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_5_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_6_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_7_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_8_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_9_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_10_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_11_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_12_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_13_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_14_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_15_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_16_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_17_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_18_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_19_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_20_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_21_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_22_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_23_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_24_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_25_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_26_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_27_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_28_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_29_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_30_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_31_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_32_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_33_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_34_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_35_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_36_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_37_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_38_196633.root','root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/ycyang/MCProd/ZA_lowmass/step3/196633/s3_ZA_lowmass_39_196633.root'])

events_zg = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/00366B16-2804-E811-82A4-C4346BBC9BB0.root'])

handlePruned  = Handle ("std::vector<reco::GenParticle>")
handlePacked  = Handle ("std::vector<pat::PackedGenParticle>")
labelPruned = ("prunedGenParticles")
labelPacked = ("packedGenParticles")
geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"

count_zglowmll= 0
count_zg= 0

count_zglowmll_weighted= 0
count_zg_weighted= 0

hist_zglowmll_mll=ROOT.TH1F("zglowmll mll","zglowmll mll",100,0,100)
hist_zg_mll=ROOT.TH1F("zg mll","zg mll",100,0,100)

xs_zglowmll = 96.75 
xs_zg = 48.43

n_4_muon_events = 0

for event in events_zglowmll:

    if count_zglowmll % 1000 == 0:
        print count_zglowmll

    count_zglowmll += 1

    event.getByLabel (labelPruned, handlePruned)

    pruned = handlePruned.product()

    event.getByLabel(geninfoLabel,geninfo)

    gen = geninfo.product()

    if gen.weight() > 0:
        count_zglowmll_weighted += 1
    else:    
        count_zglowmll_weighted -= 1

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

    assert((n_mu_minus == 1 and n_mu_plus == 1) or (n_mu_minus == 0 and n_mu_plus == 0) or (n_mu_minus == 2 and n_mu_plus == 2) or (n_mu_minus == 3 and n_mu_plus == 3))        

    if (n_mu_minus == 2 and n_mu_plus == 2) or (n_mu_minus == 3 and n_mu_plus == 3):
        n_4_muon_events += 1

    if n_mu_minus == 1 and n_mu_plus == 1:
        if gen.weight() > 0:
            hist_zglowmll_mll.Fill((mu_plus_p4+mu_minus_p4).M())
        else:
            hist_zglowmll_mll.Fill((mu_plus_p4+mu_minus_p4).M(),-1)

for event in events_zg:

    if count_zg % 1000 == 0:
        print count_zg

    count_zg += 1

    event.getByLabel(geninfoLabel,geninfo)

    gen = geninfo.product()

    if gen.weight() > 0:
        count_zg_weighted += 1
    else:    
        count_zg_weighted -= 1

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

    assert((n_mu_minus == 1 and n_mu_plus == 1) or (n_mu_minus == 0 and n_mu_plus == 0) or (n_mu_minus == 2 and n_mu_plus == 2) or (n_mu_minus == 3 and n_mu_plus == 3))        

    if (n_mu_minus == 2 and n_mu_plus == 2)  or (n_mu_minus == 3 and n_mu_plus == 3):
        n_4_muon_events += 1

    if n_mu_minus == 1 and n_mu_plus == 1:
        if gen.weight() > 0:
            hist_zg_mll.Fill((mu_plus_p4+mu_minus_p4).M())
        else:
            hist_zg_mll.Fill((mu_plus_p4+mu_minus_p4).M(),-1)

c = ROOT.TCanvas()

hist_zglowmll_mll.SetLineColor(3)
hist_zg_mll.SetLineColor(3)

hist_zglowmll_mll.Scale(xs_zglowmll/count_zglowmll_weighted)
hist_zg_mll.Scale(xs_zg/count_zg_weighted)

hist_zg_mll.SetLineColor(ROOT.kBlue)
hist_zglowmll_mll.SetLineColor(ROOT.kRed)

hist_zg_mll.SetMaximum(1.5*max(hist_zg_mll.GetMaximum(),hist_zglowmll_mll.GetMaximum()))

hist_zg_mll.GetXaxis().SetTitle("m_{ll} (GeV)")

hist_zg_mll.SetStats(0)

hist_zg_mll.Draw()
hist_zglowmll_mll.Draw("same")

leg=ROOT.TLegend(.58,.73,.88,.88)

leg.AddEntry(hist_zg_mll,"zg+jets official","l")
leg.AddEntry(hist_zglowmll_mll,"zg+jets low mll","l")

leg.Draw("same")

c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")

print "n_4_muon_events = "+str(n_4_muon_events)
