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

#events_wgjets_1 = Events (['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIISummer15wmLHEGS-00183_LO.root'])
#events_wgjets_1 = Events (['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIISummer15wmLHEGS-00183_NLO.root'])

#events_wgjets_1 = Events (['/afs/cern.ch/work/a/amlevin/delete_this/HIG-RunIIFall17wmLHEGS-01060.root'])

#events_wgjets_1 = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FEA483D3-AEBE-E611-B8C2-0CC47A706E5E.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FE82A657-5FC0-E611-9C47-002590DE6E5C.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FE462044-B9BE-E611-A01C-0025904B242A.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FCEAFCD3-50BE-E611-B5A5-0CC47A74524E.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FACC9665-35BF-E611-B37D-FA163EC5E4A0.root'])

events_wgjets_1 = Events(['/eos/user/a/amlevin/tmp/F6938E48-06BF-E611-8A82-0CC47A706E5E.root','/eos/user/a/amlevin/tmp/F6BAB4E1-57BE-E611-ABFA-FA163EAB4B9E.root','/eos/user/a/amlevin/tmp/F6CBA788-BBBE-E611-8AC0-0CC47A7E6A8E.root','/eos/user/a/amlevin/tmp/F814E890-E1BE-E611-BA13-0CC47A00AA80.root','/eos/user/a/amlevin/tmp/F88E2345-78BE-E611-8ED0-0CC47A78A3F8.root','/eos/user/a/amlevin/tmp/FA4A76D3-00BF-E611-BCAB-0CC47A00AA80.root','/eos/user/a/amlevin/tmp/FACC9665-35BF-E611-B37D-FA163EC5E4A0.root','/eos/user/a/amlevin/tmp/FCEAFCD3-50BE-E611-B5A5-0CC47A74524E.root','/eos/user/a/amlevin/tmp/FE462044-B9BE-E611-A01C-0025904B242A.root','/eos/user/a/amlevin/tmp/FE82A657-5FC0-E611-9C47-002590DE6E5C.root','/eos/user/a/amlevin/tmp/FEA483D3-AEBE-E611-B8C2-0CC47A706E5E.root'])

#events_wgjets_1 = Events(['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIISummer15wmLHEGS-00183_NLO_W.root'])

events_wgjets_2 = Events (['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIISummer15wmLHEGS-00183_NLO_FxFx.root'])

#events_wgjets_3 = Events(['/afs/cern.ch/user/a/amlevin/delete_this/HIG-RunIIFall17wmLHEGS-01060.root'])

events_wgjets_3 = Events(['/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.3.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.38.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.39.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.95.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.59.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.82.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.50.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.29.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.92.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.4.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.67.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.45.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.71.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.30.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.22.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.42.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.75.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.15.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.99.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.18.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.32.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.17.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.1.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.61.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.91.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.12.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.25.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.36.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.31.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.79.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.6.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.93.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.94.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.10.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.28.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.46.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.81.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.37.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.41.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.20.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.24.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.97.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.85.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.0.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.83.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.66.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.77.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.33.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.23.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.8.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.63.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.11.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.60.root','/eos/user/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.74.root'])



#events_wgjets_3 = Events(['/afs/cern.ch/work/a/amlevin/delete_this/HIG-RunIIFall17wmLHEGS-01060.root.bak','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.43.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.55.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.57.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.64.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.59.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.73.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.45.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.61.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.77.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.51.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.44.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.65.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.75.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.42.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.41.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.54.root','/afs/cern.ch/work/a/amlevin/tmp/HIG-RunIIFall17wmLHEGS-01060.53.root'])

#events_wgjets_3 = Events(['/afs/cern.ch/work/a/amlevin/delete_this/HIG-RunIIFall17wmLHEGS-01060_NLO_POWHEG.root'])

xs_wgjets_1 = 60670
#xs_wgjets_1 = 10980
#xs_wgjets_1 = 495.8
#xs_wgjets_1 = 196.4
#xs_wgjets_1 = 179.1
xs_wgjets_2 = 178.6

xs_wgjets_3 = 10908

#xs_wgjets = xs_wjets


lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "externalLHEProducer"
geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"
genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

# loop over events
count= 0
countweighted = 0

th1f_wgjets_1_njets = ROOT.TH1F("wgjets 1 njets","",7,-0.5,6.5)
th1f_wgjets_2_njets = ROOT.TH1F("wgjets 2 njets","",7,-0.5,6.5)
th1f_wgjets_3_njets = ROOT.TH1F("wgjets 3 njets","",7,-0.5,6.5)

th1f_wgjets_1_nphotons = ROOT.TH1F("wgjets 1 nphotons","",7,-0.5,6.5)
th1f_wgjets_2_nphotons = ROOT.TH1F("wgjets 2 nphotons","",7,-0.5,6.5)
th1f_wgjets_3_nphotons = ROOT.TH1F("wgjets 3 nphotons","",7,-0.5,6.5)

th1f_wgjets_1_nleptons = ROOT.TH1F("wgjets 1 nleptons","",7,-0.5,6.5)
th1f_wgjets_2_nleptons = ROOT.TH1F("wgjets 2 nleptons","",7,-0.5,6.5)
th1f_wgjets_3_nleptons = ROOT.TH1F("wgjets 3 nleptons","",7,-0.5,6.5)

th1f_wgjets_1_photon_pt = ROOT.TH1F("wgjets 1 photon pt","",11,15,125)
th1f_wgjets_2_photon_pt = ROOT.TH1F("wgjets 2 photon pt","",11,15,125)
th1f_wgjets_3_photon_pt = ROOT.TH1F("wgjets 3 photon pt","",11,15,125)

th1f_wgjets_1_photon_eta = ROOT.TH1F("wgjets 1 photon eta","",10,-2.5,2.5)
th1f_wgjets_2_photon_eta = ROOT.TH1F("wgjets 2 photon eta","",10,-2.5,2.5)
th1f_wgjets_3_photon_eta = ROOT.TH1F("wgjets 3 photon eta","",10,-2.5,2.5)

th1f_wgjets_1_lepton_pt = ROOT.TH1F("wgjets 1 lepton pt","",12,5,125)
th1f_wgjets_2_lepton_pt = ROOT.TH1F("wgjets 2 lepton pt","",12,5,125)
th1f_wgjets_3_lepton_pt = ROOT.TH1F("wgjets 3 lepton pt","",12,5,125)

th1f_wgjets_1_delta_r = ROOT.TH1F("wgjets 1 delta r","",35,0,3.5)
th1f_wgjets_2_delta_r = ROOT.TH1F("wgjets 2 delta r","",35,0,3.5)
th1f_wgjets_3_delta_r = ROOT.TH1F("wgjets 3 delta r","",35,0,3.5)

th1f_wgjets_1_njets.Sumw2()
th1f_wgjets_2_njets.Sumw2()
th1f_wgjets_3_njets.Sumw2()

th1f_wgjets_1_nphotons.Sumw2()
th1f_wgjets_2_nphotons.Sumw2()
th1f_wgjets_3_nphotons.Sumw2()

th1f_wgjets_1_nleptons.Sumw2()
th1f_wgjets_2_nleptons.Sumw2()
th1f_wgjets_3_nleptons.Sumw2()

th1f_wgjets_1_photon_pt.Sumw2()
th1f_wgjets_2_photon_pt.Sumw2()
th1f_wgjets_3_photon_pt.Sumw2()

th1f_wgjets_1_photon_eta.Sumw2()
th1f_wgjets_2_photon_eta.Sumw2()
th1f_wgjets_3_photon_eta.Sumw2()

th1f_wgjets_1_lepton_pt.Sumw2()
th1f_wgjets_2_photon_eta.Sumw2()
th1f_wgjets_3_lepton_pt.Sumw2()

th1f_wgjets_1_delta_r.Sumw2()
th1f_wgjets_2_delta_r.Sumw2()
th1f_wgjets_3_delta_r.Sumw2()

f_wjets=ROOT.TFile("/eos/user/a/amlevin/tmp/wjets.root")

t_wjets = f_wjets.Get("demo/events")

wjets_nweightedevents = f_wjets.Get("demo/n_weighted_events_run_over").GetBinContent(1)

for entry in range(t_wjets.GetEntries()):
    
    t_wjets.GetEntry(entry)
    
#    if count > 0:
    if count > 100000:
#    if count > 1000:
#    if count > -1:
        break

    if count % 10000 == 0:
#    if count % 1 == 0:
        print "count = " + str(count)

    count +=1

    if t_wjets.drlgamma < 0.7:
        continue

    if t_wjets.weight > 0:
#        th1f_wgjets_1_njets.Fill(njets,1)
#        th1f_wgjets_1_nphotons.Fill(nphotons,1)
#        th1f_wgjets_1_nleptons.Fill(nelectrons,1)
        th1f_wgjets_1_photon_pt.Fill(t_wjets.photon_pt,1)
        th1f_wgjets_1_photon_eta.Fill(t_wjets.photon_eta,1)
        th1f_wgjets_1_lepton_pt.Fill(t_wjets.electron_pt,1)
        th1f_wgjets_1_delta_r.Fill(t_wjets.drlgamma,1)
    else:
#        th1f_wgjets_1_njets.Fill(njets,-1)
#        th1f_wgjets_1_nphotons.Fill(nphotons,-1)
#        th1f_wgjets_1_nleptons.Fill(nelectrons,-1)
        th1f_wgjets_1_photon_pt.Fill(t_wjets.photon_pt,-1)
        th1f_wgjets_1_photon_eta.Fill(t_wjets.photon_eta,-1)
        th1f_wgjets_1_lepton_pt.Fill(t_wjets.electron_pt,-1)
        th1f_wgjets_1_delta_r.Fill(t_wjets.drlgamma,-1)

    #print njets

c = ROOT.TCanvas()

if wjets_nweightedevents > 0:
    th1f_wgjets_1_njets.Scale(xs_wgjets_1*1000*lumi/wjets_nweightedevents)
    th1f_wgjets_1_nphotons.Scale(xs_wgjets_1*1000*lumi/wjets_nweightedevents)
    th1f_wgjets_1_nleptons.Scale(xs_wgjets_1*1000*lumi/wjets_nweightedevents)
    th1f_wgjets_1_photon_pt.Scale(xs_wgjets_1*1000*lumi/wjets_nweightedevents)
    th1f_wgjets_1_photon_eta.Scale(xs_wgjets_1*1000*lumi/wjets_nweightedevents)
    th1f_wgjets_1_lepton_pt.Scale(xs_wgjets_1*1000*lumi/wjets_nweightedevents)
    th1f_wgjets_1_delta_r.Scale(xs_wgjets_1*1000*lumi/wjets_nweightedevents)

th1f_wgjets_1_njets.SetLineWidth(3)
th1f_wgjets_1_nphotons.SetLineWidth(3)
th1f_wgjets_1_nleptons.SetLineWidth(3)
th1f_wgjets_1_photon_pt.SetLineWidth(3)
th1f_wgjets_1_photon_eta.SetLineWidth(3)
th1f_wgjets_1_lepton_pt.SetLineWidth(3)
th1f_wgjets_1_delta_r.SetLineWidth(3)

th1f_wgjets_1_njets.SetLineColor(ROOT.kRed)
th1f_wgjets_1_nphotons.SetLineColor(ROOT.kRed)
th1f_wgjets_1_nleptons.SetLineColor(ROOT.kRed)
th1f_wgjets_1_photon_pt.SetLineColor(ROOT.kRed)
th1f_wgjets_1_photon_eta.SetLineColor(ROOT.kRed)
th1f_wgjets_1_lepton_pt.SetLineColor(ROOT.kRed)
th1f_wgjets_1_delta_r.SetLineColor(ROOT.kRed)

count = 0
countweighted = 0

for event in events_wgjets_2:

    if count > 50000:
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

    for p in genparticles.product() :

#        if abs(p.pdgId()) == 11 and p.pt() > 25 and (p.statusFlags().isPrompt() or p.statusFlags().isPromptTauDecayProduct()) and p.status() == 1  :
        if p.pdgId() == -11 and p.pt() > 25 and abs(p.eta()) < 2.47 and p.status() == 1 :
            nelectrons += 1
            electron = p

#    print "nelectrons = "+str(nelectrons)

    if nelectrons != 1:
        continue

    nphotons = 0        

    for p in genparticles.product() :

#        if abs(p.pdgId()) == 22 and p.pt() > 25 and (p.statusFlags().isPrompt() or p.statusFlags().isPromptTauDecayProduct()) and p.status() == 1   :
#        if abs(p.pdgId()) == 22 and p.pt() > 15 and abs(p.eta()) < 2.37 and p.status() == 1 and p.statusFlags().isPrompt()  :
        if abs(p.pdgId()) == 22 and p.pt() > 15 and abs(p.eta()) < 2.37 and p.status() == 1 :
            nphotons += 1
            photon = p

#    print "nphotons = "+str(nphotons)

    if nphotons != 1:
        continue

    if deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()) < 0.7:
        continue

    njets = 0        

    for p in genparticles.product() :

#        if (abs(p.pdgId()) == 1 or abs(p.pdgId()) == 2 or abs(p.pdgId()) == 3 or abs(p.pdgId()) == 4 or abs(p.pdgId()) == 5 or abs(p.pdgId()) == 21) and p.pt() > 30 and p.statusFlags().isPrompt() and p.statusFlags().isLastCopy()  :
        if (abs(p.pdgId()) == 1 or abs(p.pdgId()) == 2) and p.pt() > 30 :
            njets +=1

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

th1f_wgjets_2_njets.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_nphotons.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_nleptons.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_photon_pt.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_photon_eta.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_lepton_pt.SetLineColor(ROOT.kBlue)
th1f_wgjets_2_delta_r.SetLineColor(ROOT.kBlue)

count = 0
countweighted = 0

for event in events_wgjets_3:

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

    for p in genparticles.product() :

#        if abs(p.pdgId()) == 11 and p.pt() > 25 and (p.statusFlags().isPrompt() or p.statusFlags().isPromptTauDecayProduct()) and p.status() == 1  :
        if p.pdgId() == -11 and p.pt() > 25 and abs(p.eta()) < 2.47 and p.status() == 1 and p.statusFlags().isPrompt() :
            nelectrons += 1
            electron = p

#    print "nelectrons = "+str(nelectrons)

    if nelectrons != 1:
        continue

    nphotons = 0        

    for p in genparticles.product() :

#        if abs(p.pdgId()) == 22 and p.pt() > 25 and (p.statusFlags().isPrompt() or p.statusFlags().isPromptTauDecayProduct()) and p.status() == 1   
         if abs(p.pdgId()) == 22 and p.pt() > 15 and abs(p.eta()) < 2.37 and p.status() == 1 and p.statusFlags().isPrompt()  :
#        if abs(p.pdgId()) == 22 and p.pt() > 15 and abs(p.eta()) < 10 and p.status() == 1 :
#        if abs(p.pdgId()) == 22 and p.pt() > 15 and abs(p.eta()) < 10 and p.status() == 1 and p.statusFlags().isPrompt():

            nphotons += 1
            photon = p

#    print "nphotons = "+str(nphotons)

    if nphotons != 1:
        continue

    if deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()) < 0.7:
        continue

    njets = 0        

    for p in genparticles.product() :

#        if (abs(p.pdgId()) == 1 or abs(p.pdgId()) == 2 or abs(p.pdgId()) == 3 or abs(p.pdgId()) == 4 or abs(p.pdgId()) == 5 or abs(p.pdgId()) == 21) and p.pt() > 30 and p.statusFlags().isPrompt() and p.statusFlags().isLastCopy()  :
        if (abs(p.pdgId()) == 1 or abs(p.pdgId()) == 2) and p.pt() > 30 :
            njets +=1

    njets = npartons 

    if gen.weight() > 0:
        th1f_wgjets_3_njets.Fill(njets,1)
        th1f_wgjets_3_nphotons.Fill(nphotons,1)
        th1f_wgjets_3_nleptons.Fill(nelectrons,1)
        th1f_wgjets_3_photon_pt.Fill(photon.pt(),1)
        th1f_wgjets_3_photon_eta.Fill(photon.eta(),1)
        th1f_wgjets_3_lepton_pt.Fill(electron.pt(),1)
        th1f_wgjets_3_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),1)
    else:
        th1f_wgjets_3_njets.Fill(njets,-1)
        th1f_wgjets_3_nphotons.Fill(nphotons,-1)
        th1f_wgjets_3_nleptons.Fill(nelectrons,-1)
        th1f_wgjets_3_photon_pt.Fill(photon.pt(),-1)
        th1f_wgjets_3_photon_eta.Fill(photon.eta(),-1)
        th1f_wgjets_3_lepton_pt.Fill(electron.pt(),-1)
        th1f_wgjets_3_delta_r.Fill(deltaR(electron.eta(), electron.phi(), photon.eta(), photon.phi()),-1)
    #print njets

if countweighted > 0:
    th1f_wgjets_3_njets.Scale(xs_wgjets_3*1000*lumi/countweighted)
    th1f_wgjets_3_nphotons.Scale(xs_wgjets_3*1000*lumi/countweighted)
    th1f_wgjets_3_nleptons.Scale(xs_wgjets_3*1000*lumi/countweighted)
    th1f_wgjets_3_photon_pt.Scale(xs_wgjets_3*1000*lumi/countweighted)
    th1f_wgjets_3_photon_eta.Scale(xs_wgjets_3*1000*lumi/countweighted)
    th1f_wgjets_3_lepton_pt.Scale(xs_wgjets_3*1000*lumi/countweighted)
    th1f_wgjets_3_delta_r.Scale(xs_wgjets_3*1000*lumi/countweighted)

th1f_wgjets_3_njets.SetLineWidth(3)
th1f_wgjets_3_nphotons.SetLineWidth(3)
th1f_wgjets_3_nleptons.SetLineWidth(3)
th1f_wgjets_3_photon_pt.SetLineWidth(3)
th1f_wgjets_3_photon_eta.SetLineWidth(3)
th1f_wgjets_3_lepton_pt.SetLineWidth(3)
th1f_wgjets_3_delta_r.SetLineWidth(3)

th1f_wgjets_3_njets.SetLineColor(ROOT.kGreen)
th1f_wgjets_3_nphotons.SetLineColor(ROOT.kGreen)
th1f_wgjets_3_nleptons.SetLineColor(ROOT.kGreen)
th1f_wgjets_3_photon_pt.SetLineColor(ROOT.kGreen)
th1f_wgjets_3_photon_eta.SetLineColor(ROOT.kGreen)
th1f_wgjets_3_lepton_pt.SetLineColor(ROOT.kGreen)
th1f_wgjets_3_delta_r.SetLineColor(ROOT.kGreen)

th1f_wgjets_1_photon_pt.SetMinimum(0)
th1f_wgjets_1_photon_pt.SetMaximum(1.5*max(th1f_wgjets_1_photon_pt.GetMaximum(),th1f_wgjets_2_photon_pt.GetMaximum(),th1f_wgjets_3_photon_pt.GetMaximum()))
th1f_wgjets_1_photon_pt.Draw()
th1f_wgjets_1_photon_pt.GetXaxis().SetTitle("photon pt (GeV)")
th1f_wgjets_1_photon_pt.SetStats(0)
th1f_wgjets_2_photon_pt.Draw("same")
th1f_wgjets_3_photon_pt.Draw("same")


leg=ROOT.TLegend(.58,.73,.88,.88)

#leg.AddEntry(th1f_wgjets_1_photon_pt,"wg+jets POWHEG","l")
leg.AddEntry(th1f_wgjets_1_photon_pt,"w+jets mg5_aMC","l")
leg.AddEntry(th1f_wgjets_3_photon_pt,"wg+jets POWHEG","l")
leg.AddEntry(th1f_wgjets_2_photon_pt,"wg+jets mg5_aMC","l")


leg.Draw("same")

c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")
