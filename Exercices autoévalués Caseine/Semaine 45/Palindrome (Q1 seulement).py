def est_palindrome(mot):
    """Reçoit un mot (une chaîne de caractères), 
    détermine si ce mot est un palindrome, 
    et renvoie le résultat (un booléen)."""
    res = True
    for i in range(len(mot)):
        if mot[i]!=mot[-i-1]:
            res = False
    return res

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")



