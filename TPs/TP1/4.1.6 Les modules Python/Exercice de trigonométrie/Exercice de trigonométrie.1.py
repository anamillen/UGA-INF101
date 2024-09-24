from math import cos, sin  # importation des fonctions trigonométriques nécessaires

# définition des messages constants pour l'interface utilisateur
HYPO = "Entrez la longueur de l'hypoténuse : "
ALPH = "Entrez la valeur d'un angle : "
REP = "Les deux côtés sont : "

# saisie de la longueur de l'hypoténuse et de la valeur de l'angle 
h = float(input(HYPO))
a = float(input(ALPH))

# calcul de la longueur des côtés
adj = cos(a) * h
opp = sin(a) * h

# affichage des résultats
print(REP, adj, ",", opp)