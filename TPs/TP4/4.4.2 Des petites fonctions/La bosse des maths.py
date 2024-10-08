
# les definitions des fonctions

def valeur_abs(x):
    """Prend en argument un nombre x et renvoie sa valeur absolue
    
    >>> valeur_abs(0)
    0
    >>> valeur_abs(1)
    1
    >>> valeur_abs(-1)
    1
    """
    # comme la valeur absolue d'un nombre positif vaut bien ce nombre
    # on convertira que les x negatifs
    if x<0:     
        x = -x
    return x

def signe_different(x,y):
    """
    Prend en arguments 2 nombres x et y et renvoie True s’ils ont des signes différents, 
    False sinon (si l’un est égal à 0, la fonction renvoie False)

    >>> signe_different(0,1)
    False
    >>> signe_different(-1,1)
    True
    >>> signe_different(1,1)
    False
    """
    res = False         # on definie d'abord la valeur renvoyee par defaut
    # si x et y ont bien le signes differents alors on change la valeur renvoyee
    if (x>0 and y<0) or (x<0 and y>0):      
        res = True
    return res

def f(x):
    """Prend en argument un réel x et renvoie la valeur de f (x)
    
    >>> f(0)
    3
    >>> f(1)
    8
    >>> f(-1)
    4
    """
    # on definit les coefficients constants
    A = 3; B = 2; C = 3
    # on calcule f(x)
    y = A*x**2+B*x+C
    return y


# on importe le doctest pour tester les fonctions apres
import doctest
doctest.testmod()








