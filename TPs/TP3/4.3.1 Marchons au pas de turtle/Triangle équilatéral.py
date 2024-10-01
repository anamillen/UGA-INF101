import turtle

# l'initialisation de constantes
ALPH = 120
DIST = 100


n = 3       # l'initialisation du decompteur

while n>0:      # lorsu'on a pas trace les 3 cotes la boucle s'execute
    turtle.forward(DIST)
    turtle.right(ALPH)
    n-=1        #on diminuit le decompteur
