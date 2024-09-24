from random import randint      # on importe de module random le methode randint 

# l'initialisation des constantes
MSG_INIT = "Je cherche un nombre entre"
MSG_PROPO = "Je propose "
MSG_GAGNE = "J’ai gagné"
MSG_ESS = "Le nombre d'essais est :"
MSG_PAR = "Combien de parties voulez-vous jouer ? "
MSG_MYN_ESS = "La moyenne d'essais est :"


#l'initialisation des variables
rep = ""
inf=0
sup=100
n_ess = 0
n_ess_tot =0

# on demande l'utilisateur d'entrer le nombre de parties qu'il veut jouer
N_PARTIES = int(input(MSG_PAR))
n_parties = N_PARTIES


while n_parties>0: # tandis que le decompteur de parties voulues est > 0 alors
    tire = randint(1,100)
    # le programme essaye de deviner le nombre choisi jusqu'a la reussite
    while rep!="b":
        print(MSG_INIT,inf,"et",sup)
        propo = inf+(sup-inf)//2        # le programme choisi un nombre aleatoire entre les deux bornes
        print(MSG_PROPO,propo," ? ",end="")
        n_ess+=1            # on augmente le nombre d'essais
        if propo<tire:      # si le nombre devenu est plus petit que le nombre tire alors
            rep="p"
            print(rep)
            inf=propo+1    # l'echange de la borne inferieure
        elif propo>tire:    # si le nombre devenu est plus grande que le nombre tire alors
            rep="g"
            print(rep)
            sup=propo-1    # l'echange de la borne superieure
        else:               # si le nombre devenu est egal au nombre choisi alors
            rep="b"
            print(rep)
    # quand on sort de la boucle rep="b", le programme a devine le nombre choisi par l'util

    #l'affichage de messages pour chaque partie
    print(MSG_GAGNE)
    print(MSG_ESS,n_ess, end="\n\n")

    # la reaffectation de variables 
    n_ess_tot+=n_ess/N_PARTIES
    rep=""
    inf = 0
    sup = 100
    n_ess = 0
    n_parties-=1

# l'affichage de la moyenne d'essais apres toutes les parties
print(MSG_MYN_ESS, round(n_ess_tot,2))
