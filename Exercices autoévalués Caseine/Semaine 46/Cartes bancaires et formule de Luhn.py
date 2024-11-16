# on importe les modules necessaires
import random
# definitions des fonctions

def listeSomme(li):
    """Calcule la somme d'elements de la liste li"""
    somme = 0
    for el in li:
        somme+=el
    return somme

def changeUnChiffre(chf):
    """Multiplie la chiffre chf par deux. Si chf*2>9 on soustrait 9"""
    res = 2*chf
    if res>9:
        res -= 9
    return res

def changeChiffres(li):
    """Modifie un chiffre sur deux, en commençant par l’avant dernier
    et en se déplaçant de droite à gauche"""
    res = list(li)
    l = len(li)
    for i in range(l-2, -1, -2):   # Commence à l'avant-dernier chiffre et avance de deux en deux
        res[i] = changeUnChiffre(res[i])
    return res

def resteDivSomme(li):
    """Reçoit une liste de chiffres (résultats de l’étape 1), 
    calcule leur somme (étape 2), la divise par 10 et renvoie le reste de cette division"""
    somme = listeSomme(li)
    return somme%10

def verifie_Luhn(num):
    """Prend en argument un numéro représenté par la liste de ses chiffres,
    et renvoie un booléen indiquant s’il vérifie la formule de Luhn."""
    num_modifie = changeChiffres(num)
    return resteDivSomme(num_modifie) == 0

def ajoute_chiffre_controle(num):
    """Prend en argument une liste de chiffres 
    et lui rajoute un chiffre de contrôle pour la rendre valide"""
    num.append(0)
    num_modifie = changeChiffres(num)
    reste = resteDivSomme(num_modifie)
    if reste!=0:
        chf_cont = (10 - reste)%10
        num[-1] = chf_cont

def  genere_numero(n):
    """Prend un entier positif en argument et renvoie un numéro valide de
    n décimales généré aléatoirement"""
    num = []
    for i in range(n-1):
        num.append(random.randint(0, 9))
    if n==0:
        res = []
    else:  # s'il y a au moins 1 element dans la liste
        ajoute_chiffre_controle(num)
        res = num
    return res



    
