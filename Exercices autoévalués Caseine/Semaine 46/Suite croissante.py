# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


def est_croissante(li):
    """Reçoit une liste d'entiers et renvoie un booléen indiquant si les éléments de cette liste sont dans l'ordre croissant (non strict). """
    drap = True
    if len(li)!=0:
        loc_max = li[0]
    else:    # si la liste li est vide alors
        loc_max = None
    
    for el in li:
        if el<loc_max:
            drap = False
        loc_max = el
    return drap
    
def est_decroissante(li):
    """Détermine si une liste reçue en paramètre est en ordre décroissant (non strict)."""
    drap = True
    if len(li)!=0:
        loc_min = li[0]
    else:    # si la liste li est vide alors
        loc_min = None

    for el in li:
        if el > loc_min:
            drap = False
        loc_min = el
    return drap
    
def est_en_desordre(li):
    """Détermine si une liste reçue en paramètre est dans le désordre
    (ni en ordre croissant, ni en ordre décroissant)"""
    return not (est_decroissante(li) or est_croissante(li))
        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en fai
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")




