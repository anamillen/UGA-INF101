# on importe les modules importants
from math import sqrt
import doctest

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

def resolution(a,b,c):
    """
    Prend en arguments 3 réels a, b, c, qui résout le polynôme
    ax2 + bx + c, et qui affiche le nombre et la valeurs de ses racines.

    Exemples :
    >>> resolution(1, -3, 2)
    Les racines sont : 2.0 1.0
    Le nombre de racines est : 2
    >>> resolution(1, 2, 1)
    Les racines sont : -1.0 
    Le nombre de racines est : 1
    >>> resolution(1, 0, 1)
    Les racines sont :  
    Le nombre de racines est : 0
    """
    # on definit les constantes
    MSG_VAL = "Les racines sont :"
    MSG_N = "Le nombre de racines est :"
    # les valeurs initiales de racines
    x1 = ""; x2 = ""
    #on calcule le discriminant
    delta = b**2-4*a*c
    # on definit le nombre de racines par defaut
    n = 0

    if delta >0:    # si delta est strictement positive on a 2 racines. on les calcule
        x1 = (-b+sqrt(delta))/(2*a)
        x2 = (-b-sqrt(delta))/(2*a)
        n = 2
    elif delta==0:  # si delta == 0 on a 1 racine est on la calcule
        x1 = (-b)/(2*a)
        n = 1
    # l'affichage de valeurs et leur nombre
    print(MSG_VAL,x1,x2)
    print(MSG_N,n)


# on teste les fonctions avec doctest
doctest.testmod()

# programme principal

# l'input de l'util
MSG_INIT = "Entrez 3 reels a,b,c , coefficients de ax^2+bx+c"
print(MSG_INIT)
a = float(input())
b = float(input())
c = float(input())

# l'appel de la fonction
resolution(a,b,c)

    


















# on importe doctest pour tester les fonctions definies

import doctest
doctest.testmod()








