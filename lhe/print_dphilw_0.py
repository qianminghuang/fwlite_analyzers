import ROOT
import sys
from DataFormats.FWLite import Events, Handle

from math import hypot, pi, sqrt, acos


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

events = Events (['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIIWinter15pLHE-00008.root'])

lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "source"

for event in events:

#    if event.eventAuxiliary().event() != 16355436:
#    if event.eventAuxiliary().event() != 31915392:
#    if event.eventAuxiliary().event() != 31688057:
#        continue

    event.getByLabel(lheinfoLabel,lheinfo)

    v_photon=ROOT.TLorentzVector();
    v_w=ROOT.TLorentzVector();

    for i in range(0,len(lheinfo.product().hepeup().IDUP)):


        if lheinfo.product().hepeup().IDUP.at(i) == 22:
            v_photon.SetPxPyPzE(lheinfo.product().hepeup().PUP.at(i)[0],lheinfo.product().hepeup().PUP.at(i)[1],lheinfo.product().hepeup().PUP.at(i)[2],lheinfo.product().hepeup().PUP.at(i)[3])

        if abs(lheinfo.product().hepeup().IDUP.at(i)) == 24:
            v_w.SetPxPyPzE(lheinfo.product().hepeup().PUP.at(i)[0],lheinfo.product().hepeup().PUP.at(i)[1],lheinfo.product().hepeup().PUP.at(i)[2],lheinfo.product().hepeup().PUP.at(i)[3])
    print abs(deltaPhi(v_w.Phi(),v_photon.Phi()))

    #break
