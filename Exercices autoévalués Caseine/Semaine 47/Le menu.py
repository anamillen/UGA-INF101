# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


def prix_menu(menu, avecBoisson = False, nb_supplement = 0):
    """Renvoie le prix du menu choisi"""
    res = 0
    prix_basique = 9
    prix_gourmand = 15
    prix_complet = 19
    prix_boisson = 4
    prix_supp = 1.5
    
    if menu=="Basique":
        res+=prix_basique
    elif menu=="Gourmand":
        res+=prix_gourmand
    else:   # si le menu choisi est le menu Complet
        res+=prix_complet
    if avecBoisson:
        res+=prix_boisson
    res+= prix_supp*nb_supplement
    return res
    
def table_Dupont():
    bas = "Basique"
    gour = "Gourmand"
    comp = "Complet"
    p1 = prix_menu(bas)
    p2 = prix_menu(gour, True)
    p3 = prix_menu(bas, nb_supplement=2)
    p4 = prix_menu(bas, avecBoisson = True, nb_supplement=1)
    return p1+p2+p3+p4
        

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")




