import ROOT
import sys
from DataFormats.FWLite import Events, Runs, Handle

runs = Runs(["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/40000/10BFD217-3702-E811-A0B4-0CC47A009E24.root"])

handleLHERunInfoProduct  = Handle ("LHERunInfoProduct")
labelLHERunInfoProduct = ("externalLHEProducer")

found_run_card = False

for run in runs:
    
    run.getByLabel(labelLHERunInfoProduct, handleLHERunInfoProduct)

    header = handleLHERunInfoProduct.product().headers_begin()

    while header != handleLHERunInfoProduct.product().headers_end():

        if not ((not found_run_card and header.tag() == "MGRunCard") or header.tag() == "initrwgt"):
            header = header+1    
            continue
        
        if header.tag() == "MGRunCard":
            found_run_card = True

        print "len(header.lines()) = "+str(len(header.lines()))

        print "header.tag() = "+str(header.tag())

        for i in range(0,len(header.lines())):
            print header.lines()[i].rstrip("\n")

        header = header+1    


    break
