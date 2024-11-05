# definitions de fonctions
def moyenne(li):
    """Renvoie la moyenne d'une liste"""
    long = len(li)
    res = 0
    for el in li:
        res+=el
    res = res/long
    return res



# programme principal

# definitions de constantes and variables
MSG = "Votre nombre ? "
liste = []
print("Entrez des nombres strictement positifs (pour terminer tapez 0) :")
nb = float(input(MSG))
while nb!=0:
    liste.append(nb)
    nb = float(input(MSG))
    
print(liste)
print(moyenne(liste))