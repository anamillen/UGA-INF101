# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


def liste_decroissante(n):
    """Prend en argument un entier n et renvoie la liste de tous les entiers de n à 0"""
    res = []
    for i in range(n,-1,-1):
        res.append(i)
    return res
    
def multiples(m, longueur):
    """Prend en argument un entier m et un entier longueur et
    renvoie une liste contenant les multiples de m,
    en commençant par 0, et dont la longueur est déterminée par l'argument longueur."""
    res = []
    for i in range(longueur):
        res.append(i*m)
    return res
    
def pairs(longueur):
    """Prend un argument longueur et renvoie une liste contenant les entiers pairs dans l'ordre croissant,
    en commençant par 0, et dont la longueur est donnée par l'argument longueur. """
    return multiples(2, longueur)


        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")




