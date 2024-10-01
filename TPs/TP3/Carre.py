"""
Écrivez un programme permettant de tracer un carré de côté 100. A la fin du
tracé, le curseur doit être au même
endroit et dans la même direction qu’au début du tracé.
"""

import turtle

turtle.speed(1)

n = 0       # on initialise le decompteur pour arreter la bouccle apres qu'on
            # a trace exactement un carre
alpha = 90  # l'angle alpha pour diriger turtle vers la bonne direction


while n<4:      # la boucle s'execute jusqu'au moment ou turtle a trace les 4
                # cotes du carre
    turtle.forward(100)     # turtle avance par 100 pas 
    turtle.left(alpha)      # turtle pivote vers la gauche par 90 degres
    n+=1                    # on augmente le decompteur apres qu'on a trace une cote



