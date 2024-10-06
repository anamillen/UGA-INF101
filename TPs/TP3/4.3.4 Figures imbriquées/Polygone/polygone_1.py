# l'import de modules
import turtle


# la definition de la fonction

def polygone(nb_cotes, cote):
    """
    trace un polygone régulier à nb_cotes côtés (triangle, 
    carré, pentagone, hexagone....) et dont la longueur d’un côté est cote. 
    """
    # def des constantes
    DIM = 360
    alph = 360/nb_cotes
    
    i = 0   # l'initialisation d'un decompteur pour conditionner la boucle

    # la boucle pour tracer n cotes
    while i<nb_cotes:
        turtle.forward(cote)
        turtle.right(alph)
        i+=1    # on augmente la valeur du decompteur
    # d'ici i == n



"""
# programme principal

# l 'initialisation de constantes
MSG_N = "Choisissez le nombre de cotes : "
MSG_L = "Entrez la longueur d'un cote : "

# l'utilisateur saisit
n = int(input(MSG_N))
cote = float(input(MSG_L))

# appel a la fonction
polygone(n, cote)

"""








