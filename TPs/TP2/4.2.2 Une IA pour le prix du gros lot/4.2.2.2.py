from random import randint      # on importe de module random le methode randint 

# l'initialisation des constantes
MSG_INIT = "Je cherche un nombre entre"
MSG_PROPO = "Je propose "
MSG_GAGNE = "J’ai gagné"
MSG_ESS = "Le nombre d'essais est :"
TIRE = randint(1,100)


#l'initialisation des variables
rep = ""
inf=0
sup=100
n_ess = 0

# le programme essaye de deviner le nombre choisi jusqu'a la reussite
while rep!="b":
    print(MSG_INIT,inf,"et",sup)
    propo = randint(inf,sup)        # le programme choisi un nombre aleatoire entre les deux bornes
    print(MSG_PROPO,propo," ? ",end="")
    n_ess+=1            # on augmente le nombre d'essais
    if propo<TIRE:      # si le nombre devenu est plus petit que le nombre tire alors
        rep="p"
        print(rep)
        inf=propo+1    # l'echange de la borne inferieure
    elif propo>TIRE:    # si le nombre devenu est plus grande que le nombre tire alors
        rep="g"
        print(rep)
        sup=propo-1    # l'echange de la borne superieure
    else:               # si le nombre devenu est egal au nombre choisi alors
        rep="b"
        print(rep)
# quand on sort de la boucle rep="b", le programme a devine le nombre choisi par l'util
print(MSG_GAGNE)
print(MSG_ESS,n_ess)
