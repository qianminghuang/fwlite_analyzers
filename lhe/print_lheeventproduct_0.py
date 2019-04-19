import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/10BFD217-3702-E811-A0B4-0CC47A009E24.root'])

lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "externalLHEProducer"

for event in events:

    event.getByLabel(lheinfoLabel,lheinfo)

    print lheinfo.product().originalXWGTUP()
    print len(lheinfo.product().weights())
    break
