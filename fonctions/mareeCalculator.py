from datetime import *
from math import *

def marreCalculator(TMarreeHaute, HMarreeHaute, TMarreeBasse, HMarreeBasse, time):
    """
       Calcule la hauteur de l'eau

       @type  TMarreeHaute: time
       @param TMarreeHaute: heure de maree haute
       @type  HMarreeHaute: float
       @param HMarreeHaute: hauteur de l'eau à maree haute
       @type TMarreeBasse: time
       @param TMarreeBasse: heure de maree basse
       @type HMarreeBasse: float
       @param HMarreeBasse: hauteur de l'eau à maree basse
       @type time: time
       @param time: temps de la journee
       @rtype: float
       @return: hauteur de l'eau

       @author: Maxime Favier
       @since: 0.4
       @version: 0.
       """
    # TODO gestion entre 2 jours + conversion minutes
    # calcul de la durée de la marée
    durreMaree = abs(TMarreeBasse - TMarreeHaute)
    print("durre marre", durreMaree)
    # calcul de l'heure marée
    heureMaree = durreMaree / 6
    print("heureMaree", heureMaree)
    # calcul du marnage et du 12éme
    marnage = HMarreeHaute - HMarreeBasse
    print("marnage", marnage)
    douzieme = marnage / 12
    print("douzième", douzieme)
    # durée ecoulée entre la basse mer et le tmps demandé
    duree = abs(time - TMarreeBasse)
    print("duree", duree)
    # convertissons en heure-marée
    convertHM = duree / heureMaree
    print("convertHM", convertHM)
    # calcul des douzièmes
    dz = [douzieme, douzieme * 2, douzieme * 3, douzieme * 3, douzieme * 2, douzieme]
    arrHt = floor(convertHM)
    reste = convertHM - arrHt
    # produit en croix
    print("reste", reste, 'arrHt', arrHt)
    x = reste * dz[arrHt]
    print("prd x", x)
    # calcul de l'augmentation de la hauteur de l'eau
    deltaH = x
    for i in range(arrHt):
        deltaH += dz[i]
    print("deltaH", deltaH)
    # hauteur d'eau final
    out = deltaH + HMarreeBasse
    print("heuteur d'eau final", out)



marreCalculator(724, 7.3, 1072, 1.6, 970)