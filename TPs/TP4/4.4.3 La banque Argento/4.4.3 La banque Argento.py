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
    INT = 1.05
    COUT = 11
    # l'initialisation d'un decompteur pour gerer la boucle suivante
    i = 0 
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
    res = False
    if capital(nba,deb)>deb:
        res = True
    return res

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
    while i<nb_annees:
        but = (but + 11) / 1.05
        i+=1
    return capital

def dureeMin(capital,but):
    """
    Calcule la durée minimum de placement avec
    un capital de départ donné pour atteindre le capital but souhaité.

    Exemples :
    >>> dureeMin(100,1000)
    -1
    >>> dureeMin(300,1000)
    47
    """
    DUR = 1
    cap_init = capital
    n = 0
    while capital<but and cap_init<capital:
        capital = capital(DUR,capital)
        n+=1
    if cap_init>capital:
        n=-1
    return n


# on teste les fonctions
doctest.testmod()







