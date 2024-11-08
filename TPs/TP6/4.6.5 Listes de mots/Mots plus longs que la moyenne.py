import doctest
from statistics import mean

def taille_de_mots(txt):
    """Reçoit un texte et renvoie une liste d’entiers contenant
    la taille de chacun de ses mots.
    
    Exemples :
    >>> taille_de_mots("")
    []
    >>> taille_de_mots("Hello kitty girl")
    [5, 5, 4]
    >>> taille_de_mots("HI")
    [2]
    >>> taille_de_mots("I'm tired")
    [3, 5]
    """
    # l'inilisation des constantes et variables
    res = []
    txt_liste = txt.split()
    for mot in txt_liste:
        counter = 0  # l'initialisation du decompteur
        for ltr in mot:
            counter+=1
        res.append(counter)
    return res

def plus_de_la_moyenne(txt):
    """Reçoit un texte et affiche tous les mots qui
    sont plus longs que la longueur moyenne de ses mots.
    
    Exemples :
    >>> plus_de_la_moyenne("Chat chien éléphant")
    ['éléphant']
    
    >>> plus_de_la_moyenne("Un deux trois quatre cinq")
    ['trois', 'quatre']
    
    >>> plus_de_la_moyenne("Python est génial")
    ['Python', 'génial']
    
    >>> plus_de_la_moyenne("abc a abcd")
    ['abc', 'abcd']
    
    >>> plus_de_la_moyenne("word")
    []
    """
    moyenne = mean(taille_de_mots(txt))
    txt_liste = txt.split()
    res = []
    for mot in txt_liste:
        compteur = 0 # l'inilisation du decompteur
        for _ in mot:
            compteur+=1
        if compteur>moyenne:
            res.append(mot)
    return res



# programme principal
doctest.testmod()