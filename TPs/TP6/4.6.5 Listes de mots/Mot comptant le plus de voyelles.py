import doctest

def nb_de_voyelles(mot):
    """Reçoit un mot (sans espaces) et renvoie son nombre de voyelles
    
    Exemples :
    >>> nb_de_voyelles('aaa')
    3
    >>> nb_de_voyelles('Emma')
    2
    >>> nb_de_voyelles('yolk')
    2
    """
    res = 0
    for ltr in mot:
        if ltr in 'AEUOIYaeuioy':
            res+=1
    return res

def mot_avec_plus_de_voyelles(txt):
    """Reçoit un texte et renvoie le mot de ce texte qui
    compte le plus de voyelles
    
    Exemples :
    >>> mot_avec_plus_de_voyelles("I don't like you")
    'you'
    >>> mot_avec_plus_de_voyelles("A cat")
    'A'
    >>> mot_avec_plus_de_voyelles("Good")
    'Good'

    """
    txt_liste = txt.split()
    max_vlls = 0
    res = ""
    for mot in txt_liste:
        counter = 0     # l'initialisation du decompteur
        for ltr in mot:
            if ltr in 'AEUOIYaeuioy':
                counter+=1
        if counter> max_vlls:
            max_vlls = counter
            res = mot
    return res






# programme principal
doctest.testmod()