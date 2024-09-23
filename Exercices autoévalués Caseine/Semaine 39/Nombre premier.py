'''
Ecrire un programme qui demande à l'utilisateur de saisir un entier positif N et qui vérifie si N est premier.

Exemple 1 

Nombre : 25
25 n'est pas premier.

Exemple 2

Nombre : 7
7 est premier.

/!\ Comme d'habitude, lorsque que l'on vous demande d'afficher une phrase à l'écran, vous devez suivre celle du modèle à la lettre (seuls les différences de ponctuation, d'espaces, de majuscules, et de certains accents sont tolérées).

(Exercice proposé par Amir Charif et Aurélie Lagoutte)
'''

# initialisation des messages
MSG_INIT = "Nombre : "
MSG_NP = "n'est pas premier."
MSG_P = "est premier."
n = int(input(MSG_INIT)) # l'utilisateur entre un nombre entier positif

# On définit un nombre premier comme un nombre qui ne se divise que par 1 et par lui-même
# Pour optimiser l'algorithme, on peut définir une variable `n_sup` qui sera un peu plus grande que la moitié de `n`
# (car il n'y a pas de nombre entier supérieur à 2 et différent de 1 qui divise quelconque `n`)
n_sup = n//2+1

# on parcourt les nombres de `n_sup` à 1 pour vérifier si `n` est divisible par l'un d'eux
while n_sup > 0:
    if n % n_sup == 0 and n_sup!=1 and n_sup!=n:
        print(n, MSG_NP) # `n` n'est pas premier
        n_sup = 0 # on sort de la boucle
    else:
        if n_sup == 1:
            print(n, MSG_P) # `n` est premier
        n_sup -= 1 # on décrémente `n_sup` pour tester le prochain nombre