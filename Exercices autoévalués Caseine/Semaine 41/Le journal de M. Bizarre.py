
# definitions des fonctions

def lundi(mot):
    """Prend en argument un mot et qui transforme ce mot selon la règle du lundi :
    le mot est repete 2 fois, separe par 1 espace"""
    return mot+" "+mot
    
def mardi(mot):
    """Prend en argument un mot et qui renvoie la chaîne de caractères suivant la règle du mardi :
    mots de long' paire sont repetes 6 fois, separes par tiret
    mots de lon'g impaire sont repetes 3 fois, separes par virgules
    """
    long = len(mot)
    res = ""
    if long%2==0:
        res = (mot+"-")*5+mot  # on modifie le resultat selon les regles du mardi
    else:  # si la longueur du mot est impaire alors
        res = (mot+",")*2+mot
    return res

def mercredi(mot):
    """Si le mot entree est de la longueur paire renvoie le mot rentree,
    sinon renvoie "impair"
    """
    long = len(mot)
    res = mot
    if long%2!=0:    # si la longueur est impaire
        res = "impair"
        
    return res
    
def jeudi(mot):
    """Le mot est repete autant de fois que leur longueur modulo 3, sans espace"""
    res = ""
    long = len(mot)
    n = long%3
    i = 0    # on initialise le decompteur pour conditionner la boucle while
    
    # tant que le mot n'est pas repete autant de fois qu'il faut on continue
    while i<n:
        res+=mot   # on modifie le resultat
        i+=1    # on increment le decompteur
    return res
    
def vendredi(mot):
    """Les mots sont ecrits normalement"""
    return mot
    
def transforme(mot, jour):
    """Prend en argument un mot et le numero du jour et 
    renvoie le mot transforme selon la regle du jour correspondant"""
    res = ""
    if jour == 1:
        res = lundi(mot)
    elif jour == 2:
        res = mardi(mot)
    elif jour ==3:
        res = mercredi(mot)
    elif jour == 4:
        res = jeudi(mot)
    else:
        res = vendredi(mot)
    return res
        
    
        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")

