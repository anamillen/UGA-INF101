# on importe les modules necessaires
import doctest

# definitions de fonctions
def proche_zero(li):
    """Prend en argument une liste de températures (entiers)
    et renvoie la plus proche de zéro. 
    S’il n’y a aucune température, renvoie 0
    
    Exemples :
    >>> proche_zero([-1,2])
    -1
    >>> proche_zero([])
    0
    >>> proche_zero([0,1])
    0
    >>> proche_zero([8,-8])
    8
    """
    if len(li)<1:
        temp = 0
    else:  # s'il la liste n'est pas vide alors
        temp = li[0]
        for curr in li:
            if abs(curr)<abs(temp): 
                temp = curr
            elif abs(curr) == abs(temp):
                # Pour renvoyer la temperature positive
                temp = max(curr,temp)
    return temp








# programme principal
doctest.testmod()