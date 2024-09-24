from random import randint      # on importe le module random et sa methode randint

# initialisation des constantes pour les messages
MSG_INIT = "Devine mon nombre entre 0 et 100"
MSG_PT = "Trop petit"
MSG_GR = "Trop grand"
MSG_WIN = "Gagné"

# on definit un nombre aleatoire entier entre 1 et 100 avec randint
NMBR = randint(1, 100)

# on initialise la variable "essaye" pour commencer la boucle
essaye = 0
while essaye != NMBR:  # boucle pour que l'utilisateur devine le nombre jusqu'a la bonne reponse
    print(MSG_INIT)
    essaye = int(input())  # on recupere l'essai de l'utilisateur

    # on informe l'utilisateur si son essai est trop petit ou trop grand
    if essaye < NMBR:
        print(MSG_PT)
    elif essaye > NMBR:
        print(MSG_GR)

# une fois sorti de la boucle, l'utilisateur a devine le bon nombre (essaye == NMBR)

# affichage du message de victoire quand l'utilisateur a devine
print(MSG_WIN)
