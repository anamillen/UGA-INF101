# on importe les modules necessaires
import doctest

# definitions de fonctions

def pos_alphabet(ltr):
    """Reçoit une lettre (majuscule ou minuscule) et
    renvoie sa position dans l’alphabet

    Exemples :
    >>> pos_alphabet("A")
    1
    >>> pos_alphabet("a")
    1
    >>> pos_alphabet("d")
    4
    """
    # definitions de constantes et de variables
    PREM_MINU = ord('a')-1; PREM_MAJU = ord('A')-1
    i_ltr = ord(ltr)

    if ltr.islower():    # si la lettre est minuscule alors
        pos = i_ltr-PREM_MINU
    else:                # si la lettre est majuscule alors
        pos = i_ltr-PREM_MAJU
    return pos

def chiffre_numerique(mot):
    """Reçoit un mot (contenant des majuscules et des minuscules) et renvoie ce mot chiffré
    en remplaçant chaque lettre par sa position dans l’alphabet. Les nombres doivent
    être séparées par des +.
    
    Exemples :
    >>> chiffre_numerique("bonjour")
    '2+15+14+10+15+21+18'
    >>> chiffre_numerique('abcd')
    '1+2+3+4'
    """
    # definitions de constantes et variables
    res=""; i = 0

    # on parcourt chaque lettre du mot
    for ltr in mot:
        if ltr.isalpha() and ltr!=" ":   
            pos = pos_alphabet(ltr)
            if i!=0:
                res+="+"+str(pos)
            else:  # on evite le plus innecessaire devant le premier mot
                i=1    # on canhge la valeur de notre flag pour indiquer 
                res+=str(pos)
        else: # si le caractere n'est pas une lettre de l'alphabet
            res+=ltr
    return res

def chiffre_texte(txt): 
    """Reçoit un texte (qu’on suppose non accentué) et qui renvoie ce texte codé
    comme précédemment. Les espaces et autres ponctuations dans le texte ne sont pas modifiés.
    
    Exemple :
    >>> chiffre_texte("bonjour a tous !")
    '2+15+14+10+15+21+18 1 20+15+21+19 !'
    """
    res=""; i = 0
    for mot in txt.split():
        if i!=0:
            res+=" "+chiffre_numerique(mot)
        else:       # si le drapeau i ==1
            i = 1
            res+=chiffre_numerique(mot)
    return res
        






# programme principal    
doctest.testmod()

MSG_CHOIX = "Quel chiffre voulez-vous utiliser ?"
MCG_OPT = "(tapez a pour le chiffre de Cesar et b pour le chiffre numerique)"