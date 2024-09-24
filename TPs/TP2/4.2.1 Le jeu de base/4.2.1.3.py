from random import randint  # on importe le module random et sa methode randint

# initialisation des constantes pour les messages
MSG_INIT = "Devine mon nombre entre"
MSG_PT = "Trop petit"
MSG_GR = "Trop grand"
MSG_WIN = "Gagné au bout de"
MSG_LOSE = "Perdu"

# on definit un nombre aleatoire entier entre 1 et 100 avec randint
NMBR = randint(1, 100)

# on definit les valeurs initiales des variables
essaye = 0
upper = 100  # la borne superieure
lower = 1    # la borne inferieure
n_essayes = 5   # compteur initial du nombre d'essais

# l'utilisateur essaye de deviner le nombre jusqu'a la bonne reponse ou jusqu'a epuiser ses essais
while essaye != NMBR and n_essayes > 0:
    print(MSG_INIT, lower, "et", upper)  # on affiche les bornes actuelles
    essaye = int(input())  # on recupere l'essai de l'utilisateur
    n_essayes -= 1  # on decremente le compteur d'essais restants

    # on verifie si l'essai est trop petit ou trop grand et on ajuste les bornes
    if essaye < NMBR:
        print(MSG_PT)
        lower = essaye + 1  # si l'essai est trop petit, on ajuste la borne inferieure
    elif essaye > NMBR:
        print(MSG_GR)
        upper = essaye - 1  # si l'essai est trop grand, on ajuste la borne superieure

# une fois sorti de la boucle, soit le nombre a ete devine, soit les essais sont epuises

if essaye == NMBR:
    # affichage du message de victoire si l'utilisateur a devine le bon nombre
    print(MSG_WIN,5-n_essayes)
else:
    # affichage du message de defaite si l'utilisateur a epuisé ses essais sans deviner
    print(MSG_LOSE)

