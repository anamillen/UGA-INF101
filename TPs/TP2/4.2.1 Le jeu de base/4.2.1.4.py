from random import randint      # on importe le module random et son methode randint

# l'initialisation de constantes
MSG_INIT = "Devine mon nombre entre"
MSG_PT = "Trop petit"
MSG_GR = "Trop grand"
MSG_WIN = "Gagné"
MSG_LOSE = "Perdu"

# on definit un nombre aleatoire entier [1,100] en utilisant le methode randint
NMBR = randint(1,100)

# on deifinit les valeurs des variables initiales
essaye = 0
upper = 100  # la borne superieure 
lower = 1    # la borne inferieure
n_essayes = 5   # l'initialisation du compteur d'essayes

while essaye!=NMBR and n_essayes>0:     # l'utilisateur essaye de deviner le nombre jusqu'a il a la bonne reponse
    print(MSG_INIT,lower,"et",upper,"(",n_essayes,"essais )")
    essaye = int(input())
    

    # pour indiquer a l'utilisateur si son nombre est trop petit ou trop grande on ajoute les conditions
    if essaye<NMBR:
        print(MSG_PT)
        n_essayes-=1    # on decrement le compteur d'essayes
        lower=essaye+1  #si le nombre devine est plus petit que le nombre tire alors le nombre tire est compris
                        # entre [nombre devine+1;borne superieure]
    elif essaye>NMBR:
        print(MSG_GR)
        n_essayes-=1    # on decrement le compteur d'essayes
        upper=essaye-1  #si le nombre devine est plus grand que le nombre tire alors le nombre tire est compris
                        # entre [borne inferieure;nombre devine-1]
                        
# des qu'on est sorti de la boucle nombre devine par l'utilisateur est egal a celui-ci qu'on a tire (essaye==NMBR)
# ou il reste 0 essayes a l'utilisateur et il n'a pas devine le nombre correct


if essaye==NMBR:
    # l'affichage de message si l'utilisateur a gagne
    print(MSG_WIN)
else:
    # l'affichage de message si l'utilisateur a perdu
    print(MSG_LOSE)
