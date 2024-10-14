# on importe les modules utilises
import doctest

# les definitions des fonctions
def capital(nba,deb):
    """
    Renvoie le capital en euros sur un tel compte au bout
    de nba en plaçant initialement (année 0) un capital égal à deb (en euros).

    Exemples :
    >>> capital(1,0)
    -11.0
    >>> capital(2,100)
    87.7
    """
    # definitions des constantes
    INT = 1.05   # taux d'interet
    COUT = 11    # coût annuel
    # l'initialisation d'un decompteur pour gerer la boucle suivante
    i = 0 
    # boucle sur les années pour accumuler les intérêts et soustraire le coût
    while i<nba:
        deb=deb*INT-COUT
        i+=1
    return deb

def gagne(nba,deb):
    """
    Renvoie un booléen indiquant si le capital au bout de
    nba années sur un tel compte est (ou non) supérieur ou égal au capital de début deb.
    Exemples:
    >>> gagne(1,100)
    False
    >>> gagne(10,1000)
    True
    >>> gagne(1,0)
    False

    """
    return capital(nba,deb)>deb

def capMin(nb_annees,but):
    """
    Calcule le placement minimum nécessaire pour
    atteindre au moins le capital but après nb_annees d’économies.

    Par exemple :
    >>> capMin(7,500) 
    418.99077243643393
    >>> capMin(10,2000) 
    1312.7655913025512
    """
    i = 0
    # la boucle pour trouver le capital minimum en reversant l'algortihme principal
    while i<nb_annees:
        but = (but + 11) / 1.05
        i+=1
    return but

def dureeMin(cap_init,but):
    """
    Calcule la durée minimum de placement avec
    un capital de départ donné pour atteindre le capital but souhaité.

    Exemples :
    >>> dureeMin(100,1000)
    -1
    >>> dureeMin(300,1000)
    47
    >>> dureeMin(500, 500)
    0
    >>> dureeMin(500, 400)
    0
    >>> dureeMin(1000, 2000)
    17
    >>> dureeMin(0, 1000)
    -1
    >>> dureeMin(100, 0)
    0
    """
    cap = cap_init
    n = 0     # valeur renvoiee par defaut (si but>=cap)

    # tant que le capital est inférieur au but et diminue pas avec chaque pas
    while cap<but and cap_init<=cap:
        cap = capital(1,cap)  # on calcule le capital nouveau
        n+=1
    
    # si le capital est tombe en dessous du capital initial alors
    if cap_init>cap:
        n=-1

        
    return n


# on teste les fonctions
doctest.testmod()







