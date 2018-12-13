import ROOT
import sys
from DataFormats.FWLite import Events, Runs, Handle

runs = Runs(["/afs/cern.ch/project/afs/var/ABS/recover/R.1935065321.12130256/list_root/MiniAOD_5044046_249.root"])

handleLHERunInfoProduct  = Handle ("LHERunInfoProduct")
labelLHERunInfoProduct = ("externalLHEProducer")

for run in runs:
    
    run.getByLabel(labelLHERunInfoProduct, handleLHERunInfoProduct)

    header = (handleLHERunInfoProduct.product().headers_begin()+3)

    for i in range(0,len(header.lines())):
        print header.lines()[i]

    break
