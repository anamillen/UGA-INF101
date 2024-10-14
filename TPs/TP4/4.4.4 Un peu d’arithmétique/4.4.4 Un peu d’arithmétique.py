
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
    

def pgcd_naif(a,b):
    """Renvoie le plus grand commun diviseur des entiers a et b.
    Le calcule en utilisant l'algorithme naif
    
    Exemples :
    >>> pgcd_naif(12, 8)
    4
    >>> pgcd_naif(17, 13)
    1
    >>> pgcd_naif(100, 25)
    25
    >>> pgcd_naif(48, 18)
    6
    >>> pgcd_naif(7, 1)
    1
    >>> pgcd_naif(0, 5)
    5
    >>> pgcd_naif(0, 0)
    0
    >>> pgcd_naif(3,0)
    3
    """

    # comme on peut pas diviser par zero, on verifie d'abord si a ou b
    # est egale a 0. si a = 0 ou b = 0 alors pcgd = nombre non-nul
    if a == 0:
        i = b 
    elif b == 0:
        i = a
    else:    # si a,b!=0 alors on procede au calcul du pgcd
        if a>b :  # on trouve le nombre plus grand pour diminuir le n de nos candidats
            a,b = b,a
        i = a
        while not (a%i==0 and b%i==0):   # on parcourt chaque  nombre <min(a,b) jusqu'a on a trouve pgcd
            i-=1
    return i

def pgcd(a,b):
    """Renvoie le plus grand commun diviseur des entiers a et b.
    Le calcule en utilisant l'algorithme d'Euclide
    
    Exemples :
    >>> pgcd(12, 8)
    4
    >>> pgcd(17, 13)
    1
    >>> pgcd(100, 25)
    25
    >>> pgcd(48, 18)
    6
    >>> pgcd(7, 1)
    1
    >>> pgcd(0, 5)
    5
    >>> pgcd(0, 0)
    0
    """
    # on implemente l'algorithme euclideen
    while b != 0:
        a, b = b, a % b
    return a

def ppcm(a,b):
    """
    Renvoie le plus petit commun multiple de a et b

    Exemples :
    >>> ppcm(24,12)
    24
    >>> ppcm(9,16)
    144
    >>> ppcm(7,3)
    21
    >>> ppcm(0,25)
    0
    >>> ppcm(35,5)
    35
    >>> ppcm(10,10)
    10
    """
    # on sait que ppcm  = a*b/pgcd(a,b)
    return int(a*b/pgcd(a,b))

def irreductible(num,den):
    """Calcule un booléen indiquant si la fraction 
    num/dem est irréductible ou non
    
    Exemples :
    >>> irreductible(5,3)
    True
    >>> irreductible(0,7)
    False
    >>> irreductible(14, 7)
    False
    >>> irreductible(5,10)
    False
    >>> irreductible(3,2)
    True
    >>> irreductible(2,1)
    True
    """
    # On vérifie si le PGCD du numérateur et du dénominateur est 1
    return pgcd(num, den) == 1




# programme principal
doctest.testmod()