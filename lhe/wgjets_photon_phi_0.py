import ROOT
import sys
from DataFormats.FWLite import Events, Handle

h_photon_phi=ROOT.TH1F("h_photon_phi","h_photon_phi",70,-3.5,3.5)

lumi = float(1)/float(1000)

#events = Events(['/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_0.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1000.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1001.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1002.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1003.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1004.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1005.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1006.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1007.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1008.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1009.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_100.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1010.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1011.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1012.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1013.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1014.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1015.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1016.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1017.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1018.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1019.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_101.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1020.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1021.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1022.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1023.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1024.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1025.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1026.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1027.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1028.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1029.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_102.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1030.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1031.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1032.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1033.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1034.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1035.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1036.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1037.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1038.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1039.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_103.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1040.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1041.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1042.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1043.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1044.root'])

#events = Events(['/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_0.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1000.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1001.root','/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1002.root'])

#events = Events(['/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_0.root'])

events = Events(['/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1000.root'])

#events = Events(['/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1001.root'])

#events = Events(['/afs/cern.ch//work/a/amlevin/list_root/MiniAOD_5044046_1002.root'])


#events = Events(['/afs/cern.ch/work/a/amlevin/delete_this/mg5_aMCwgjetsewdim6.root'])

handleLHEEventProduct  = Handle ("LHEEventProduct")
#labelLHEEventProduct = ("source")
labelLHEEventProduct = ("externalLHEProducer")

n_weighted_run_over = 0
n_run_over = 0

for event in events:

    n_run_over += 1

    event.getByLabel (labelLHEEventProduct, handleLHEEventProduct)

    lheevent = handleLHEEventProduct.product()

    if lheevent.originalXWGTUP() > 0:
        n_weighted_run_over += 1
    else:    
        n_weighted_run_over -= 1
        
    n_photons = 0

    for i in range(0,len(lheevent.hepeup().IDUP)):
        v=ROOT.TLorentzVector()
        v.SetPxPyPzE(lheevent.hepeup().PUP.at(i)[0],lheevent.hepeup().PUP.at(i)[1],lheevent.hepeup().PUP.at(i)[2],lheevent.hepeup().PUP.at(i)[3])

        if lheevent.hepeup().ISTUP.at(i) != 1:
            continue

        if abs(lheevent.hepeup().IDUP.at(i)) == 22:
            v_pho = v
            n_photons += 1

    assert(n_photons == 1)    

    if lheevent.originalXWGTUP() > 0:
        h_photon_phi.Fill(v_pho.Phi())
    else:
        h_photon_phi.Fill(v_pho.Phi(),-1)

c = ROOT.TCanvas()
h_photon_phi.Draw()
c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")
