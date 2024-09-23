"""
Ecrire un programme qui demande un entier positif n et qui calcule la factorielle de n. Si le nombre donné est strictement négatif, le programme doit afficher un message d'erreur et terminer. Pour les phrases à afficher, vous suivrez celles des exemples suivants.

Rappel: la factorielle de n est définie par: n! = 1 x 2 x 3 x .... x n

Exemple 1:

n=? -5
La factorielle n'est pas definie pour les nombres négatifs.

Exemple 2:

n=? : 5
La factorielle de 5 vaut 120 .

Exemple 3:

n=? 0
La factorielle de 0 vaut 1 .

(Exercice proposé par Amir Charif et Aurélie Lagoutte)
"""

# l'initialisation de constantes, variables et de messages
MSG_INIT = "n=?"
MSG_ERR = "La factorielle n'est pas definie pour les nombres negatifs."
facto = 1

# l'utilisateur entre un entier
n = int(input(MSG_INIT))


if n<0:
    print(MSG_ERR)
else:       # si l'entier est bien positif alors on calcule sa factorielle
    print("La factorielle de",n, end=" ")
    while n>0:      #
        facto*=n
        n-=1
    print("vaut",facto, end=" .\n")

