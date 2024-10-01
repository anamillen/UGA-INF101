import turtle       # on importe le module

# l'initialisation de constantes
MSG = "Combien de figures tracees voulez-vous ? "
COTE = 50
DIST = 10

# l'utilisateur choisit le nombre de figures a dessiner
N = int(input(MSG))

# on change la position initiale du turtle, on oublie pas d'enlever le crayon et de le abaisser apres
turtle.up()
turtle.goto(-200,200)
turtle.down()

j = 0       # on initialise le decompteur qui represent le nombre de figures

while j<N:      # lorsqu'on a encore des carres pour tracer la boucle s'execute
    if j%2==0:
        i = 4       # on (re)initialise un decompteur pour les cotes du carre
        alph = 90   # on (re)initialise l'angle entre les cotes d'un carre
        
    else:
        i = 3       # on (re)initialise un decompteur pour les cotes du triangle
        alph = 120   # on (re)initialise l'angle entre les cotes d'un triangle
    while i>0:  # lorsqu'il nous restent des cotes a tracer pour une figure la boucle s'execute
        turtle.forward(COTE)
        turtle.right(alph)
        i-=1    # on diminuit la valeur du decompteur des cotes
    # ici le turtle se deplace a la prochaine position pour tacer une nouvelle figure
    turtle.up()
    turtle.forward(COTE+DIST)
    turtle.down()
    j+=1        # on diminuit la valeur du decompteur des carres

