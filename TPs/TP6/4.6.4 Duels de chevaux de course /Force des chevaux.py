# definitions de fonctions

def plus_proches(li):
    """Etant donnée une liste des forces, 
    identifie les forces les plus proches et 
    renvoie la différence entre ces deux forces 
    (entier positif ou nul).
    
    Exemples :
    >>> plus_proches([2,3,15])
    1
    >>> plus_proches([34,23,12,12])
    0
    >>> plus_proches([12,13,145])
    1
    >>> plus_proches([28,24,22])
    2
    """
    min_diff = float("inf")
    for el0 in li:
        for el1 in li:
            diff = abs(el0 - el1)
            if diff < min_diff:
                min_diff = diff
    return min_diff


def plus_proches_avancee(li):
    """Etant donnée une liste des forces, 
    identifie les forces les plus proches et 
    renvoie la différence entre ces deux forces 
    (entier positif ou nul).
    Renvoie non seulement la différence de force 
    mais aussi les numéros des 2 chevaux concernés
    
    Exemples :
    >>> plus_proches()
    >>> plus_proches()
    >>> plus_proches()
    >>> plus_proches()
    """
    min_diff = float("inf"); long = len(li)
    chev1, chev2 = li[0], li[1]
    for j in long:
        for i in long:
            diff = abs(li[j] - li[i])
            if diff < min_diff:
                min_diff = diff
                chev1 = j
                chev2 = i      
    return min_diff, chev1, chev2



