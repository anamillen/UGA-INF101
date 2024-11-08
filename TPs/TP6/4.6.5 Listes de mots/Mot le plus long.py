import doctest

def mot_le_plus_long(txt):
    """Reçoit un texte et renvoie son mot le plus long
    
    Exemples :
    >>> mot_le_plus_long("У себя дома я держу глазовыколупывалку")
    'глазовыколупывалку'
    >>> mot_le_plus_long("ME")
    'ME'
    >>> mot_le_plus_long("Who's ready")
    "Who's"
    """
    max_ltr = 0
    res = ""
    txt_liste = txt.split()
    for mot in txt_liste:
        counter = 0
        for ltr in mot:
            counter+=1
        if counter>max_ltr:
            max_ltr = counter
            res = mot
    return res



# programme principal
doctest.testmod()