# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


def decale(l,d):
    """Prend en argument une liste l et un nombre d et renvoie la liste 
    obtenue à partir de l en ajoutant un décalage de d à chaque élément de l"""
    res = []
    for el in l:
        res.append(el+d)
    return res
    
def intercale_zeros(l):
    """Prend en argument une liste l et renvoie la liste obtenue 
    à partir de l en intercalant un zéro après chaque élément de l."""
    res = []
    for el in l:
        res+=[el,0]
    return res
    
def supprime(l, elem):
    """Prend en argument une liste l et un élément elem et renvoie la liste obtenue
    à partir de l en supprimant toutes les occurrences de elem."""
    res = []
    for el in l:
        if el!=elem:
            res.append(el)
    return res
    
def insere_milieu(l, elem):
    """
    Prend en argument une liste l et un élément elem et renvoie la liste obtenue
    à partir de l en ajoutant elem "au milieu" de l, c'est-à-dire: 

    Si la longueur de l est paire, l'élément est ajouté une fois, au milieu de la liste.
    Si la longueur de l est impaire: l'élément est ajouté de part à d'autre de l'élément central.
    """
    long = len(l)
    mil = long//2
    
    res = []
    if long%2==0:
        res = list(l[:mil])+[elem]+list(l[mil:])
    else:    # si la longueur de la liste est impaire alors
        res = list(l[:mil])+[elem]+[l[mil]]+[elem]+list(l[mil+1:])
    return res
    
def decoupe(l, seuil):
    """Prend en argument une liste de nombres l et un nombre seuil et renvoie deux listes:
    la première est obtenue à partir de l en ne gardant que les nombres inférieurs ou égaux à seuil;
    la deuxième est obtenue à partir de l en ne gardant que les nombres strictement supérieurs à seuil.
    """
    l_inf = []
    l_sup = []
    for el in l:
        if el>seuil:
            l_sup.append(el)
        else:   # si el<=seuil alors
            l_inf.append(el)
    return l_inf, l_sup
    
        

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")


## Ci-dessous: copie des exemples
## Pour avoir l'enonce en entier, ouvrez deux fenetres cote-a-cote.
##decale([4, 17, 12], 3) vaut [7, 20, 15].
##intercale_zeros([4, 17, 12]) vaut [4, 0, 17, 0, 12, 0].
##supprime([4, 7, 12, 4, 4, 0, 4, 5], 4) vaut [7, 12, 0, 5].
##insere_milieu([4, 7, 12, 3], 0) vaut [4, 7, 0, 12, 3]
##et insere_milieu([9, 3, 5, 6, 2], 1) vaut [9, 3, 1, 5, 1, 6, 2].
##decoupe([14, 27, 12, 0, 40, 34, 20, 11], 20) a pour
##valeur de retour  [14, 12, 0, 20, 11] et [27, 40, 34].


