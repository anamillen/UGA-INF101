import turtle # on importe turtle


# la definition de la fonction
def triangle(x,y,cote):
    """Trace triangle de taille donnée (cote)."""
    # l'initialisation de la position initiale
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    
    i = 1 # compteur du nb de cotes
    while i <= 3 :
        turtle.forward(cote)
        turtle.right(120)
        i+=1




"""
test avec plusieurs triangles randomises

from random import randint
for i in range(10):
    x = randint(-200,200)
    y = randint(-200,200)
    cote = randint(1,10)*10
    triangle(x,y,cote)

"""
