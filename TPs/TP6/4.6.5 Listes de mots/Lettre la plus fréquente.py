import doctest

def lettre_la_plus_frequente(txt):
    """Reçoit un texte et renvoie la lettre
    qui est présente le plus souvent dans ce texte
    
    Exemples :
    >>> lettre_la_plus_frequente("I hate this place")
    'a'
    >>> lettre_la_plus_frequente("My cat Melly meows")
    'm'
    >>> lettre_la_plus_frequente("HAHA!!!!")
    'a'
    """
    NB_LTRS = 26
    A_IND = ord('a')
    lettres_liste = [0]*NB_LTRS
    txt_lower = txt.lower()
    txt_liste = list(txt_lower)
    for el in txt_liste:

        # on verifie que la lettre appartient a l'alphabet latin
        if el.isalpha():
            # on incremente le decompteur responsable pour chaque lettre de la liste 
            lettres_liste[ord(el)-A_IND] = lettres_liste[ord(el)-A_IND]+1
    
    maxim = max(lettres_liste)
    lettre = chr(A_IND+lettres_liste.index(maxim))

    return lettre




# programme principal

doctest.testmod()