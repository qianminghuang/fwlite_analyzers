import ROOT
import sys
from DataFormats.FWLite import Events, Handle

from math import hypot, pi

def deltaPhi(phi1,phi2):
    ## Catch if being called with two objects                                                                                                                                             
    if type(phi1) != float and type(phi1) != int:
        phi1 = phi1.phi
    if type(phi2) != float and type(phi2) != int:
        phi2 = phi2.phi
    ## Otherwise                                                                                                                                                                          
    dphi = (phi1-phi2)
    while dphi >  pi: dphi -= 2*pi
    while dphi < -pi: dphi += 2*pi
    return dphi

def deltaR(eta1,phi1,eta2=None,phi2=None):
    ## catch if called with objects                                                                                                                                                       
    if eta2 == None:
        return deltaR(eta1.eta,eta1.phi,phi1.eta,phi1.phi)
    ## otherwise                                                                                                                                                                          
    return hypot(eta1-eta2, deltaPhi(phi1,phi2))

lumi = float(1)/float(1000)

events = Events(['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIIWinter15pLHE-00008.root'])

handleLHEEventProduct  = Handle ("LHEEventProduct")
labelLHEEventProduct = ("source")

n_weighted_run_over = 0
n_weighted_selected = 0

for event in events:

    event.getByLabel (labelLHEEventProduct, handleLHEEventProduct)

    lheevent = handleLHEEventProduct.product()

    n_leptons = 0
    n_photons = 0

    if lheevent.originalXWGTUP() > 0:
        n_weighted_run_over += 1
    else:
        n_weighted_run_over -= 1

    for i in range(0,len(lheevent.hepeup().IDUP)):
        v=ROOT.TLorentzVector()
        v.SetPxPyPzE(lheevent.hepeup().PUP.at(i)[0],lheevent.hepeup().PUP.at(i)[1],lheevent.hepeup().PUP.at(i)[2],lheevent.hepeup().PUP.at(i)[3])

        if lheevent.hepeup().ISTUP.at(i) != 1:
            continue

        if abs(lheevent.hepeup().IDUP.at(i)) == 11 or abs(lheevent.hepeup().IDUP.at(i)) == 13 or abs(lheevent.hepeup().IDUP.at(i)) == 15:
            v_lep = v
            n_leptons += 1

        if abs(lheevent.hepeup().IDUP.at(i)) == 22:
            v_pho = v
            n_photons += 1

    assert(n_leptons == 1 and n_photons == 1)    

    if  deltaR(v_pho.Eta(),v_pho.Phi(),v_lep.Eta(),v_lep.Phi())  < 0.7:
        continue

    if lheevent.originalXWGTUP() > 0:
        n_weighted_selected += 1
    else:
        n_weighted_selected -= 1

acc = float(n_weighted_selected) / n_weighted_run_over

xs = 155.9

print xs * acc
