# on importe les modules necessaires
import doctest

# definitions de fonctions

def inversion(li):
    """Inverse l’ordre des éléments d’une liste
    
    Exemples :
    >>> inversion([1,2])
    [2, 1]
    >>> inversion([1,2,3])
    [3, 2, 1]
    >>> inversion([])
    []
    >>> inversion([1,1,2,2])
    [2, 2, 1, 1]
    """
    for i in range(len(li)//2):
        li[i], li[-1-i] =li[-1-i], li[i]
    return li

doctest.testmod()




