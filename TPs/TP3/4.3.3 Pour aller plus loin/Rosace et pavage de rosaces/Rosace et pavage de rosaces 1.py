import turtle # on importe turtle


# la definition de la fonction
def rosace(x,y,nb,r):
    """Trace une rosace centrée sur le point de coordonnées (x,y),
    composée de nb cercles chacun de rayon r.
    
    Tests de la fonction:
    rosace(-100,100,10,100)
    rosace(70,-150,12,20)    
    rosace(150,150,2,30)

    """

    # turtle prend la position initiale
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

    # initialisation des constantes et variables
    ALPH = 360/nb
    i = 0 # decompteur pour compter les cercles traces

    # l'algorithme principal
    while i<nb:
        turtle.circle(r)        # turtle trace un cercle
        turtle.right(ALPH)      # turtle tourne a droit pour tracer prochain cercle
        i+=1


# programme principal


