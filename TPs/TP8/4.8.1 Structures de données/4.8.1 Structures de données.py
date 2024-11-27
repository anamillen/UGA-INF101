# on importe les modules necessaires
from random import randint


# definitions de fonctions

def creerGrille(N,M, v = 0):
    """Reçoit en paramètres les entiers N et M, et un paramètre optionnel v (par défaut 0) 
    représentant la valeur d’initialisation de toutes les cellules ; 
    crée une grille à N lignes et M colonnes (donc une liste de N listes de M entiers), 
    ne contenant que des valeurs v (0 par défaut) ; et renvoie cette liste."""
    ligne = [0]*M
    grille = []
    for _ in range(N):
        grille.append(list(ligne))
    return grille

def placerMines(grille, X, mine = 1):
    """Reçoit en paramètre une grille de démineur et un entier X ;
    modifie cette liste pour y placer X mines (valeur 1) à des positions au hasard ;
    ne renvoie rien"""
    N = len(grille)
    M = len(grille[0])
    for _ in range(X):
        line = randint(0,N-1)
        col = randint(0, M-1)
        while grille[line][col]==mine:
            line = randint(0,N-1)
            col = randint(0,M-1)
        # a partir d'ici la case choisie n'a pas de mine 
        grille[line][col]=mine

# programme principal pour tester

N = int(input("Numero de lignes : "))
M = int(input("Numero de colonnes : "))
X = int(input("Numero de mines à placer : "))

grille = creerGrille(N,M)
placerMines(grille, X)
print(grille)



