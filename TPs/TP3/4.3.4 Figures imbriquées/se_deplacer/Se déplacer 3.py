# l'importation des modules
import turtle
from random import randint

# la transformation de dimensions de la fenetre
INF = -400
SUP = 400

# on change l'affichage du turtle 
turtle.shape("turtle")
turtle.up()
turtle.speed(0)


# les definitions des fonctions

def gen(inf,sup):
    """Genere la prochaine configuration du turtle"""
    x = randint(inf,sup); y = randint(inf,sup)
    alph = randint(0,360)
    return x,y,alph



def deplacement(inf,sup):
    """Deplace le turtle en utilisant les coordonees et l'angle
    generes par la fonction gen(inf,sup). Ne prend aucun argument"""
    x,y,alph = gen(inf,sup)
    turtle.goto(x,y)
    turtle.right(alph)
    turtle.stamp()

# programme principal
MSG_INIT = "Combien de stamps voulez-vous ? "
i=0                 # on definit le decompteur pour gerer la boucle
n = int(input(MSG_INIT))    # l'utilisateur choisit le nombre de stamps


while i<n:
    deplacement(INF,SUP)
    i+=1
# d'ici i==n















