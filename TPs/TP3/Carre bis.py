"""
odifiez le programme précédent pour dessiner un carré identique au p
récédent dont le coin supérieur gauche
a pour coordonnées le point (-50,20). A la fin du tracé, le curseur doit être
au même endroit (-50,20) et dans la même
direction qu’au début du tracé.
Attention : à l’exécution de votre programme, seul le carré doit être tracé !
Si le point (-50,20) n’est pas le coin supérieur
gauche mais plutôt le coin inférieur gauche de votre carré, essayez de tourner
dans l’autre sens.
"""

import turtle

turtle.up()             # on enleve le crayon pour laisser pas de traces
turtle.goto(50,-20)     # on initialise la position initiale pour proceder
turtle.down()           # on baisse le crayon pour tracer le carre


n = 0       # on initialise le decompteur pour arreter la bouccle apres qu'on
            # a trace exactement un carre
alpha = 90  # l'angle alpha pour diriger turtle vers la bonne direction


while n<4:      # la boucle s'execute jusqu'au moment ou turtle a trace les 4
                # cotes du carre
    turtle.forward(100)     # turtle avance par 100 pas 
    turtle.right(alpha)      # turtle pivote vers le droit par 90 degres
    n+=1                    # on augmente le decompteur apres qu'on a trace une cote

