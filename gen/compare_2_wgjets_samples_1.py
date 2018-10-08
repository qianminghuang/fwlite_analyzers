import ROOT
import sys
from DataFormats.FWLite import Events, Handle
#from PhysicsTools.HepMCCandAlgos import MCTruthHelper


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

lumi = float(1)/float(1000)

events_wgjets_1 = Events (['/eos/user/a/amlevin/tmp/wp3leptonflavors.0.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.10.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.11.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.12.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.13.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.14.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.15.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.16.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.17.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.18.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.19.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.1.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.20.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.21.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.22.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.23.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.24.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.25.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.26.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.27.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.28.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.29.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.2.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.30.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.31.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.32.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.33.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.34.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.35.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.36.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.37.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.38.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.39.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.3.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.40.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.41.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.42.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.43.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.44.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.45.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.46.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.47.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.48.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.49.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.4.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.50.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.51.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.52.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.53.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.54.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.55.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.56.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.57.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.58.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.59.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.5.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.60.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.61.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.62.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.63.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.64.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.65.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.66.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.67.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.68.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.69.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.6.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.70.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.71.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.72.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.73.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.74.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.75.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.76.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.77.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.78.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.79.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.7.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.82.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.8.root','/eos/user/a/amlevin/tmp/wp3leptonflavors.9.root'])

events_wgjets_2 = Events(['/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.38.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.39.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.95.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.59.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.82.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.50.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.29.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.92.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.67.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.45.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.71.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.30.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.22.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.42.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.75.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.15.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.99.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.18.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.32.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.17.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.61.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.91.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.12.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.25.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.36.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.31.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.79.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.93.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.94.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.10.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.28.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.46.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.81.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.37.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.41.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.20.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.24.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.97.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.85.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.83.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.66.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.77.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.33.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.23.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.63.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.11.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.60.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.74.root'])

xs_wgjets_1 = 33540
xs_wgjets_2 = 10908

lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "externalLHEProducer"
geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"
genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

# loop over events
count= 0
countweighted = 0

th1f_wgjets_1_njets = ROOT.TH1F("wgjets 1 njets","",7,-0.5,6.5)
th1f_wgjets_2_njets = ROOT.TH1F("wgjets 2 njets","",7,-0.5,6.5)

th1f_wgjets_1_nphotons = ROOT.TH1F("wgjets 1 nphotons","",7,-0.5,6.5)
th1f_wgjets_2_nphotons = ROOT.TH1F("wgjets 2 nphotons","",7,-0.5,6.5)

th1f_wgjets_1_nleptons = ROOT.TH1F("wgjets 1 nleptons","",7,-0.5,6.5)
th1f_wgjets_2_nleptons = ROOT.TH1F("wgjets 2 nleptons","",7,-0.5,6.5)

th1f_wgjets_1_photon_pt = ROOT.TH1F("wgjets 1 photon pt","",11,15,125)
th1f_wgjets_2_photon_pt = ROOT.TH1F("wgjets 2 photon pt","",11,15,125)

th1f_wgjets_1_photon_eta = ROOT.TH1F("wgjets 1 photon eta","",10,-2.5,2.5)
th1f_wgjets_2_photon_eta = ROOT.TH1F("wgjets 2 photon eta","",10,-2.5,2.5)

th1f_wgjets_1_lepton_pt = ROOT.TH1F("wgjets 1 lepton pt","",12,5,125)
th1f_wgjets_2_lepton_pt = ROOT.TH1F("wgjets 2 lepton pt","",12,5,125)

th1f_wgjets_1_delta_r = ROOT.TH1F("wgjets 1 delta r","",35,0,3.5)
th1f_wgjets_2_delta_r = ROOT.TH1F("wgjets 2 delta r","",35,0,3.5)

th1f_wgjets_1_njets.Sumw2()
th1f_wgjets_2_njets.Sumw2()

th1f_wgjets_1_nphotons.Sumw2()
th1f_wgjets_2_nphotons.Sumw2()

th1f_wgjets_1_nleptons.Sumw2()
th1f_wgjets_2_nleptons.Sumw2()

th1f_wgjets_1_photon_pt.Sumw2()
th1f_wgjets_2_photon_pt.Sumw2()

th1f_wgjets_1_photon_eta.Sumw2()
th1f_wgjets_2_photon_eta.Sumw2()

th1f_wgjets_1_lepton_pt.Sumw2()
th1f_wgjets_2_photon_eta.Sumw2()

th1f_wgjets_1_delta_r.Sumw2()
th1f_wgjets_2_delta_r.Sumw2()

count = 0
countweighted = 0

for event in events_wgjets_1:

    if count > 1000000:
#    if count > -1:
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

    nphotons = 0        

    for p in genparticles.product() :
        
        if p.pdgId() == -11 and p.pt() > 25 and abs(p.eta()) < 2.47 and p.status() == 1  and p.statusFlags().isPrompt():
            nelectrons += 1
            electron = p

        if abs(p.pdgId()) == 22 and p.pt() > 15 and abs(p.eta()) < 2.37 and p.status() == 1  and p.statusFlags().isPrompt():
            nphotons += 1
            photon = p


    if nelectrons != 1:
        continue


    if nphotons != 1:
        continue

    if deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()) < 0.7:
        continue

    njets = npartons 

    if gen.weight() > 0:
        th1f_wgjets_1_njets.Fill(njets,1)
        th1f_wgjets_1_nphotons.Fill(nphotons,1)
        th1f_wgjets_1_nleptons.Fill(nelectrons,1)
        th1f_wgjets_1_photon_pt.Fill(photon.pt(),1)
        th1f_wgjets_1_photon_eta.Fill(photon.eta(),1)
        th1f_wgjets_1_lepton_pt.Fill(electron.pt(),1)
        th1f_wgjets_1_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),1)
    else:
        th1f_wgjets_1_njets.Fill(njets,-1)
        th1f_wgjets_1_nphotons.Fill(nphotons,-1)
        th1f_wgjets_1_nleptons.Fill(nelectrons,-1)
        th1f_wgjets_1_photon_pt.Fill(photon.pt(),-1)
        th1f_wgjets_1_photon_eta.Fill(photon.eta(),-1)
        th1f_wgjets_1_lepton_pt.Fill(electron.pt(),-1)
        th1f_wgjets_1_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),-1)
    #print njets

if countweighted > 0:
    th1f_wgjets_1_njets.Scale(xs_wgjets_1*1000*lumi/countweighted)
    th1f_wgjets_1_nphotons.Scale(xs_wgjets_1*1000*lumi/countweighted)
    th1f_wgjets_1_nleptons.Scale(xs_wgjets_1*1000*lumi/countweighted)
    th1f_wgjets_1_photon_pt.Scale(xs_wgjets_1*1000*lumi/countweighted)
    th1f_wgjets_1_photon_eta.Scale(xs_wgjets_1*1000*lumi/countweighted)
    th1f_wgjets_1_lepton_pt.Scale(xs_wgjets_1*1000*lumi/countweighted)
    th1f_wgjets_1_delta_r.Scale(xs_wgjets_1*1000*lumi/countweighted)

th1f_wgjets_1_njets.SetLineWidth(3)
th1f_wgjets_1_nphotons.SetLineWidth(3)
th1f_wgjets_1_nleptons.SetLineWidth(3)
th1f_wgjets_1_photon_pt.SetLineWidth(3)
th1f_wgjets_1_photon_eta.SetLineWidth(3)
th1f_wgjets_1_lepton_pt.SetLineWidth(3)
th1f_wgjets_1_delta_r.SetLineWidth(3)

th1f_wgjets_1_njets.SetLineColor(ROOT.kBlue)
th1f_wgjets_1_nphotons.SetLineColor(ROOT.kBlue)
th1f_wgjets_1_nleptons.SetLineColor(ROOT.kBlue)
th1f_wgjets_1_photon_pt.SetLineColor(ROOT.kBlue)
th1f_wgjets_1_photon_eta.SetLineColor(ROOT.kBlue)
th1f_wgjets_1_lepton_pt.SetLineColor(ROOT.kBlue)
th1f_wgjets_1_delta_r.SetLineColor(ROOT.kBlue)

count = 0
countweighted = 0

for event in events_wgjets_2:

    if count > 500000:
#    if count > -1:
        break

    if count % 10000 == 0:
#    if count % 1 == 0:
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

    nphotons = 0        

    for p in genparticles.product() :

        if p.pdgId() == -11 and p.pt() > 25 and abs(p.eta()) < 2.47 and p.status() == 1 and p.statusFlags().isPrompt() :
            nelectrons += 1
            electron = p

        if abs(p.pdgId()) == 22 and p.pt() > 15 and abs(p.eta()) < 2.37 and p.status() == 1 and p.statusFlags().isPrompt()  :
            
            nphotons += 1
            photon = p


    if nelectrons != 1:
        continue

    if nphotons != 1:
        continue

    if deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()) < 0.7:
        continue

    njets = npartons 

    if gen.weight() > 0:
        th1f_wgjets_2_njets.Fill(njets,1)
        th1f_wgjets_2_nphotons.Fill(nphotons,1)
        th1f_wgjets_2_nleptons.Fill(nelectrons,1)
        th1f_wgjets_2_photon_pt.Fill(photon.pt(),1)
        th1f_wgjets_2_photon_eta.Fill(photon.eta(),1)
        th1f_wgjets_2_lepton_pt.Fill(electron.pt(),1)
        th1f_wgjets_2_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),1)
    else:
        th1f_wgjets_2_njets.Fill(njets,-1)
        th1f_wgjets_2_nphotons.Fill(nphotons,-1)
        th1f_wgjets_2_nleptons.Fill(nelectrons,-1)
        th1f_wgjets_2_photon_pt.Fill(photon.pt(),-1)
        th1f_wgjets_2_photon_eta.Fill(photon.eta(),-1)
        th1f_wgjets_2_lepton_pt.Fill(electron.pt(),-1)
        th1f_wgjets_2_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),-1)
    #print njets

if countweighted > 0:
    th1f_wgjets_2_njets.Scale(xs_wgjets_2*1000*lumi/countweighted)
    th1f_wgjets_2_nphotons.Scale(xs_wgjets_2*1000*lumi/countweighted)
    th1f_wgjets_2_nleptons.Scale(xs_wgjets_2*1000*lumi/countweighted)
    th1f_wgjets_2_photon_pt.Scale(xs_wgjets_2*1000*lumi/countweighted)
    th1f_wgjets_2_photon_eta.Scale(xs_wgjets_2*1000*lumi/countweighted)
    th1f_wgjets_2_lepton_pt.Scale(xs_wgjets_2*1000*lumi/countweighted)
    th1f_wgjets_2_delta_r.Scale(xs_wgjets_2*1000*lumi/countweighted)

th1f_wgjets_2_njets.SetLineWidth(3)
th1f_wgjets_2_nphotons.SetLineWidth(3)
th1f_wgjets_2_nleptons.SetLineWidth(3)
th1f_wgjets_2_photon_pt.SetLineWidth(3)
th1f_wgjets_2_photon_eta.SetLineWidth(3)
th1f_wgjets_2_lepton_pt.SetLineWidth(3)
th1f_wgjets_2_delta_r.SetLineWidth(3)

th1f_wgjets_2_njets.SetLineColor(ROOT.kGreen)
th1f_wgjets_2_nphotons.SetLineColor(ROOT.kGreen)
th1f_wgjets_2_nleptons.SetLineColor(ROOT.kGreen)
th1f_wgjets_2_photon_pt.SetLineColor(ROOT.kGreen)
th1f_wgjets_2_photon_eta.SetLineColor(ROOT.kGreen)
th1f_wgjets_2_lepton_pt.SetLineColor(ROOT.kGreen)
th1f_wgjets_2_delta_r.SetLineColor(ROOT.kGreen)

c = ROOT.TCanvas()

th1f_wgjets_1_photon_pt.SetMinimum(0)
th1f_wgjets_1_photon_pt.SetMaximum(1.5*max(th1f_wgjets_1_photon_pt.GetMaximum(),th1f_wgjets_2_photon_pt.GetMaximum()))
th1f_wgjets_1_photon_pt.Draw()
th1f_wgjets_1_photon_pt.GetXaxis().SetTitle("photon pt (GeV)")
th1f_wgjets_1_photon_pt.SetStats(0)
th1f_wgjets_2_photon_pt.Draw("same")

leg=ROOT.TLegend(.58,.73,.88,.88)

#leg.AddEntry(th1f_wgjets_1_photon_pt,"wg+jets POWHEG","l")
leg.AddEntry(th1f_wgjets_1_photon_pt,"POWHEG PR 24763","l")
leg.AddEntry(th1f_wgjets_2_photon_pt,"POWHEG","l")


leg.Draw("same")

c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")
