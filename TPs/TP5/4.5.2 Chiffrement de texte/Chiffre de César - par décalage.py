# on importe des modules necessaires
import doctest

# definitions de fonctions
def decalage(ltr, DECAL):
    """Decale une lettre par DECAL lettres

    Exemples :
    >>> decalage("A",4)
    'E'
    >>> decalage("Z",1)
    'A'
    """
    # definitions de constantes et variables
    PREMIER = ord("A")-1; DERNIER = ord("Z")
    ordre = ord(ltr) 
    nov_ordre = ord(ltr)+DECAL    # on calcule le nouveau index 
    # si lettre indexee depasse "Z" alors on revient au debut de l'alphabet
    if nov_ordre>DERNIER:
        nov_ordre = nov_ordre+PREMIER-DERNIER
    return chr(nov_ordre)

def chiffre_de_cesar(mot, DECAL):
    """
    Reçoit un mot en majuscules, et le renvoie chiffré en décalant chaque lettre
    de 3 positions (le ’A’ devient ’D’, le ’B’ devient ’E’, le ’Z’ devient ’C’, etc).
    
    Exemples :
    >>> chiffre_de_cesar('PYTHON',3)
    'SBWKRQ'
    >>> chiffre_de_cesar("A",3)
    'D'
    >>> chiffre_de_cesar("XYZ",3)
    'ABC'
    """
    # definitions de constantes et variables
    res = ""
    # on parcourt toutes les lettres de notre mot
    for ltr in mot:
        if ltr.isalpha():
            res+=decalage(ltr,DECAL)
        else:    # si le caractere est bien une signe de ponctiation alors
            res+=ltr
    return res

def texte_chiffre(texte):
    """Chiffre un texte complet en utilisant le Chiffre de Cesar
    
    Exemples :
    >>> texte_chiffre("NO, IT WAS WRITTEN IN CIPHER")
    'QR, LW ZDV ZULWWHQ LQ FLSKHU'
    >>> texte_chiffre("HI!!!")
    'KL!!!'
    """
    res = ""
    DECAL = 3
    i = 0     # le drapeau pour detecter le premier mot du texte et 
    # chager l'affichage
    # on parcourt chaque mot dans notre txt
    for mot in texte.split():   
        if i!=0:  
            res+=" "+chiffre_de_cesar(mot, DECAL)
        else: # ici on evite l'espace innecessaire apres le dernier mot
            res+=chiffre_de_cesar(mot, DECAL)
            i = 1     # on cnahge la valeur du drapeau pour continuer en affichant des mots de maniere necessaire
    return res

        

# programme principal
doctest.testmod()