import ROOT
import sys
from DataFormats.FWLite import Events, Runs, Handle

#runs = Runs(["/afs/cern.ch/project/afs/var/ABS/recover/R.1935065321.12130256/list_root/MiniAOD_5044046_0.root"])
#runs = Runs(["/eos/cms/store/user/amlevin/data/miniaod_root/MiniAOD_5223734_0.root"])
#runs = Runs(["/eos/user/a/amlevin/data/miniaod_root/MiniAOD_5532529_0.root"])
#runs = Runs(["/eos/user/w/wangk/andrew/miniaodsim/wpa_powheg/mergeStep3_1990171_15.root"])
runs = Runs(["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC332430-9C04-E811-8B94-008CFA1983BC.root"])
#runs = Runs(["/afs/cern.ch/work/a/amlevin/miniaod_root/MiniAOD_5223734_1920.root"])

handleLHERunInfoProduct  = Handle ("LHERunInfoProduct")
labelLHERunInfoProduct = ("externalLHEProducer")

for run in runs:
    
    run.getByLabel(labelLHERunInfoProduct, handleLHERunInfoProduct)

    header = (handleLHERunInfoProduct.product().headers_begin()+6)

    print "len(header.lines()) = "+str(len(header.lines()))

    print header.tag()

    for i in range(0,len(header.lines())):
        print header.lines()[i]

    break
