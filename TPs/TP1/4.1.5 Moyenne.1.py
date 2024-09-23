# l'utilisateur entre les notes de 4 matieres
# les notes se conversent en entiers pour faire des calculations apres
chim = int(input())
phy = int(input())
math = int(input())
info = int(input())

# l'initialisation des messages
INCOR = "INCORRECT"
COR = "CORRECT"

# la calculation de la moyenne
moyenne = (chim+phy+math+info)/4

# la verification de validite des notes
if chim>20 or chim<0 or phy>20 or phy<0 or math<0 or math>20:
    print("INCORRECT") 
else: # si toutes les notes sont compris entre 0 et 20, on affiche la moyenne calculee
    print(moyenne)




