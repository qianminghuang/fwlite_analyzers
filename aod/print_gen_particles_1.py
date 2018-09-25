import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EEF150FB-C5B1-E611-87B0-FA163EFD20EB.root'])

genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

# loop over events
count= 0
for event in events:

#    if event.eventAuxiliary().luminosityBlock() != 2219:
#        continue

    if event.eventAuxiliary().event() != 355277974:
        continue

    event.getByLabel(genParticlesLabel, genparticles)

    for genparticle in genparticles.product():

        if genparticle.mother(0) and genparticle.mother(1):
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+ str(genparticle.mother(0).eta())+ " " +str(genparticle.mother(0).phi()) +" "+str(genparticle.mother(1).pdgId())+" "+str(genparticle.mother(1).pt())+" "+str(genparticle.mother(1).eta())+" "+str(genparticle.mother(1).phi())+" "+str(genparticle.numberOfMothers())
        elif genparticle.mother(0):
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+str(genparticle.mother(0).eta())+" "+ str(genparticle.mother(0).phi())+" "+str(genparticle.numberOfMothers())
        else:
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.numberOfMothers())

        print "    genparticle.statusFlags().isLastCopyBeforeFSR() = "+str(genparticle.statusFlags().isLastCopyBeforeFSR())
        print "    genparticle.statusFlags().isLastCopy() = "+str(genparticle.statusFlags().isLastCopy())
        print "    genparticle.statusFlags().isFirstCopy() = "+str(genparticle.statusFlags().isFirstCopy())
        print "    genparticle.statusFlags().fromHardProcessBeforeFSR() = "+str(genparticle.statusFlags().fromHardProcessBeforeFSR())
        print "    genparticle.statusFlags().isDirectHardProcessTauDecayProduct() = "+str(genparticle.statusFlags().isDirectHardProcessTauDecayProduct())
        print "    genparticle.statusFlags().isHardProcessTauDecayProduct() = "+str(genparticle.statusFlags().isHardProcessTauDecayProduct())
        print "    genparticle.statusFlags().fromHardProcess() = "+str(genparticle.statusFlags().fromHardProcess())
        print "    genparticle.statusFlags().isHardProcess() = "+str(genparticle.statusFlags().isHardProcess())
        print "    genparticle.statusFlags().isDirectHadronDecayProduct() = "+str(genparticle.statusFlags().isDirectHadronDecayProduct())
        print "    genparticle.statusFlags().isDirectPromptTauDecayProduct() = "+str(genparticle.statusFlags().isDirectPromptTauDecayProduct())
        print "    genparticle.statusFlags().isDirectTauDecayProduct() = "+str(genparticle.statusFlags().isDirectTauDecayProduct())
        print "    genparticle.statusFlags().isPromptTauDecayProduct() = "+str(genparticle.statusFlags().isPromptTauDecayProduct())
        print "    genparticle.statusFlags().isTauDecayProduct() = "+str(genparticle.statusFlags().isTauDecayProduct())
        print "    genparticle.statusFlags().isDecayedLeptonHadron() = "+str(genparticle.statusFlags().isDecayedLeptonHadron())
        print "    genparticle.statusFlags().isPrompt() = "+str(genparticle.statusFlags().isPrompt())

