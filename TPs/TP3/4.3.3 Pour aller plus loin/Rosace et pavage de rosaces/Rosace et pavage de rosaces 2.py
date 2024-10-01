import turtle # on importe turtle

turtle.speed(0)


# les definition des fonction
def rosace(nb,r):
    """Trace une rosace centrée sur le point de coordonnées (x,y),
    composée de nb cercles chacun de rayon r.
    
    Tests de la fonction:
    rosace(-100,100,10,100)
    rosace(70,-150,12,20)    
    rosace(150,150,2,30)

    """

    # initialisation des constantes et variables
    ALPH = 360/nb
    i = 0 # decompteur pour compter les cercles traces

    # l'algorithme principal
    while i<nb:
        turtle.circle(r)        # turtle trace un cercle
        turtle.right(ALPH)      # turtle tourne a droit pour tracer prochain cercle
        i+=1


def ligne_de_rosaces(x,y,l):
    """Trace une ligne de tl rosaces"""

    # On initialise les constantes
    
    NMBR = " Nombre de cerles ? "
    RAY = "De rayon ? "

    # turtle prend la position initiale
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

    # on demande l'utilisateur pour obtenir les parametres pour fonc rosace()
    
    nb = int(input(NMBR))
    r = int(input(RAY))

    # on initialise le decompteur pour compter le nombre de rosaces deja tracees
    i = 0
    
    while i<l:      # dans la boucle on trace chaque rosaces separement et aussi deplace turtle pour suivant rosace
        rosace(nb,r)
        turtle.up()
        turtle.forward(4*r)
        turtle.down()
        i+=1    
    

# programme principal

# On initialise les constantes
LEN = "Combien de rosaces voulez-vous ? "
POS = "initial ? "



# La saisie de nombre de rosaces par l'utilisateur
x = int(input("x "+POS))
y = int(input("y "+POS))
l = int(input(LEN))


# l'execution de la fonction
ligne_de_rosaces(x,y,l)
         
