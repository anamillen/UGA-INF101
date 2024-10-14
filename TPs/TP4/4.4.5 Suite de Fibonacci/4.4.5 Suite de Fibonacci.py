# on importe les modules necessaires
import doctest
import scipy.constants

# definitions de fonctions

def fibonacci(N):
    """Calcule n-ieme nombre de Fibonacci
    
    Exemples :
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(9)
    34
    """
    # definitions de variables
    f0 = 0; f1 = 1; i = 1

    # traitement de cas de base
    if N == 0:
        f = f0
    elif N == 1:
        f = f1
    
    # on calcule les termes de Fibonacci
    while i<N:
        f = f0+f1
        f1, f0 = f, f1
        i+=1
    # a partir d'ici i = N
    return f

def fibo_termes(n):
    """Affiche tous les termes de Fibonacci un par un jusqu’au n-ième
    Exemple :
    >>> fibo_termes(5)
    0
    1
    1
    2
    3
    5
    """
    i = 0
    # on affiche tous les nombres fibonacci jusqu'a nieme en utilisant
    # la fonction fibonacci(i)
    while i<=n:
        print(fibonacci(i))
        i+=1

def liste_de_termes(n):
    """Renvoie la liste des n premiers termes de la suite de Fibonacci
    Exemples :
    >>> liste_de_termes(5)
    [0, 1, 1, 2, 3, 5]
    >>> liste_de_termes(0)
    [0]
    """
    l = []; i = 0
    while i<=n:
        l+=[fibonacci(i)]
        i+=1
    return l

def nombre_d_or(N):
    """Renvoie la n-ième estimation du nombre d’or fn/f(n-1)
    
    Exemples :
    >>> nombre_d_or(2)
    1.0
    >>> nombre_d_or(6)
    1.6
    >>> nombre_d_or(10)
    1.6176470588235294
    """
    # definitions de variables
    f0 = 0; f1 = 1; i = 1
    
    # on calcule les termes de Fibonacci
    while i<N:
        f = f0+f1
        f1, f0 = f, f1
        i+=1
    # a partir d'ici i = N
    return float(f1/f0)

"""
def precision_ndor(eps):
    i = 2
    NDOR = scipy.constants.golden
    ndor_cur = nombre_d_or
    while NDOR-eps!=ndor_cur or NDOR+eps!=ndor_cur:

"""









# programme principal

doctest.testmod()