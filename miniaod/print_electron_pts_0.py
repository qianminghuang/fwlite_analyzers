#print out gen particles and lhe particles and electrons

import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://eoscms.cern.ch//eos/cms/store/data/Run2016B/DoubleEG/MINIAOD/03Feb2017_ver2-v2/810000/D64E2D65-5EED-E611-9118-0025901E4A16.root'])

electrons, electronLabel = Handle("std::vector<pat::Electron>"), "slimmedElectrons"

# loop over events
count= 0

for event in events:

    if event.eventAuxiliary().luminosityBlock() != 7:
        continue

    if event.eventAuxiliary().event() != 6723769:
        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())
    
    event.getByLabel(electronLabel, electrons)

    print "electrons\n"

    # Electrons
    for i,el in enumerate(electrons.product()):
        if el.pt() < 5: continue
        print el.pt()
