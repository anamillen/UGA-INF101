# on importe les modules necessaires
import doctest

# definitions de fonctions
def minimum(li):
    """Renvoie l’élément le plus petit de li
    
    Exemples:
    >>> minimum([3,0,-3])
    -3
    >>> minimum([])
    
    >>> minimum([-10,-2,0])
    -10
    """
    if len(li)<1:
        minim = None
    else:   # si la liste li n'est pas vide
        minim = li[0]
        for el in li:
            if el<minim: minim = el
    return minim

def contient(li,elem):
    """Renvoie True si elem est présent dans l, False sinon. Sans utiliser in.

    Exemples :
    >>> contient([],"")
    False
    >>> contient([2,3,4],4)
    True
    >>> contient([1,2,3],0)
    False
    """
    res = False
    i = 0
    long = len(li)
    while i<long:
        if elem==li[i]: res = True
        i+=1
    # a partir d'ici i>=long
    return res

def min_plus_grand_que(li, x):
    """Renvoie le plus petit élément de li 
    qui est strictement plus grand que la valeur x. 
    S’il n’y en a aucun, renvoie None.
    
    Exemples :
    >>> min_plus_grand_que([], 10)
    
    >>> min_plus_grand_que([1,2,3,4],5)

    >>> min_plus_grand_que([1,2,2.5,2.6,3,4], 2)
    2.5
    """
    li_supp = []
    for el in li:
        if el>x:
            li_supp.append(el)
    if len(li_supp)<1:
        res = None
    else:   # s'il y a d'elements qui sont > x alors
        res = minimum(li_supp)
    return res

def minimum2(li):
    """Renvoie le deuxième valeur la plus petite de li (i.e., la
    plus petite valeur strictement supérieure au minimum).
    Si aucun element n'est plus grand que le minimum renvoie None
    
    Exemples :
    >>> minimum2([])
    
    >>> minimum2([2,2])
    
    >>> minimum2([12,4,2,76,23,2,6])
    4
    """    
    minim = minimum(li)
    return min_plus_grand_que(li, minim)        


def minimum3(li):
    """Renvoie le 2e élément le plus petit de liste 
    mais au sens large : par exemple si le minimum est présent plusieurs fois,
    alors le 2e minimum a la même valeur que le premier.
    
    Exemples :
    >>> minimum3([4,5,2,2])
    2
    >>> minimum3([1,2,2,4,5])
    2
    >>> minimum3([])

    >>> minimum3([0])

    >>> minimum3([2,2.3])
    2.3
    """
    if len(li)<2:
        res = None
    else: # si la liste contient plus de 2 elements
        minim = minimum(li)
        li.remove(minim)
        if minim in li:
            res = minim
        else: # si le minimum ne se repete pas, alors
            res = min_plus_grand_que(li, minim)
    return res




# programme principal
doctest.testmod()









