import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/30000/12B7972F-B066-E811-94CF-002590E7DDE6.root'])

genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

# loop over events
count= 0
for event in events:

#    if event.eventAuxiliary().luminosityBlock() != 2219:
#        continue

    if event.eventAuxiliary().event() != 42251686:
        continue

    event.getByLabel(genParticlesLabel, genparticles)

    for genparticle in genparticles.product():

        if genparticle.mother(0) and genparticle.mother(1):
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+ str(genparticle.mother(0).eta())+ " " +str(genparticle.mother(0).phi()) +" "+str(genparticle.mother(1).pdgId())+" "+str(genparticle.mother(1).pt())+" "+str(genparticle.mother(1).eta())+" "+str(genparticle.mother(1).phi())+" "+str(genparticle.numberOfMothers())
        elif genparticle.mother(0):
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+str(genparticle.mother(0).eta())+" "+ str(genparticle.mother(0).phi())+" "+str(genparticle.numberOfMothers())
        else:
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.numberOfMothers())
