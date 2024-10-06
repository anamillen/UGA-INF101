# l'import de modules
import math


# la definition de la fonction

def diametre_polygone(nb_cotes, cote):
    """
    renvoie le diamètre d’un polygone régulier à nb_cotes de longueur cote.
    """
    PI = math.pi
    
    diametre = cote/(math.sin(PI/nb_cotes))
    return diametre

    
"""
# programme principal

# l 'initialisation de constantes
MSG_N = "Choisissez le nombre de cotes : "
MSG_L = "Entrez la longueur d'un cote : "



# l'utilisateur saisit
n = int(input(MSG_N))
cote = float(input(MSG_L))

# appel a la fonction
print(diametre_polygone(n, cote))
"""










