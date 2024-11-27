# om importe les modules necessaires
import calculs




def afficheSolution(dimensions, positionMines, avec_mine = "*", sans_mine = "-"):
    """Reçoit en paramètre 
    - une liste positionsMines (grille d’entiers indiquant les positions des mines),
    - dimensions de la grille (un pair)
    - parametres optionnels : la valeur de mine, style de l'affichage de cases sans et avec mines
    Affiche cette grille sous la forme d’un rectangle de caractères représentant la solution du démineur,
    c’est-à-dire dévoilant les positions des mines.
    On choisit d’afficher avec un ’-’ (tiret) les cases non minées (valeur 0),
    et avec une ’*’ (étoile) les cases minées (valeur mine)."""
    N_LINS = dimensions[0]
    N_COLS = dimensions[1]
    for ind_lin in range(N_LINS):
        for ind_col in range(N_COLS):
            if [ind_lin, ind_col] in positionMines:
                print(avec_mine, end="")
            else:  # si la case n'est pas une case avec une mine alors
                print(sans_mine, end="")
        print()
    print()

def afficheJeu(dimensions, positionMines, casesDevoilees, non_decouvert = "?", avec_mine = "*"):
    """
    Reçoit en paramètre :
    dimensions : un 2uplet, dimensions de la grille a afficher (N_LIGNES, N_COLS)
    positionMines : une liste 2d, grille d’entiers indiquant les positions des mines
    casesDevoilees : une liste, grille de booléens indiquant les cases dévoilées
    """
    N_LINS = dimensions[0]
    N_COLS = dimensions[1]
    for ind_lin in range(N_LINS):
        for ind_col in range(N_COLS):
            if [ind_lin, ind_col] not in casesDevoilees:
                print(non_decouvert, end=" ")
            else:   # si la case courante a deja ete devoilee alors
                if [ind_lin, ind_col] in positionMines:
                    print(avec_mine, end=" ")
                else:   # si la case courante ne contient pas une mine alors

                    """Completer avec un algorithme qui affichera le nombre 
                    de mines voisines de cette case"""
                    
                    print()
        print()
    print()

    return
    
    



# programme principal pour tester
dims = (4,4)
mines = [[0,0], [2,3], [1,0], [0,3]]
afficheSolution(dims,mines)

dims = (8,8)
mines = [[0,0], [2,3], [1,0], [0,3], [7,7], [4,4], [6,2]]
afficheSolution(dims,mines)