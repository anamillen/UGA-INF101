# l'importation des modules
import turtle
from random import randint

# la transformation de dimensions de la fenetre
inf = -400
sup = 400
turtle.shape("turtle")

# lse definitions des fonctions

def gen(inf,sup):
    x = randint(inf,sup); y = randint(inf,sup)
    alph = randint(0,360)
    return x,y,alph



def deplacement(x,y,alph):
    x,y,alph = gen(inf,sup)
    turtle.stamp()


i=0
n = int(input())
while i<n:
    x,y,alph = gen(inf,sup)
    deplacement(x,y,alph)
    i+=1
















