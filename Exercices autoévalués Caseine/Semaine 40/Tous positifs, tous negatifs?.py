
"""
Ecrire un programme qui demande à l'utilisateur plusieurs nombres 
successivement en affichant "Nombre ?" jusqu'à ce que l'utilisateur 
entre le nombre 0. Le programme doit alors afficher "Tous -", 
ou "Tous +", ou "Seulement 0", ou "Ni tous +, ni tous -" selon que
 l'utilisateur n'a rentré que des nombres négatifs, ou bien que 
 des nombres positifs, ou bien seulement zéro, ou bien aucun 
 des cas précédents. Dans ce dernier cas (Ni tous +, ni tous -),
le programme doit afficher "Somme -", ou "Somme=0", ou "Somme +"
selon que la somme totale des nombres donnés par l'utilisateur 
est strictement négative, nulle ou strictement positive.
"""




# initialisation des constantes pour les messages d'affichage
INIT = "Nombre ? "
QUE_0 = "Seulement 0"
POS = "Tous +"
NEG = "Tous -"
NI_NI = "Ni tous +, ni tous -."
SOM = "La somme"

# demander à l'utilisateur un premier nombre
nmbr = float(input(INIT))

# initialisation des variables pour la somme absolue et la somme totale
somme_abs = 0
somme = 0

# boucle pour continuer à demander des nombres tant que l'utilisateur n'entre pas 0
while nmbr != 0:
    # mise à jour de la somme absolue et de la somme totale
    somme_abs += abs(nmbr)
    somme += nmbr
    
    # demander un nouveau nombre
    nmbr = float(input(INIT))

# vérifier si tous les nombres sont zéro
if somme_abs == 0:
    print(QUE_0)
# vérifier si tous les nombres sont positifs
elif somme == somme_abs:
    print(POS)
# vérifier si tous les nombres sont négatifs
elif somme == -somme_abs:
    print(NEG)
# cas où il y a un mélange de nombres positifs et négatifs
else:
    print(NI_NI)
    print(SOM, end=" ")
    
    # afficher le signe de la somme totale
    if somme > 0:
        print("+")
    elif somme < 0:
        print("-")
    else:
        print("0")