import turtle       # on importe le module turtle

# la definition de la fonction
def descendre_sans_tracer(lon):
    """
    Descend de longueur par rapport à la
    position actuelle, sans tracer.
    """
    # l'initilaisation des constantes
    ALPH = 90
    # l'algo principal
    turtle.up()
    turtle.right(ALPH)
    turtle.forward(lon)
    turtle.left(ALPH)
    turtle.down()














