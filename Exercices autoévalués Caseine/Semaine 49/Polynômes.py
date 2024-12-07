# on importe les modules necessaires
import doctest

# definitions de fonctions
def evaluer(p, x):
    """Renvoie la valeur du polynôme p au point x
    
    Parametres :
    - p (dict) : un polynome
    - x (float) : un nombre reel

    Exemple :
    >>> evaluer({3:1, 1: 2, 0: -1}, 2)
    11
    """
    y = 0 
    for puissance in p:
        coeff = (p[puissance])
        y += x**(puissance) * coeff
        
    return y
    
def somme_polynomes(p1, p2):
    """Prend deux polynômes (dictionnaires) en arguments et renvoie un nouveau dictionnaire représentant la somme des deux polynômes p1 et p2.
    
    Exemple :
    >>> somme_polynomes({3:1, 2:1, 0:1}, {4:2, 2:3})
    {0: 1, 2: 4, 3: 1, 4: 2}
    >>> somme_polynomes({2:1, 1:1, 0:1}, {2:1, 1:-1, 0:1})
    {0: 2, 2: 2}
    """
    somme = dict(p1)
    for mnm in p2:
        if mnm in p1:
            if somme[mnm] + p2[mnm]!=0:
                somme[mnm] += p2[mnm]
            else:   # si la somme de 2 polynomes est nulle alors
                del somme[mnm]
                
        else: # si le monome n'est pas present dans le polynome 1 alors
            somme[mnm] = p2[mnm]
    return somme
            
def produit_polynomes(p1, p2):
    """Prend deux polynômes en argument et renvoie le produit des deux polynômes dans un nouveau dictionnaire.
    
    Exemple :
    >>> produit_polynomes({3:1, 2:1, 0:1}, {4:2, 2:3})
    {2: 3, 4: 5, 5: 3, 6: 2, 7: 2}
    """
    produit = {}
    for mnm2 in p2:
        for mnm1 in p1:
            mnm_prod = mnm1 + mnm2
            coeff_prod = p1[mnm1] * p2[mnm2]
            if mnm_prod in produit:
                produit[mnm_prod] += coeff_prod
            else : # si le monome n'est pas encore present
                produit[mnm_prod] = coeff_prod
    
    return produit

# programme principal
doctest.testmod()