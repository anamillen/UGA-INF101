# on importe les modules necesssaires
import doctest

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

def placerMines(grille, positionMines, avec_mine = '*'):
    """Place les mines sur la grille aux positions stockees dans positionMines"""
    for coord_pair in positionMines:
        ind_lin = coord_pair[0]
        ind_col = coord_pair[1]
        grille[ind_lin][ind_col] = avec_mine

def grillePourAffichage(dimensions, positionMines, avec_mine = "*", sans_mine = "-"):
    """Cree la grille qui est adaptee a l'affichage"""
    N_LINS = dimensions[0]
    N_COLS = dimensions[1]
    grille = creerGrille(N_LINS, N_COLS, sans_mine)
    placerMines(grille, positionMines, avec_mine)
    return grille

def testMine(grille, i, j, mine = 1):
    """Reçoit la grille des positions des mines, et 2 coordonnées
    i (numéro de ligne entre 0 et N-1) 
    et j (numéro de colonne entre 0 et M-1) ; 
    vérifie s’il y a une mine sur la case indiquée par ces coordonnées ; 
    et renvoie un booléen indiquant le résultat.
    Exemples :
    --------
    >>> grille0 = [
    ...     [1, 0, 0, 0],
    ...     [0, 0, 0, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> testMine(grille0,0,0)
    True

    >>> grille1 = [
    ...     [0, 0, 0, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> testMine(grille1,1,2)
    True
    >>> testMine(grille1,1,3)
    False
    
    
    """
    res = False
    if grille[i][j] == mine:
        res = True
    return res

def compteMinesVoisines(grille, i, j, mine = 1):
    """Reçoit la grille des positions des mines, 
    et 2 coordonnées i (ligne) et j (colonne) ; compte le nombre de mines sur les cases voisines ; 
    renvoie ce compteur.
    
    Exemples :
    >>> grille = [
    ...     [0, 1, 0, 0, 1, 0],
    ...     [0, 0, 1, 0, 0, 0],
    ...     [0, 0, 0, 1, 0, 1],
    ...     [1, 1, 0, 0, 0, 1],
    ...     [1, 1, 0, 0, 0, 1],
    ... ]

    >>> compteMinesVoisines(grille, 0, 0)
    1
    >>> compteMinesVoisines(grille, 1, 2)
    2
    >>> compteMinesVoisines(grille, 4, 5)
    1
    >>> compteMinesVoisines(grille, 3, 1)
    3
    >>> compteMinesVoisines(grille, 3, 2)
    3
    >>> compteMinesVoisines(grille, 0, 5)
    1
    >>> compteMinesVoisines(grille, 4, 5)
    1
    >>> compteMinesVoisines(grille, 2, 2)
    3
    """
    res = 0  # le decompteur de mines voisines
    res+= minesVoisinesLigne(grille, i, j, mine) + minesVoisinesCol(grille, i, j, mine)
    res+= minesVoisinesLigne(grille, i+1, j, mine)
    res+= minesVoisinesLigne(grille, i-1, j, mine)
    return res

def minesVoisinesLigne(grille, i, j, mine = 1):
    """Compte le nombre de mines voisines sur la même ligne

    Exemples :
    >>> grille = [
    ...     [1, 0, 0, 0],
    ...     [1, 0, 1, 1],
    ...     [1, 1, 0, 0],
    ... ]
    >>> minesVoisinesLigne(grille,0,0)
    0
    >>> minesVoisinesLigne(grille,1,0)
    0
    >>> minesVoisinesLigne(grille,1,2)
    1
    >>> minesVoisinesLigne(grille,2,0)
    1

    """
    res = 0
    if i in range (len(grille)) and j in range(len(grille[i])):
        long = len(grille[i])

        if j==0:            # si la mine initiale est à toute gauche de la ligne alors
            if testMine(grille, i, j+1, mine):
                res+=1
        elif j==long-1:     # si la mine initiale est à toute droite de la ligne alors
            if testMine(grille, i, j-1, mine):
                res+=1
        else:               # si la mine n'est pas aux bornes alors
            if testMine(grille, i, j+1, mine):
                res+=1
            if testMine(grille, i, j-1, mine):
                res+=1
    return res

def minesVoisinesCol(grille, i, j, mine = 1):
    """Compte le nombre de mines voisines sur la même colonne
    
    Exemples :
    >>> grille = [
    ...     [1, 0, 0, 0],
    ...     [1, 0, 1, 1],
    ...     [1, 0, 1, 0],
    ... ]
    >>> minesVoisinesCol(grille,0,0)
    1
    >>> minesVoisinesCol(grille,1,2)
    1
    >>> minesVoisinesCol(grille,1,3)
    0
    >>> minesVoisinesCol(grille,2,2)
    1
    """
    long = len(grille)
    res = 0
    if i in range(long) and j in range(len(grille[i])):
        if i==0:           # si la mine initiale est à la première colonne alors
            # si la case au-dessous de la courante a une mine alors
            if testMine(grille, i+1, j, mine):
                res+=1
        elif i==long-1:    # si la mine initiale est à la dernière colonne alors
            # si la case au-dessus de la courante a une mine alors
            if testMine(grille, i-1, j, mine):
                res+=1
        else:              # si la mine n'est pas aux bornes alors
            # on verifie la case au-dessus et la case au-dessous
            if testMine(grille, i+1, j, mine):
                res+=1
            if testMine(grille, i-1, j, mine):
                res+=1
    return res




# programme principal pour tester
doctest.testmod()
