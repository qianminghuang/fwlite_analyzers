import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/0211D6FC-5A02-E811-98F1-E0071B7AC750.root'])

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/00366B16-2804-E811-82A4-C4346BBC9BB0.root']) 

handleLHEEventProduct  = Handle ("LHEEventProduct")
labelLHEEventProduct = ("externalLHEProducer")

for event in events:

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())
 
    event.getByLabel (labelLHEEventProduct, handleLHEEventProduct)

    lheevent = handleLHEEventProduct.product()
    
    print lheevent.weights().size()
    for i in range(0,lheevent.weights().size()):
        print lheevent.weights()[i].wgt

    sys.exit(0)
