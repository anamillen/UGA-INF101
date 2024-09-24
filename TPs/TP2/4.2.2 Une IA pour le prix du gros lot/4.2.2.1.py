from random import randint      # on importe de module random le methode randint 

# l'initialisation des constantes
MSG_INIT = "Je cherche un nbre entre"
MSG_PROPO = "Je propose "
MSG_GAGNE = "J’ai gagné"

#l'initialisation des variables
rep = ""
inf=0
sup=100

# le programme essaye de deviner le nombre choisi jusqu'a la reussite
while rep!="b":
    print(MSG_INIT,inf,"et",sup)
    propo = randint(inf,sup)        # le programme choisi un nombre aleatoire entre les deux bornes
    print(MSG_PROPO,propo," ? ",end="")
    rep = input()
    if rep=="p":
        inf=propo+1    # l'echange de la borne inferieure
    elif rep=="g":
        sup=propo-1    # l'echange de la borne superieure
# quand on sort de la boucle rep="b", le programme a devine le nombre choisi par l'util
print(MSG_GAGNE)
