import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EEF150FB-C5B1-E611-87B0-FA163EFD20EB.root'])

genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

photons,photonsLabel = Handle("vector<reco::Photon>"), 'gedPhotons'
electrons,electronsLabel = Handle("vector<reco::GsfElectron>"), 'gedGsfElectrons'

# loop over events
count= 0
for event in events:

#    if event.eventAuxiliary().luminosityBlock() != 2219:
#        continue

#    if event.eventAuxiliary().event() != 355277974:
#        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())

    event.getByLabel(genParticlesLabel, genparticles)
    event.getByLabel(electronsLabel, electrons)
    event.getByLabel(photonsLabel, photons)

    print "photons:"
    print ""

    for photon in photons.product():
        print str(photon.pt())+" "+str(photon.eta())+" "+str(photon.phi())+" "+str(photon.superCluster().eta())


    print ""    
    print "electrons:"
    print ""

    for electron in electrons.product():
        print str(electron.pt())+" "+str(electron.eta())+" "+str(electron.phi())+" "+str(electron.superCluster().eta())

#    for genparticle in genparticles.product():

#        if genparticle.mother(0) and genparticle.mother(1):
#            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+ str(genparticle.mother(0).eta())+ " " +str(genparticle.mother(0).phi()) +" "+str(genparticle.mother(1).pdgId())+" "+str(genparticle.mother(1).pt())+" "+str(genparticle.mother(1).eta())+" "+str(genparticle.mother(1).phi())+" "+str(genparticle.numberOfMothers())
#        elif genparticle.mother(0):
#            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+str(genparticle.mother(0).eta())+" "+ str(genparticle.mother(0).phi())+" "+str(genparticle.numberOfMothers())
#        else:
#            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.numberOfMothers())
