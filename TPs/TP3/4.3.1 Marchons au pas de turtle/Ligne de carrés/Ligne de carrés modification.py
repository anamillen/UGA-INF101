import turtle       # on importe le module

# l'initialisation de constantes
COTE = 50
DIST = 60
ALPH = 90
n = 8       # on initialise le decompteur qui represent le nombre de carres

# on change la position initiale du turtle, on oublie pas d'enlever le crayon et de le abaisser apres
turtle.up()
turtle.goto(-200,200)
turtle.down()

while n>0:      # lorsqu'on a encore des carres pour tracer la boucle s'execute
    i = 4       # on (re)initialise un decompteur pour les cotes des carres
    while i>0:  # lorsqu'il nous restent des cotes a tracer pour un carre la boucle s'execute
        turtle.forward(COTE)
        turtle.right(ALPH)
        i-=1    # on diminuit la valeur du decompteur des cotes
    # ici le turtle se deplace a la prochaine position pour tacer un nouveau carre
    turtle.up()
    turtle.forward(DIST)
    turtle.down()
    n-=1        # on diminuit la valeur du decompteur des carres



