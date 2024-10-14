
# definitions des fonctions
def maximum(a,b):
    """Renvoie le nombre plus grand entre a et b"""
    res = a
    if b>a:
        res = b
    return res
    
def maximum3(a,b,c):
    """Renvoie l'argument le plus grand"""
    res = a
    if b>a or c>a:
        if c>b:
            res = c
        else: # si b>=c
            res = b
    return res

def maximum3_input():
    """Demande l'utilisateur trois nombres et renvoie le maximum d'entre eux"""
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    return maximum3(a,b,c)


# Programme principal
if __name__=='__main__': # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
