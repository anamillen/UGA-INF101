import turtle # on importe turtle



# les definitions des fonctions
def carre(cote_deb, nb_car) :
    """Trace des carrés imbriqués comme sur la figure ci-contre : le plus grand carré a
pour côté cote_debut, la taille du carré est multipliée par 2/3 à chaque étape,
et le nombre de carrés tracés est nb_carres

Tests de la fonction
carre(100,5)
carre(200,10)

"""

    # on itinialise les constantes
    ALPH = 90
    COTES = 4

    cote = cote_deb
    
    i = 0 # compteur du nb de carres
    while i < nb_car:
        j = 0 # compteur du nb de cotes d'un carre
        while j < COTES :
            turtle.forward(cote)
            turtle.right(ALPH)
            j += 1
        cote=cote*2/3
        i+=1
    



# programme principal


