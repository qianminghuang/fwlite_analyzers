import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIISummer15wmLHEGS-00183.root'])

genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

# loop over events
count= 0
for event in events:

    count = count + 1

    if event.eventAuxiliary().luminosityBlock() != 1:
        continue

    if event.eventAuxiliary().event() != 141:
        continue

    event.getByLabel(genParticlesLabel, genparticles)

    #if count != 300:
    #    continue

    for genparticle in genparticles.product():

        if genparticle.mother(0) and genparticle.mother(1):
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+ str(genparticle.mother(0).eta())+ " " +str(genparticle.mother(0).phi()) +" "+str(genparticle.mother(1).pdgId())+" "+str(genparticle.mother(1).pt())+" "+str(genparticle.mother(1).eta())+" "+str(genparticle.mother(1).phi())+" "+str(genparticle.numberOfMothers())
        elif genparticle.mother(0):
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+str(genparticle.mother(0).eta())+" "+ str(genparticle.mother(0).phi())+" "+str(genparticle.numberOfMothers())
        else:
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.numberOfMothers())

    break
