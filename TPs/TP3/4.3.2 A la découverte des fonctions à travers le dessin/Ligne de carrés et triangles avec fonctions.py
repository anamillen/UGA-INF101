import turtle # on importe turtle



# les definitions des fonctions

def carre(cote) :
    """Trace carré de taille donnée (cote)."""
    
    i = 1 # compteur du nb de cotes
    while i <= 4 :
        turtle.forward(cote)
        turtle.right(90)
        i = i + 1


def triangle(cote):
    """Trace triangle de taille donnée (cote)."""
    
    i = 1 # compteur du nb de cotes
    while i <= 3 :
        turtle.forward(cote)
        turtle.right(120)
        i+=1


# programme principal
# trace ligne carres et triangles





# la definition des constantes
COTE = 50
DIST = 10
N = 8




i = 0       # on initialise le decompteur pour tenir en compte le nmbr de la figure actuelle


# tant qu'on a pas trace le nombre attende de figures la boucle s'execute
while i<N:
    if i%2==0:
        carre(COTE)
    else: # si i est impair alors on dessine le triangle
        triangle(COTE)

    # turtle va a la position ou la figure suivant sera dessinee
    turtle.up()
    turtle.forward(COTE+DIST)
    turtle.down()
    
    i+=1