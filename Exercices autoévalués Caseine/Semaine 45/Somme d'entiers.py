# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.



# definitions de fonctions

def somme(n):
    """Renvoie la somme des n premiers entiers en partant de 1"""
    res = 0
    for ch in range(1, n+1):
        res+=ch
    return res
    
def somme_impairs(n):
    """Renvoie la somme des n premiers entiers impairs """
    res = 0
    for ch in range(0, n):
        res+=2*ch+1
    return res
    
def somme_carres(n):
    """Renvoie la somme des n premiers carres (en partant de 1) """
    res = 0
    i = 1
    for ch in range(1, n+1):
        res+=ch*ch
    return res
    
    
    
    
        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")




