""" 
Calcul de la moyenne ponderee
Si la note entree n'est pas comprise entre 0 et 20 le programme s'arrete
"""

# l'initialisation du message sous la forme d'une constante
INCOR = "INCORRECT"

# initialisation de coefficients 
phy_c = 4
chim_c = 3
math_c = 2
info_c = 2

# l'utilisateur entre les valeurs des notes, si la note n'est pas comprise entre 0 et 20 le programme s'arrete
chim = int(input())
if 0<=chim<=20:
    phy = int(input())
    if 0<=phy<=20: 
        math = int(input())
        if 0<=math<=20:
            info = int(input())
            if 0<=info<=20:
                moyenne = (chim*chim_c+phy*phy_c+math*math_c+info*info_c)/(phy_c+chim_c+math_c_info_c) # calcul de la moyenne avec les coefficients
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




