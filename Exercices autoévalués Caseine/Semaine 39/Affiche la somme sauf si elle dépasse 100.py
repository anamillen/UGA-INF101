"""
Ecrire un programme qui:

- demande à l'utilisateur un premier entier en affichant "Entier a=?"

- demande à l'utilisateur un deuxième entier en affichant "Entier b=?"

- Si la somme des deux entiers est supérieure ou égale à 100, le programme affiche "La somme depasse 100". Sinon, le programme affiche "La somme est (*véritable valeur de a+b*)."

Exemples d'éxecution :

Exemple 1:

Entier a=? *l'utilisateur entre 5*
Entier b=? *l'utilisateur entre 7*
La somme est 12. 

 

Exemple 2:

Entier a=? *l'utilisateur entre 90*
Entier b=? *l'utilisateur entre 12*
La somme dépasse 100. 

 /!\ Lorsque que l'on vous demande d'afficher une phrase à l'écran, vous devez suivre celle de l'exemple à la lettre (seuls les différences de ponctuation, d'espaces, de majuscules, et de certains accents sont tolérées).

(Exercice proposé par Aurélie Lagoutte)
"""


# l'utilisateur entre deux entiers

a = int(input("Entier a=? "))
b = int(input("Entier b=? "))

# l'evaluation de la somme a + b

if a+b>=100:
    print("La somme depasse 100")
else: # si la somme est inferieure a 100 les instructions suivantes s'executent
    print("La somme est",a+b)
