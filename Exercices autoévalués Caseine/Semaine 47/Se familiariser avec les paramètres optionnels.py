# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

# definitions de fonctions

def moyenne(n1,n2,bonus = 0):
    """Renvoie la moyenne de l'étudiant calculée ainsi: d'abord,
    on calcule la moyenne "normale" entre les deux notes, puis on ajoute le bonus."""
    res = (n1+n2)/2
    if res+bonus<=20:
        res+=bonus
    else:   # si le resultat + bonus depasse 20, alors on met juste 20 comme la moyenne
        res = 20
    return res
    
def points_manche(pourcentage, n_points, multip = 1):
    """Calcule le nombre de points en jeu
    """
    res = int(round(pourcentage*n_points/100, 0))
    res*=multip
    return res

def division_arrondi(nom, denom, arrondi = False, decimales = 0):
    """"""
    MSG_ERR = "Impossible de diviser par 0"
    res = None
    if denom==0:
        print(MSG_ERR)
    else:  # si le denominateur n'est pas egal a zero alors
        res = nom/denom
        if arrondi:
            res = round(res, decimales)
    return res

        

        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")


