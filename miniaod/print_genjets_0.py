import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/08DCD9BB-2C25-E711-90C9-C454449229AF.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/10C28C46-3325-E711-A6C1-C454449229EB.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/510000/1A34BCE9-0C25-E711-AA29-0CC47A706D18.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0CF4D76D-6F20-E711-8107-0025901D46E4.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/28209E0A-AB20-E711-9C87-0CC47AC08BF8.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A862BF2F-7520-E711-89F2-0025904C7E02.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BE9758D6-AD20-E711-90E2-0CC47A706CF0.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CC842BFE-AD20-E711-9810-1CC1DE19280C.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FECDF61A-6420-E711-8133-0025904B12FA.root'])

handleGenJets  = Handle ("std::vector<reco::GenJet>")
labelGenJets = ("slimmedGenJets")

for event in events:

    if event.eventAuxiliary().event() != 299896:
        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())
 
    event.getByLabel (labelGenJets, handleGenJets)

    for j in handleGenJets.product():
        print "j.pt() = "+str(j.pt())
