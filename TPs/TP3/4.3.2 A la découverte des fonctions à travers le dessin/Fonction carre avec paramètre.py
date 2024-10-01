import turtle

def carre(x,y,cote) :
    """Trace carré de taille donnée (cote)."""
    # l'initialisation de la position initiale
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    
    i = 1 # compteur du nb de cotes
    while i <= 4 :
        turtle.forward(cote)
        turtle.right(90)
        i = i + 1

"""
test avec plusieurs carres randomises

from random import randint

for i in range(10):
    x = randint(-200,200)
    y = randint(-200,200)
    cote = randint(1,10)*10
    carre(x,y,cote)
"""
