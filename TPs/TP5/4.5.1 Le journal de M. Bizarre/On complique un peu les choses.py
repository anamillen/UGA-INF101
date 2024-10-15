# on importe les modules necessaires
import doctest


# definitions des fonctions
def lundi(mot):
    """Prend en argument un mot et qui transforme ce mot selon la règle du lundi :
    le mot est repete 2 fois, separe par 1 espace"""
    return mot+" "+mot
    
def mardi(mot):
    """Prend en argument un mot et qui renvoie la chaîne de caractères suivant la règle du mardi :
    mots de long' paire sont repetes 6 fois, separes par tiret
    mots de lon'g impaire sont repetes 3 fois, separes par virgules
    
    Exemples :
    >>> mardi("ho")
    'ho-ho-ho-ho-ho-ho'
    >>> mardi("non")
    'non,non,non'
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
    
    Exemples :
    >>> mercredi("chat")
    'chat'
    >>> mercredi("cat")
    'impair'
    """
    long = len(mot)
    res = mot
    if long%2!=0:    # si la longueur est impaire
        res = "impair"
        
    return res
    
def jeudi(mot):
    """Le mot est repete autant de fois que leur longueur modulo 3, sans espace
    
    Exemples :
    >>> jeudi("bonbon")
    ''
    >>> jeudi("comment")
    'comment'
    >>> jeudi("merci")
    'mercimerci'
    """
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
    """Les mots commençant par une majuscule sont privés de leur dernière lettre ; les autres
    sont privés de leur première lettre.
    
    Exemples :
    >>> vendredi("Hello")
    'Hell'
    >>> vendredi("hello")
    'ello'
    """
    if mot[0].isupper():  # si le mot commence par une mahuscule alors
        res = mot[:len(mot)-1]
    else:    # si le mot commence par une minuscule alors
        res = mot[1:]
    return res

def samedi(mot):
    """Renvoie le mot écrit à l’envers
    
    Exemples :
    >>> samedi("SOS")
    'SOS'
    >>> samedi("bonjour")
    'ruojnob'
    """
    res = ""
    # on ajoute chaque lettre une par une au resultat
    for ltr in mot:     
        res = ltr+res
    return res

def dimanche(mot):
    """Transforme le mot en ajoutant un espace entre chaque lettre
    
    Exemples :
    >>> dimanche("hello")
    'h e l l o'
    >>> dimanche("bye")
    'b y e'
    """
    return " ".join(mot)

    


def transforme(mot, jour):
    """Prend en argument un mot et le numero du jour et 
    renvoie le mot transforme selon la regle du jour correspondant
    
    Exemples :
    >>> transforme("bonjour", 5)
    'onjour'
    >>> transforme("merci", 1)
    'merci merci'
    """
    res = ""
    if jour == 1:
        res = lundi(mot)
    elif jour == 2:
        res = mardi(mot)
    elif jour ==3:
        res = mercredi(mot)
    elif jour == 4:
        res = jeudi(mot)
    elif jour == 5:
        res = vendredi(mot)
    elif jour == 6:
        res = samedi(mot)
    else:
        res = dimanche(mot)
    return res
        

# programme principal
doctest.testmod()


# definitions de messages
MSG_INIT = "Bonjour !"
MSG_MOT = "Entrez votre mot : "
MSG_JOUR = "Entrez le jour voulu : "
MSG_END = "La phrase obtenue est :"

print(MSG_INIT)
mot = input(MSG_MOT)
jour = int(input(MSG_JOUR))
print(MSG_END, transforme(mot,jour))




