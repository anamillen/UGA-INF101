# l'import de modules
import turtle
from se_deplacer.se_deplacer_2 import descendre_sans_tracer
from se_deplacer.se_deplacer_1 import aller_sans_tracer
from Polygone.polygone_2 import diametre_polygone
from Polygone.polygone_1 import polygone
from carres_imbriques import carre




def colonne_polygone(nb_poly, cote):
    '''
    Trace nb_poly polygones sur la même colonne, 
    en commençant par un triangle et en augmentant 
    le nombre de côtés de 1 à chaque fois
    La longueur du côté des polygones est toujours
    égale à cote

    Tests:
    colonne_polygone(4, 20)
    colonne_polygone(5, 30)
    colonne_polygone(1,200)


    '''
    DIST = 5 # distance a sauter entre les polygones


    cote_i = 3    # l'initialisation du decompteur
    traces = 0
    while traces<nb_poly:
        # on trace un polygone avec cote_i cotes et la longueur de un cote = cote
        polygone(cote_i, cote)  
        
        diam = diametre_polygone(cote_i, cote)  # on obtient la val du diametre du poly
        descendre_sans_tracer(diam+DIST)        # on descend distance = diam+DIST
        # on augmente les decompteurs
        cote_i+=1 
        traces+=1      
    # d'ici cote_i = nb_poly


def pavage(nb_poly, nb_col, cote):
    """
    La fonction dessine un pavage de polygones dans un plan, où le nombre de polygones
    par colonne est spécifié par `nb_poly` et le nombre de colonnes par `nb_col`.
    Le côté des polygones est initialement de longueur `cote` pour la première colonne, 
    puis augmente de AUG unités à chaque nouvelle colonne. Les polygones dans chaque colonne 
    sont alignés verticalement, avec une ordonnée fixe pour le point de départ. Les colonnes 
    sont espacées horizontalement de `diam + AUG` unités, où `diam` est le diamètre du dernier polygone
    tracé dans la précédente colonne.
    Tests:
    pavage(4,3,20)
    pavage(5, 3, 50)
    """
    # l'initialisation de constantes
    x = -270
    Y = 330
    COTE_INIT = 3
    AUG = 10

    aller_sans_tracer(x,Y)  # turtle se desplace aux (x,y)
    i = 0  # l'initialisation du decompteur pour la boucle
    while i < nb_col:
        colonne_polygone(nb_poly, cote)  # on dessine 1 colonne de polys
        diam = diametre_polygone(COTE_INIT+nb_poly,cote) # on trouve le diametre du dernier poly
        x+= diam+AUG     # prochaine abscisse
        if i!=nb_col-1:   
            aller_sans_tracer(x,Y)    
        # on augmente les decompteurs
        cote+=AUG
        i+=1
    # d'ici i = nb_col


# programme principal

# l'initialisation de constantes
N_POLY = 3
N_COL = 3
COTE_PAVAGE = 20
N_CARRE = 5
COTE_CARRE = 100

# appel aux fonctions
pavage(N_POLY,N_COL,COTE_PAVAGE)
carre(COTE_CARRE, N_CARRE)















