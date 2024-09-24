from random import randint

# constantes
MSG_IAI = "Moyenne des essais de l'IA intelligente pour"
MSG_IAA = "Moyenne des essais de l'IA aleatoire pour"

# initialisation des variables pour les moyennes
tire = 0

# boucle pour chaque nombre secret de 0 a 100
while tire <= 100:

    # initialisation des accumulateurs pour le nombre d'essais
    total_essais_iai = 0
    total_essais_iaa = 0

    # boucle pour faire jouer chaque IA 100 fois
    n_parties = 100
    while n_parties > 0:

        # --- IA INTELLIGENTE ---
        inf = 0
        sup = 100
        n_ess_iai = 0
        rep = ""
        while rep != "b":  # tant que le nombre n'est pas devine
            propo = inf + (sup - inf) // 2  # choix de l'IA intelligente (milieu des bornes)
            n_ess_iai += 1  # increment du nombre d'essais
            if propo < tire:
                inf = propo + 1  # mise a jour de la borne inferieure
            elif propo > tire:
                sup = propo - 1  # mise a jour de la borne superieure
            else:
                rep = "b"  # le nombre a ete devine
        total_essais_iai += n_ess_iai

        # --- IA ALEATOIRE ---
        inf = 0
        sup = 100
        n_ess_iaa = 0
        rep = ""
        while rep != "b":  # tant que le nombre n'est pas devine
            propo = randint(inf, sup)  # choix aleatoire entre les bornes
            n_ess_iaa += 1  # increment du nombre d'essais
            if propo < tire:
                inf = propo + 1  # mise a jour de la borne inferieure
            elif propo > tire:
                sup = propo - 1  # mise a jour de la borne superieure
            else:
                rep = "b"  # le nombre a ete devine
        total_essais_iaa += n_ess_iaa

        # decrementer le nombre de parties restantes
        n_parties -= 1

    # calcul des moyennes pour le nombre secret actuel
    moyenne_iai = total_essais_iai / 100  # moyenne essais IA intelligente
    moyenne_iaa = total_essais_iaa / 100  # moyenne essais IA aleatoire

    # affichage des resultats pour le nombre secret actuel
    print(str(tire).rjust(3),"*"*round(moyenne_iai))
    print(str(tire).rjust(3),"-"*round(moyenne_iaa))

    # passer au nombre secret suivant
    tire += 1

