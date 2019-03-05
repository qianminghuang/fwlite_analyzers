import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleElectron/MINIAOD/03Feb2017_ver2-v2/110000/8E9BFBDA-49EB-E611-A3F8-6C3BE5B58198.root '])

photons, photonLabel = Handle("std::vector<pat::Photon>"), "slimmedPhotons"


for event in events:

    #if event.eventAuxiliary().luminosityBlock() != 209529:
    #    continue

    if event.eventAuxiliary().event() != 129105394:
        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())

    event.getByLabel(photonLabel,photons)
    
    for pho in photons.product():
        print pho.pt()
        print pho.eta()
        print pho.hasPixelSeed()

        
