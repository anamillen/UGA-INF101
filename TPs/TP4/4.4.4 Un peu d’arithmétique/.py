
# on importe le smodules necessaires
import doctest

# definitions de fonctions

def est_premier(N):
    """
    Verifie si N est un premier

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
    True
    """
    i = N
    res = True

    # on examine tous les diviseurs possibles
    while i>1:
        if N%i==0 and i!=N:  # s'il existe 1 diviseur de n different de 1 alors
            res = False
            i = 0 # on quitte la boucle, comme on a trouve au moins 1 diviseur
        i-=1    # on diminuit la valeur du decompteur
    return res



# programme principal
doctest.testmod()