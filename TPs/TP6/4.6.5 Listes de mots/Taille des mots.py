import doctest

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
    # l'initialisation des constantes et variables
    res = []
    txt_liste = txt.split()
    for mot in txt_liste:
        counter = 0  # l'initialisation du decompteur
        for ltr in mot:
            counter+=1
        res.append(counter)
    return res


# programme principal
doctest.testmod()