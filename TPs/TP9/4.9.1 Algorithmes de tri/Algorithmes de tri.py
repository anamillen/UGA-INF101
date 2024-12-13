# on importe les modules necessaires
import doctest

def tri_insertion(li, descending = False):
    """Effectue la tri par insertion 

    Parametres :
    - li (list) : liste d'entiers a trier
    - descending (bool, optional) : si est egal a True, la liste sera triee
    en ordre decroissant, sinon en ordre croissant (par defaut)

    Renvoie : 
    - li_triee (list) : copie triee de la liste li

    Exemples :
    >>> li = [3,2,1]
    >>> tri_insertion(li)
    [1, 2, 3]

    >>> li = [3,7,45,23,-1,0,100,1,3,2,1]
    >>> tri_insertion(li)
    [-1, 0, 1, 1, 2, 3, 3, 7, 23, 45, 100]

    >>> li = [3,4,9,2,1]
    >>> tri_insertion(li, descending = True)
    [9, 4, 3, 2, 1]
    """
    li_triee = []
    for el in li:       # on parcourt chaque element de la liste initiale
        curr_ind = 0
        if len(li_triee)!=0:
            if not descending:
                while curr_ind<len(li_triee) and el>=li_triee[curr_ind]:
                    curr_ind+=1
                # a partir d'ici soit el>li_triee[curr_ind] soit curr_ind>=len(li_triee)
                # c.a.d. l'element courant choisi de la liste originale li est superieur a 
                # l'element a l'indice curr_ind, donc peut etre insere
            else: # si la liste doit etre triee en ordre decroissant alors
                while curr_ind<len(li_triee) and el<=li_triee[curr_ind]:
                    curr_ind+=1
            li_triee.insert(curr_ind, el)
        else:   # si la liste triee est vide alors
            li_triee.append(li[curr_ind])
    return li_triee
'''


def tri_selection(li, descending = False):
    """Effectue la tri par selection en ordre croissant

    Parametres :
    - li (list) : liste d'entiers a trier
    - descending (bool, optional) : si est egal a True, la liste sera triee
    en ordre decroissant, sinon en ordre croissant (par defaut)

    Renvoie : 
    - None

    Effets de bord :
    - Modifie la liste li en le triant

    Exemples :
    >>> li = [3,2,1]
    >>> tri_selection(li)
    >>> li 
    [1, 2, 3]

    >>> li = [3,7,45,23,-1,0,100,1,3,2,1]
    >>> tri_selection(li)
    >>> li 
    [-1, 0, 1, 1, 2, 3, 3, 7, 23, 45, 100]

    >>> li = [3,4,9,2,1]
    >>> tri_selection(li, descending = True)
    >>> li 
    [9, 4, 3, 2, 1]
    """
    loc_min_ind = minim_ind(li)
    li[loc_min_ind+1], li[curr_ind] = li[curr_ind], li[loc_min_ind+1]
    while loc_min_ind<len(li)-1:
        li[loc_min_ind+1], li[curr_ind] = li[curr_ind], li[loc_min_ind+1]
        curr_ind = min_greater_than(li, li[loc_min_ind])
        li[loc_min_ind+1], li[curr_ind] = li[curr_ind], li[loc_min_ind+1]
        loc_min_ind+=1
    
    


def min_greater_than(li, lim):
    """Calcule et renvoie l'indice de l'element le plus petit de liste li
    plus grand que lim
    
    Exemples :
    >>> min_greater_than([5, 3, 8, 10], 6)
    2
    >>> min_greater_than([7, 15, 3, 12], 10)
    1
    
    """
    i_res = 
    for ind in range(len(li)):
        if li[ind]>lim and li[ind]<li[i_res]:
            i_res = ind
            loc_lim = li[i_res]
    return i_res


def minim_ind(li):
    """
    Calcule et renvoie l'indice du minimum de la liste 

    Parametres :
    - li (list) : liste de nombres

    Renvoie :
    - res (int) : l'indice d nombre le plus petit de la liste nonvide li
    si la liste est vide, renvoie None
    """
    res_ind = 0
    if len(li)>0:
        res = li[0]
        for ind in range(len(li)):
            if li[ind]<res:
                res = li[ind]
                res_ind = ind
    else :   # si la liste li est vide alors
        res_ind = None
    return res_ind

'''


# tester
doctest.testmod()