import turtle
def carre() :
    # trace un carre de taille 100
    i = 1 # compteur du nb de cotes
    while i <= 4 :
        turtle.forward(100)
        turtle.right(90)
        i = i + 1

# prog. principal, avec appel de fonc.
carre()
turtle.up()
turtle.forward(130)
turtle.down()
carre()
