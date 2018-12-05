import ROOT
import sys
from DataFormats.FWLite import Events, Handle

h_photon_phi=ROOT.TH1F("h_photon_phi","h_photon_phi",70,-3.5,3.5)

lumi = float(1)/float(1000)

events = Events(['/afs/cern.ch/work/a/amlevin/delete_this/mg5_aMCwgjetsewdim6.root'])

handleLHEEventProduct  = Handle ("LHEEventProduct")
labelLHEEventProduct = ("source")

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
