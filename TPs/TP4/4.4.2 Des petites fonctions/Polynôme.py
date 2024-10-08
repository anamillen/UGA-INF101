# on definit les fonctions
def nb_racines(a,b,c):
    """
    Prend en argument trois réels a, b, c et qui renvoie le nombre
    de racines réelles du polynôme ax^2 + bx + c
    >>> nb_racines(4,4,1)
    1
    >>> nb_racines(1,1,1)
    0
    >>> nb_racines(2,3,-4)
    2

    """
    # on definit le nombre de racines par defaut
    n = 2
    # on calcule le discriminant
    delta = b**2-4*a*c

    if delta<0: # on verifie si les solutions existent ou non
        n = 0
    elif delta == 0:        # si solutions existent on verifie si delta est egal au 0
        n=1

    
    return n

















# on importe doctest pour tester les fonctions definies

import doctest
doctest.testmod()








