from random import randint      # on importe le module random et sa methode randint

# initialisation des constantes pour les messages
MSG_INIT = "Devine mon nombre entre"
MSG_PT = "Trop petit"
MSG_GR = "Trop grand"
MSG_WIN = "Gagné"

# on definit un nombre aleatoire entier entre 1 et 100 avec randint
NMBR = randint(1, 100)

# on definit les valeurs initiales des variables
essaye = 0
upper = 100  # la borne superieure
lower = 1    # la borne inferieure

while essaye != NMBR:  # boucle pour que l'utilisateur essaye de deviner le nombre
    print(MSG_INIT, lower, "et", upper)  # afficher les bornes actuelles
    essaye = int(input())  # on recupere l'essai de l'utilisateur

    # on verifie si l'essai est trop petit ou trop grand et on ajuste les bornes
    if essaye < NMBR:
        print(MSG_PT)
        lower = essaye + 1  # si l'essai est trop petit, on ajuste la borne inferieure
    elif essaye > NMBR:
        print(MSG_GR)
        upper = essaye - 1  # si l'essai est trop grand, on ajuste la borne superieure

# une fois sorti de la boucle, l'utilisateur a devine le bon nombre (essaye == NMBR)

# affichage du message de victoire quand l'utilisateur a devine
print(MSG_WIN)
