# definitions de fonctions

def testMine(grille, i, j, mine = 1):
    """Reçoit la grille des positions des mines, et 2 coordonnées
    i (numéro de ligne entre 0 et N-1) 
    et j (numéro de colonne entre 0 et M-1) ; 
    vérifie s’il y a une mine sur la case indiquée par ces coordonnées ; 
    et renvoie un booléen indiquant le résultat. Par exemple :
    testMine(0,2) renvoie True
    testMine(1,1) renvoie False"""
    res = False
    if grille[i][j] == mine:
        res = True
    return res

def compteMinesVoisines(grille, i, j):
    """Reçoit la grille des positions des mines, 
    et 2 coordonnées i et j ; compte le nombre de mines sur les cases voisines ; 
    renvoie ce compteur."""

    return 

def minesVoisinesLigne(ligne, i, mine = 1):
    """Compte le nombre de mines voisines sur la même ligne"""
    long = len(ligne)
    res = 0
    if long>1:
        if i==0:            # si la mine initiale est à toute gauche de la ligne alors
            if ligne[1]==mine:
                res+=1
        elif i==long-1:     # si la mine initiale est à toute droite de la ligne alors
            if ligne[long-2]==mine:
                res+=1
        else:               # si la mine n'est pas aux bornes alors
            if ligne[i-1]==mine:
                res+=1
            if ligne[i+1]==mine:
                res+=1
    return res

def minesVoisinesCol(grille, i, j, mine = 1):
    """Compte le nombre de mines voisines sur la même colonne"""
    long = len(grille)