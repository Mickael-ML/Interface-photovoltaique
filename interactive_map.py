# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:58:11 2022

@author: fbianciotto
"""

import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def interactive_map():
    """
    Affiche la carte des régions françaises, l'utilisateur doit cliquer sur une région pour la sélectionner

    Returns
    -------
    String
        Nom de la région si l'utilisateur a correctement sélectionné une région, sinon retourne "Erreur".

    """
    
    dict_poly = {} # dictionnaire pour stocké les polygones de chaque région
    
    
    #Crée la map avec matplotlib
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    im = plt.imread("fr_region.png")
    fig, ax = plt.subplots()
    im = ax.imshow(im, extent=[0, 450, 0, 450])
    plt.title("Sélectionner une région")
    plt.axis('off') # enlève les valeurs des axes.
    
    # NOUVELLE AQUITAINE 
    coord_nouvelle_aquitaine = [[91,70],[123,174],[120,208],[141,214],[131,244],[163,251],[173,239],[182,242],[202,213],[237,214],[243,185],[230,143],[208,146],[182,97],[150,94],[145,78],[154,72],[139,39],[92,70]]
    poly_nouvelle_aquitaine = Polygon([[p[0], p[1]] for p in coord_nouvelle_aquitaine])
    dict_poly["Nouvelle Aquitaine"]=poly_nouvelle_aquitaine
    #coord_nouvelle_aquitaine.append(coord_nouvelle_aquitaine[0])
    #xs, ys = zip(*coord_nouvelle_aquitaine) #create lists of x and y values
    #plt.plot(xs,ys) 
    
    # OCCITANIE
    coord_occitanie = [[141,41],[154,71],[146,79],[151,93],[181,94],[208,144],[231,141],[236,126],[253,140],[263,127],[275,142],[281,136],[291,134],[302,111],[319,111],[330,97],[311,70],[303,73],[266,50],[268,26],[272,19],[252,13],[232,14],[220,23],[178,38],[173,32],[141,40]]
    poly_occitanie = Polygon([[p[0], p[1]] for p in coord_occitanie])
    dict_poly["Occitanie"]=poly_occitanie
   
    # PACA
    coord_paca = [[313,70],[331,94],[324,110],[356,104],[360,108],[351,119],[381,142],[376,153],[388,155],[406,135],[404,115],[414,108],[428,110],[416,86],[394,65],[394,60],[377,53],[350,60],[350,64],[334,68],[327,65],[313,70]]
    poly_paca = Polygon([[p[0], p[1]] for p in coord_paca])
    dict_poly["PACA"]=poly_paca
   
    # CORSE
    coord_corse = [[435,80],[432,65],[421,64],[413,55],[409,51],[413,48],[409,43],[411,40],[415,38],[411,30],[416,31],[416,27],[413,24],[419,20],[416,17],[430,8],[433,16],[439,35],[441,52],[438,65],[436,80]]
    poly_corse =  Polygon([[p[0], p[1]] for p in coord_corse])
    dict_poly["Corse"]=poly_corse
   
    # AUVERGNE RHONE ALPES
    coord_auvergne_ra = [[231,144],[244,183],[238,214],[258,232],[281,228],[291,203],[306,201],[311,210],[319,209],[322,207],[331,221],[346,214],[356,210],[370,216],[364,205],[371,207],[374,216],[390,217],[396,202],[400,200],[392,190],[407,167],[394,157],[375,153],[379,144],[350,122],[349,117],[356,108],[323,110],[303,113],[292,133],[282,137],[277,144],[262,130],[255,141],[252,141],[236,130],[232,141]]
    poly_auvergne_ra =  Polygon([[p[0], p[1]] for p in coord_auvergne_ra])
    dict_poly["Auvergne Rhône Alpes"]=poly_auvergne_ra
 
    # BOURGOGNE FRANCHE COMTE
    coord_bourgogne_fc = [[264,232],[257,278],[262,284],[265,293],[260,300],[263,309],[276,311],[282,301],[286,299],[290,289],[312,290],[316,295],[327,286],[324,281],[334,275],[337,274],[352,277],[357,288],[364,293],[369,292],[387,289],[397,277],[392,266],[397,262],[367,221],[349,215],[331,222],[320,212],[311,211],[303,206],[294,207],[300,215],[283,231],[266,233]]
    poly_bourgogne_fc =  Polygon([[p[0], p[1]] for p in coord_bourgogne_fc])
    dict_poly["Bourgogne Franche Comté"]=poly_bourgogne_fc
 
    # CENTRE
    coord_centre = [[163,255],[169,271],[189,286],[192,300],[191,309],[196,319],[192,323],[212,337],[223,315],[227,307],[242,306],[245,298],[257,302],[263,293],[255,279],[259,233],[236,219],[202,219],[185,244],[174,242],[165,251]]
    poly_centre =  Polygon([[p[0], p[1]] for p in coord_centre])
    dict_poly["Centre Val de Loire"]=poly_centre
    
    # PAYS DE LA LOIRE 
    coord_pays_loire = [[119,212],[102,220],[91,240],[96,251],[89,254],[88,262],[82,262],[76,271],[91,275],[94,280],[109,282],[116,287],[121,287],[129,295],[129,319],[142,317],[156,320],[162,309],[171,315],[175,316],[176,309],[189,302],[187,289],[168,274],[160,253],[130,247],[136,217],[120,211]]
    poly_pays_loire =  Polygon([[p[0], p[1]] for p in coord_pays_loire])
    dict_poly["Pays de la Loire"]=poly_pays_loire
    
    # BRETAGNE
    coord_bretagne = [[79,273],[25,294],[16,291],[14,303],[6,304],[19,309],[21,312],[14,311],[7,321],[9,328],[30,337],[36,331],[46,332],[50,336],[63,339],[75,322],[87,328],[90,325],[101,330],[105,326],[111,324],[117,319],[125,320],[125,296],[116,290],[93,281],[76,272]] 
    poly_bretagne = Polygon([[p[0], p[1]] for p in coord_bretagne])
    dict_poly["Bretagne"]=poly_bretagne 
    
    # GRAND EST
    coord_grand_est = [[276,312],[279,322],[275,330],[283,345],[283,356],[295,359],[297,371],[302,388],[312,389],[320,399],[321,382],[341,368],[360,366],[381,355],[392,350],[431,347],[421,330],[416,312],[412,290],[411,272],[404,271],[393,286],[368,295],[354,290],[349,281],[339,277],[328,282],[327,290],[318,297],[305,293],[291,293],[286,302],[276,315]]
    poly_grand_est = Polygon([[p[0], p[1]] for p in coord_grand_est])
    dict_poly["Grand Est"]=poly_grand_est

    # NORMANDIE 
    coord_normandie = [[190,304],[179,310],[179,318],[163,314],[156,324],[139,320],[116,324],[116,326],[115,337],[113,356],[103,380],[125,378],[123,371],[126,362],[158,357],[184,363],[169,366],[169,374],[180,380],[195,384],[207,392],[216,387],[219,380],[220,372],[216,360],[218,354],[212,350],[211,339],[190,329],[193,320],[191,318],[186,312],[186,307]]
    poly_normandie= Polygon([[p[0], p[1]] for p in coord_normandie])
    dict_poly["Normandie"]=poly_normandie
   
    # ILE DE FRANCE
    coord_idf = [[213,341],[212,344],[218,351],[230,351],[237,350],[245,347],[253,346],[263,346],[266,342],[274,336],[276,323],[274,316],[264,314],[259,303],[246,300],[243,307],[231,309],[227,313],[214,337] ]
    poly_idf= Polygon([[p[0], p[1]] for p in coord_idf])
    dict_poly["Ile de France"]=poly_idf

    # HAUT DE FRANCE
    coord_haut = [[220,354],[220,365],[221,383],[209,394],[218,401],[214,408],[216,417],[215,428],[218,437],[244,443],[246,437],[255,425],[261,428],[269,416],[280,414],[282,408],[294,407],[297,393],[299,387],[294,374],[293,363],[282,358],[275,336],[266,347],[238,352],[222,354]]
    poly_haut= Polygon([[p[0], p[1]] for p in coord_haut])
    dict_poly["Hauts de France"]=poly_haut
   
    coords = []
    def onclick(event):
        
        global ix, iy
        ix, iy = event.xdata, event.ydata
        #print ('[%d,%d],'%(
        #    ix, iy),end="")

        coords.append((ix, iy))

        if len(coords) == 2:
            fig.canvas.mpl_disconnect(cid)
        plt.close()
        return coords
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick) 
    
    plt.show()
    #print(dict_poly)
    point = Point(coords[0][0], coords[0][1]) # point sélectionné par l'utilisateur
    #Pour chaque polygon de région, cherche si le point sélectionné par l'utilisateur est à l'intérieur du polygon.
    for key, value in dict_poly.items(): 
        #print("test",key)
        if value.contains(point):
            print(key)
            return(key)

    return "Erreur" # si aucune région trouvée retourne "Erreur"

if __name__ == "__main__":
    interactive_map()
