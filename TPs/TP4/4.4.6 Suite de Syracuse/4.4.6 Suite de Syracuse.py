# import des modules necessaires
import doctest

# definitions de fonctions
def u_pair(u):
    """Calcule u(n+1) pour la suite de Syracuse a partir d'un u(n) pair
    
    Exemples :
    >>> u_pair(16)
    8
    >>> u_pair(56)
    28
    """
    u = u/2
    return int(u)

def u_impair(u):
    """Calcule u(n+1) pour la suite de Syracuse a partir d'un u(n) impair
    Exemples :
    >>> u_impair(3)
    10
    >>> u_impair(5)
    16
    """
    u = 3*u+1
    return u

def suite_de_syracuse(A):
    """Calcule la durée de vol pour atteindre 1 à partir d’un A donné en paramètre
    Exemples:
    >>> suite_de_syracuse(6)
    8
    >>> suite_de_syracuse(3)
    7
    >>> suite_de_syracuse(19)
    20
    >>> suite_de_syracuse(1)
    0
    """
    i = 0
    u_cur = A

    while u_cur!=1:
        if u_cur%2==0:
            u_cur = u_pair(u_cur)
        else:
            u_cur = u_impair(u_cur)
        i+=1
    return i
    
def util_input():
    """Demande A pour la suite de Syracuse à l’utilisateur et affiche la durée de vol"""
    # definitions de messages
    MSG_INIT = "Entrez votre entier A : "
    MSG_AFFICHE = "\nLa duree de vol est egale a :"
    
    # l'appel a l'utilisateur
    a = int(input(MSG_INIT))

    # l'affichage
    print(MSG_AFFICHE, suite_de_syracuse(a))

def rejouer():
    """Redemande une valeur de A jusqu’à ce que l’utilisateur refuse de
    rejouer"""
    # definitions de messages
    MSG_INIT = "Bonjour ! Voulez-vous calculer la duree de vol ?"
    MSG_INST = '(tapez "o" pour commencer ou n\'importe quelle autre touche pour quitter) '
    MSG_REINIT = "Voulez-vous recommencer ?"
    MSG_QUIT = "Au revoir !"

    # l'algorithme principal
    print(MSG_INIT)
    ans = input(MSG_INST)
    while ans == "o":
        util_input()
        print(MSG_REINIT)
        ans = input(MSG_INST)
    print(MSG_QUIT)

def syracuse_pour_une_suite(X):
    """Affiche les durées de vol pour chaque valeur de A entre 1 et une borne X reçue en paramètre"""
    MSG_A = "A ="
    MSG = "La duree ="
    i = 1
    # on parcourt en boucle tous les entiers entre 1 et X
    while i<=X:
        print(MSG_A,i,end = " ")
        print(MSG,suite_de_syracuse(i))
        i+=1

def longuest_suite(X):
    """Calcule la longueur de la plus longue suite décroissante de termes"""
    l_max = 0
    while i<=X:
        l = suite_de_syracuse(i)
        if l>l_max:
            l_max = l
        i+=1
    return l_max

# programme principal
doctest.testmod()

x = int(input())
syracuse_pour_une_suite(x)