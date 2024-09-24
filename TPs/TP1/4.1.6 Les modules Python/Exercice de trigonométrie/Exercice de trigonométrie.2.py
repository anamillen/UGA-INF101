from math import sqrt  # importation de la fonction racine carrée

# définition des messages constants pour l'interface utilisateur
MSG_ENT = "Entrez trois valeurs a,b,c consequemment"
MSG_A = "a=? "
MSG_B = "b=? "
MSG_C = "c=? "

print("Ce programme est cense de resoudre l'equation ax^2+bx+c=0")

delta = -1  # initialisation de delta à une valeur négative pour entrer dans la boucle

# boucle pour s'assurer que delta est positif ou nul
while delta < 0:
    print(MSG_ENT)
    # saisie des coefficients a, b et c
    a = float(input(MSG_A))
    b = float(input(MSG_B))
    c = float(input(MSG_C))
    
    # calcul du discriminant
    delta = b**2 - 4*a*c
    
    # vérification de la validité du discriminant
    if delta < 0:
        print("Reessayez. La valeur de delta est negatif.")

# calcul des racines de l'équation
x1 = (-b + sqrt(delta)) / (2*a)
x2 = (-b - sqrt(delta)) / (2*a)

# affichage des résultats en fonction du nombre de racines distinctes
if x1 != x2:
    print("Les racines du polynome sont :", x1, x2)
else:
    print("La racine du polynome est :", x1)









