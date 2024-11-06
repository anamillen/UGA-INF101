# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.





# definitions de fonctions

def ch_a_lindice(mot, ch, i):
    """Renvoie True si le charactere ch est a l'indice i dans le mot mot. False sinon"""
    return mot[i]==ch


def est_voyelle(ch):
    """Verifie si un char est bien une voyelle"""
    voyelles = ['a','e','o','i','u','y']
    return ch in voyelles
    
def commence_par(ltr, mot):
    """Renvoie True si le mot commence par la lettre donnée en argument, False sinon"""
    return ch_a_lindice(mot, ltr, 0)

def contient_voyelle(mot):
    """Prend en argument un mot et renvoie True si le mot contient une voyelle, False sinon."""
    voyelles = ['a','e','o','i','u','y']
    res = False
    long = len(mot); i =0
    while not res and i<long:
        if est_voyelle(mot[i]): 
            res = True
        i+=1
    # a partir d'ici soit res==True soit i<long
    return res
    
def derniere_consonne(mot):
    """Prend en argument un mot et renvoie deux valeurs de retour: l'indice de sa dernière consonne ainsi que
    la dernière consonne."""
    res = ""; ind = 0
    
    for i in range(len(mot)):
        if not est_voyelle(mot[i]): 
            res=mot[i]
            ind = i
    return ind, res
        
def double_consonne(mot):
    """Prend en argument un mot et a deux valeurs de retour: 
    - un booléen valant True si le mot contient une double consonne (deux fois la même consonne à la suite), 
    et dans ce cas la deuxième valeur de retour est la consonne qui est doublée ; 
    s'il n'y a pas de consonne doublée, la fonction renvoie False et None."""
    res = False
    consonne_doublee = None
    long = len(mot)
    for i in range(long):
        if not est_voyelle(mot[i]):
            if i<long-1 and mot[i]==mot[i+1]: 
                res = True
                consonne_doublee = mot[i]
    return res, consonne_doublee
    
def envers(li):
    """Prend en argument une liste li (attention, pas un mot, contrairement aux autres fonctions de cet exercice) 
    et renvoie une liste obtenue à partir de li en inversant l'ordre des éléments."""
    res = []
    for i in range(len(li)):
        res.append(li[-i-1])
    return res
    
def palindrome(mot):
    """Prend en argument un mot et renvoie un booléen indiquant si le mot est un palindrome. """
    res = True
    for i in range(len(mot)//2):
        if mot[i]!=mot[-i-1]: res = False
    return res
    
def mot_autorise(mot, liste):
    """Prend en argument un mot et une liste de mots interdits, 
    et renvoie True si le mot est autorisé, 
    et False si le mot est interdit."""
    return not mot in liste
        





        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    
    # Exemple de transformation d'un mot en liste
    mot="bonjour"
    test=list(mot)
    print(test)
    