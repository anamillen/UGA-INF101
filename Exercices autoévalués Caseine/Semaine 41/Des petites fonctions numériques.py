"""
Les fonctions demandées ne sont a priori pas dépendantes les unes des autres. Vous pouvez les écrire dans l'ordre que vous voulez.

1) Ecrire une fonction f qui prend un nombre x en argument et qui renvoie la valeur de 4x2-x+5.

2) Considérons un triangle ABC rectangle en A. Ecrire une fonction coteAB(coteAC, hypotenuse) qui prend en argument 
la longueur du côté AC et la longueur de l'hypoténuse et qui renvoie la longueur du côté AB.

3) Ecrire une fonction conversion_feet_m qui prend comme argument une longueur en pieds et qui renvoie la longueur en mètres correspondante. 
On utilisera le taux de conversion suivant: 1 pied=0.3048m.

4) Etant donnés deux points A et B de coordonnées (xA,yA) et (xB,yB), la distance Manhattan entre A et B est donnée par la formule suivante:

d=|xA-xB|+|yA-yB|

(les barres verticales désignent la valeur absolue, dont le nom en Python est abs) . 
Elle porte ce nom car c'est la distance qu'il faut parcourir pour aller de A à B en utilisant seulement des directions parallèles à l'axe 
des abscisses ou à l'axe des ordonnées (comme le quadrillage des rues de Manhattan). Ecrire une fonction distance_manh(xA, yA, xB, yB) 
qui renvoie la distance Manhattan entre A et B.

(Exercice proposé par Aurélie Lagoutte)
"""


# on importe les modules necessaires
import math
# definitions de fonctions
def f(x):
    """Prend un nombre x en argument et renvoie la valeur de 4x^2+5"""
    A = 4; B = -1; C = 5   # definition de coefficients
    res = A*x**2+B*x+C     # calcul de resultat
    return res

def coteAB(AC, h):
    """Prend en argument la longueur du côté AC et la longueur de l'hypoténuse  et renvoie la longueur du côté AB"""
    
    AB = math.sqrt(h**2-AC**2)
    return AB
    

def conversion_feet_m(l):
    """Prend comme argument une longueur en pieds et renvoie la longueur en mètres correspondante"""
    TAUX = 0.3048
    res = l*TAUX
    return res
    
def distance_manh(xA,yA,xB,yB):
    """
    La fonction renvoie la distance Manhattan entre A et B.
    Etant donnés deux points A et B de coordonnées (xA,yA) et (xB,yB), 
    la distance Manhattan entre A et B est donnée par la formule suivante:
    d=|xA-xB|+|yA-yB|
    """
    xd = abs(xA-xB)
    yd = abs(yA-yB)
    return xd+yd

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")