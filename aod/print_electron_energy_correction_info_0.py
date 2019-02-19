import ROOT
import sys
from DataFormats.FWLite import Events, Handle

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EEF150FB-C5B1-E611-87B0-FA163EFD20EB.root'])

events = Events (['root://cms-xrd-global.cern.ch//store/data/Run2016B/DoubleEG/AOD/23Sep2016-v3/00000/A0FC15A4-1998-E611-A2D1-0242AC130003.root'])

electrons,electronsLabel = Handle("vector<reco::GsfElectron>"), 'gedGsfElectrons'

# loop over events
count= 0
for event in events:

    event.getByLabel(electronsLabel, electrons)

    if event.eventAuxiliary().luminosityBlock() != 7:
        continue

    if event.eventAuxiliary().event() != 6723769:
        continue

    for electron in electrons.product():

        print "electron.isEcalEnergyCorrected() = "+str(electron.isEcalEnergyCorrected())
        print "electron.pt() = "+str(electron.pt())
        print "electron.ecalEnergy() = " + str(electron.ecalEnergy())
        print "electron.correctedEcalEnergy() = " + str(electron.correctedEcalEnergy())
        print "electron.superCluster().energy() = "+str(electron.superCluster().energy())
