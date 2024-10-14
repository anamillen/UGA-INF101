
# on importe le smodules necessaires
import doctest

# definitions de fonctions

def est_premier(N):
    """Verifie si N est un premier

    Exemples :
    >>> est_premier(7)
    True
    >>> est_premier(1)
    False
    >>> est_premier(2)
    True
    >>> est_premier(4)
    False
    >>> est_premier(6)
    False
    >>> est_premier(0)
    False
    """
    i = N
    res = True

    if N <= 1:
        res = False

    # on examine tous les diviseurs possibles
    while i>1:
        if N%i==0 and i!=N:  # s'il existe 1 diviseur de n different de 1 alors
            res = False
            i = 0 # on quitte la boucle, comme on a trouve au moins 1 diviseur
        i-=1    # on diminuit la valeur du decompteur
    return res


def plus_grand_diviseur_premier(n):
    """Renvoie le plus grand diviseur premier de l’entier n, s'il
    n'y a aucun, renvoie -1
    
    Exemples :
    >>> plus_grand_diviseur_premier(21)
    7
    >>> plus_grand_diviseur_premier(1)
    -1
    >>> plus_grand_diviseur_premier(2)
    2
    >>> plus_grand_diviseur_premier(30)
    5
    >>> plus_grand_diviseur_premier(16)
    2
    >>> plus_grand_diviseur_premier(0)
    -1
    """
    i = n
    res = -1

    # on parcourt chaque diviseur possible et verifie s'il est premier
    while i>0:
        if n%i==0 and est_premier(i):
            res = i
            i = 0
        i-=1
    return res
    


# programme principal
doctest.testmod()

