import ROOT
import sys
from DataFormats.FWLite import Events, Handle

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/10BFD217-3702-E811-A0B4-0CC47A009E24.root'])

events = Events (['/eos/user/w/wangk/andrew/miniaodsim/wpa_powheg/mergeStep3_1990175_7.root'])

lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "externalLHEProducer"

for event in events:

    if event.eventAuxiliary().event() != 377852:
        continue

    event.getByLabel(lheinfoLabel,lheinfo)

    for i in range(0,len(lheinfo.product().hepeup().IDUP)):
        print lheinfo.product().hepeup().IDUP.at(i)

    break
