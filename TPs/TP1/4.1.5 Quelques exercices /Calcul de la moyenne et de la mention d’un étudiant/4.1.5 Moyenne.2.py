""" 
Calcul de la moyenne
Si la note entree n'est pas comprise entre 0 et 20 le programme s'arrete
"""

# l'initialisation du message sous la forme d'une constante
INCOR = "INCORRECT"


# l'utilisateur entre les valeurs des notes, si la note n'est pas comprise entre 0 et 20 le programme s'arrete 
chim = int(input())
if 0<=chim<=20:
    phy = int(input())
    if 0<=phy<=20: 
        math = int(input())
        if 0<=math<=20:
            info = int(input())
            if 0<=info<=20:
                moyenne = (chim+phy+math+info)/4
                print(moyenne)


# l'affichage des messages si une de notes n'est pas comprise entre 0 et 20
            else:
                print("INCOR")
        else:
            print(INCOR)
    else:
        print(INCOR)
else:
    print(INCOR)




