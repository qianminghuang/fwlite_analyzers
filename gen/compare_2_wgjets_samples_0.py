import ROOT
import sys
from DataFormats.FWLite import Events, Handle


from math import hypot, pi

def deltaPhi(phi1,phi2):
    ## Catch if being called with two objects                                                                                                                                             
    if type(phi1) != float and type(phi1) != int:
        phi1 = phi1.phi
    if type(phi2) != float and type(phi2) != int:
        phi2 = phi2.phi
    ## Otherwise                                                                                                                                                                          
    dphi = (phi1-phi2)
    while dphi >  pi: dphi -= 2*pi
    while dphi < -pi: dphi += 2*pi
    return dphi

def deltaR(eta1,phi1,eta2=None,phi2=None):
    ## catch if called with objects                                                                                                                                                       
    if eta2 == None:
        return deltaR(eta1.eta,eta1.phi,phi1.eta,phi1.phi)
    ## otherwise                                                                                                                                                                          
    return hypot(eta1-eta2, deltaPhi(phi1,phi2))

events_wgjets_1 = Events (['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIISummer15wmLHEGS-00183_LO.root'])

events_wgjets_2 = Events (['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIISummer15wmLHEGS-00183_NLO.root'])

xs_wgjets_1 = 196.4
xs_wgjets_2 = 178.6
#xs_wgjets = xs_wjets


lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "externalLHEProducer"
geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"
genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

# loop over events
count= 0
countweighted = 0

th1f_wgjets_1_njets = ROOT.TH1F("wgjets 1 njets","",7,-0.5,6.5)
th1f_wgjets_2_njets = ROOT.TH1F("wgjets 2 njets","",7,-0.5,6.5)

th1f_wgjets_1_photon_pt = ROOT.TH1F("wgjets 1 photon pt","",10,25,125)
th1f_wgjets_2_photon_pt = ROOT.TH1F("wgjets 2 photon pt","",10,25,125)

th1f_wgjets_1_photon_eta = ROOT.TH1F("wgjets 1 photon eta","",10,-2.5,2.5)
th1f_wgjets_2_photon_eta = ROOT.TH1F("wgjets 2 photon eta","",10,-2.5,2.5)

th1f_wgjets_1_lepton_pt = ROOT.TH1F("wgjets 1 lepton pt","",10,25,125)
th1f_wgjets_2_lepton_pt = ROOT.TH1F("wgjets 2 lepton pt","",10,25,125)

th1f_wgjets_1_delta_r = ROOT.TH1F("wgjets 1 delta r","",35,0,3.5)
th1f_wgjets_2_delta_r = ROOT.TH1F("wgjets 2 delta r","",35,0,3.5)

th1f_wgjets_1_njets.Sumw2()
th1f_wgjets_2_njets.Sumw2()

th1f_wgjets_1_photon_pt.Sumw2()
th1f_wgjets_2_photon_pt.Sumw2()

th1f_wgjets_1_photon_eta.Sumw2()
th1f_wgjets_2_photon_eta.Sumw2()

th1f_wgjets_1_lepton_pt.Sumw2()
th1f_wgjets_2_lepton_pt.Sumw2()

th1f_wgjets_1_delta_r.Sumw2()
th1f_wgjets_2_delta_r.Sumw2()

for event in events_wgjets_1:

    if count > 100000:
        break

    if count % 10000 == 0:
        print "count = " + str(count)

    count +=1

    event.getByLabel (genParticlesLabel, genparticles)
    
    event.getByLabel(geninfoLabel,geninfo)
    
    gen = geninfo.product()

    event.getByLabel(lheinfoLabel, lheinfo)

    npartons = 0

    for i in range(0,len(lheinfo.product().hepeup().IDUP)):
        if lheinfo.product().hepeup().ISTUP.at(i) != 1:
            continue

        if (abs(lheinfo.product().hepeup().IDUP.at(i)) == 1 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 2 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 3 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 4 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 5 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 21):
            npartons += 1


    if gen.weight() > 0:
        countweighted += 1
    else:
        countweighted -= 1

    nelectrons = 0

    for p in genparticles.product():

        if abs(p.pdgId()) == 11 and p.pt() > 25 and abs(p.eta()) < 2.5 and p.status() == 1  :
            nelectrons += 1
            electron = p

    if nelectrons != 1:
        continue

    nphotons = 0        

    for p in genparticles.product() :

        if abs(p.pdgId()) == 22 and p.pt() > 25 and abs(p.eta()) < 2.5 and p.status() == 1   :
            nphotons += 1
            photon = p

    if nphotons != 1:
        continue

    if deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()) < 0.5:
        continue

    njets = 0        

    for p in genparticles.product():

#        if (abs(p.pdgId()) == 1 or abs(p.pdgId()) == 2 or abs(p.pdgId()) == 3 or abs(p.pdgId()) == 4 or abs(p.pdgId()) == 5 or abs(p.pdgId()) == 21) and p.pt() > 30 and p.statusFlags().isPrompt() and p.statusFlags().isLastCopy()  :
        if (abs(p.pdgId()) == 1 or abs(p.pdgId()) == 2) and p.pt() > 30:
            njets +=1

    njets = npartons         

    if gen.weight() > 0:
        th1f_wgjets_1_njets.Fill(njets,1)
        th1f_wgjets_1_photon_pt.Fill(photon.pt(),1)
        th1f_wgjets_1_photon_eta.Fill(photon.eta(),1)
        th1f_wgjets_1_lepton_pt.Fill(electron.pt(),1)
        th1f_wgjets_1_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),1)
    else:
        th1f_wgjets_1_njets.Fill(njets,-1)
        th1f_wgjets_1_photon_pt.Fill(photon.pt(),-1)
        th1f_wgjets_1_photon_eta.Fill(photon.eta(),-1)
        th1f_wgjets_1_lepton_pt.Fill(electron.pt(),-1)
        th1f_wgjets_1_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),-1)

    #print njets

c = ROOT.TCanvas()

th1f_wgjets_1_njets.Scale(xs_wgjets_1*1000*36/countweighted)
th1f_wgjets_1_photon_pt.Scale(xs_wgjets_1*1000*36/countweighted)
th1f_wgjets_1_photon_eta.Scale(xs_wgjets_1*1000*36/countweighted)
th1f_wgjets_1_lepton_pt.Scale(xs_wgjets_1*1000*36/countweighted)
th1f_wgjets_1_delta_r.Scale(xs_wgjets_1*1000*36/countweighted)

th1f_wgjets_1_njets.SetLineWidth(3)
th1f_wgjets_1_photon_pt.SetLineWidth(3)
th1f_wgjets_1_photon_eta.SetLineWidth(3)
th1f_wgjets_1_lepton_pt.SetLineWidth(3)
th1f_wgjets_1_delta_r.SetLineWidth(3)

th1f_wgjets_1_njets.SetLineColor(ROOT.kRed)
th1f_wgjets_1_photon_pt.SetLineColor(ROOT.kRed)
th1f_wgjets_1_photon_eta.SetLineColor(ROOT.kRed)
th1f_wgjets_1_lepton_pt.SetLineColor(ROOT.kRed)
th1f_wgjets_1_delta_r.SetLineColor(ROOT.kRed)

count = 0
countweighted = 0

for event in events_wgjets_2:

    if count > 100000:
        break

    if count % 10000 == 0:
        print "count = " + str(count)

    count +=1

    event.getByLabel (genParticlesLabel, genparticles)
    
    event.getByLabel(geninfoLabel,geninfo)
    
    gen = geninfo.product()

    event.getByLabel(lheinfoLabel, lheinfo)

    npartons = 0

    for i in range(0,len(lheinfo.product().hepeup().IDUP)):
        if lheinfo.product().hepeup().ISTUP.at(i) != 1:
            continue

        if (abs(lheinfo.product().hepeup().IDUP.at(i)) == 1 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 2 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 3 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 4 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 5 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 21):
            npartons += 1

    if gen.weight() > 0:
        countweighted += 1
    else:
        countweighted -= 1

    nelectrons = 0

    for p in genparticles.product() :

#        if abs(p.pdgId()) == 11 and p.pt() > 25 and (p.statusFlags().isPrompt() or p.statusFlags().isPromptTauDecayProduct()) and p.status() == 1  :
        if abs(p.pdgId()) == 11 and p.pt() > 25 and abs(p.eta()) < 2.5 and p.status() == 1  :
            nelectrons += 1
            electron = p

#    print "nelectrons = "+str(nelectrons)

    if nelectrons != 1:
        continue

    nphotons = 0        

    for p in genparticles.product() :

#        if abs(p.pdgId()) == 22 and p.pt() > 25 and (p.statusFlags().isPrompt() or p.statusFlags().isPromptTauDecayProduct()) and p.status() == 1   :
        if abs(p.pdgId()) == 22 and p.pt() > 25 and abs(p.eta()) < 2.5 and p.status() == 1   :
            nphotons += 1
            photon = p

#    print "nphotons = "+str(nphotons)

    if nphotons != 1:
        continue

    if deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()) < 0.5:
        continue

    njets = 0        

    for p in genparticles.product() :

#        if (abs(p.pdgId()) == 1 or abs(p.pdgId()) == 2 or abs(p.pdgId()) == 3 or abs(p.pdgId()) == 4 or abs(p.pdgId()) == 5 or abs(p.pdgId()) == 21) and p.pt() > 30 and p.statusFlags().isPrompt() and p.statusFlags().isLastCopy()  :
        if (abs(p.pdgId()) == 1 or abs(p.pdgId()) == 2) and p.pt() > 30 :
            njets +=1

    njets = npartons 

    if gen.weight() > 0:
        th1f_wgjets_2_njets.Fill(njets,1)
        th1f_wgjets_2_photon_pt.Fill(photon.pt(),1)
        th1f_wgjets_2_photon_eta.Fill(photon.eta(),1)
        th1f_wgjets_2_lepton_pt.Fill(electron.pt(),1)
        th1f_wgjets_2_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),1)
    else:
        th1f_wgjets_2_njets.Fill(njets,-1)
        th1f_wgjets_2_photon_pt.Fill(photon.pt(),-1)
        th1f_wgjets_2_photon_eta.Fill(photon.eta(),-1)
        th1f_wgjets_2_lepton_pt.Fill(electron.pt(),-1)
        th1f_wgjets_2_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),-1)
    #print njets

th1f_wgjets_2_njets.Scale(xs_wgjets_2*1000*36/countweighted)
th1f_wgjets_2_photon_pt.Scale(xs_wgjets_2*1000*36/countweighted)
th1f_wgjets_2_photon_eta.Scale(xs_wgjets_2*1000*36/countweighted)
th1f_wgjets_2_lepton_pt.Scale(xs_wgjets_2*1000*36/countweighted)
th1f_wgjets_2_delta_r.Scale(xs_wgjets_2*1000*36/countweighted)

th1f_wgjets_2_njets.SetLineWidth(3)
th1f_wgjets_2_photon_pt.SetLineWidth(3)
th1f_wgjets_2_photon_eta.SetLineWidth(3)
th1f_wgjets_2_lepton_pt.SetLineWidth(3)
th1f_wgjets_2_delta_r.SetLineWidth(3)

th1f_wgjets_2_njets.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_photon_pt.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_photon_eta.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_lepton_pt.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_delta_r.SetLineColor(ROOT.kBlue)

if th1f_wgjets_1_photon_eta.GetMaximum() > th1f_wgjets_2_photon_eta.GetMaximum():

    th1f_wgjets_1_photon_eta.SetMinimum(0)
    th1f_wgjets_1_photon_eta.SetMaximum(1.5*th1f_wgjets_1_photon_eta.GetMaximum())

    th1f_wgjets_1_photon_eta.Draw()
    th1f_wgjets_1_photon_eta.GetXaxis().SetTitle("photon #eta")
    th1f_wgjets_1_photon_eta.SetStats(0)
    th1f_wgjets_2_photon_eta.Draw("same")
else:

    th1f_wgjets_2_photon_eta.SetMinimum(0)
    th1f_wgjets_2_photon_eta.SetMaximum(1.5*th1f_wgjets_2_photon_eta.GetMaximum())

    th1f_wgjets_2_photon_eta.Draw()
    th1f_wgjets_2_photon_eta.GetXaxis().SetTitle("photon #eta")
    th1f_wgjets_2_photon_eta.SetStats(0)
    th1f_wgjets_1_photon_eta.Draw("same")

leg=ROOT.TLegend(.58,.73,.88,.88)

leg.AddEntry(th1f_wgjets_1_photon_eta,"wg+jets LO","l")
leg.AddEntry(th1f_wgjets_2_photon_eta,"wg+jets NLO","l")

leg.Draw("same")

c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")
