"""
Vous partez à la recherche d'un trésor caché dans une pyramide. Vous avez réussi à obtenir des informations sur les épreuves qui vous attendent à l'intérieur de celle-ci:

- dans le hall d'entrée, une statue de sphinx va vous demander un code secret sous la forme suivante : "Je n'aime que les nombres p qui sont des nombres premiers, 
tels que p+2 soit aussi un nombre  premier... Et mon nombre préféré de la journée est  *un nombre qui change tous les jours*. 
Le code secret est le plus petit nombre supérieur ou égal à mon nombre préféré parmi les nombres que j'aime."

- une fois entré, vous parcourez un labyrinthe dont vous vous êtes déjà procuré le plan, puis vous arrivez face à une statue d'Osiris qui garde la salle du trésor. 
Il va vous demander un code secret sous la forme suivante: "Je n'aime que les nombres n tels que n+1 soit une puissance de 2.... et il faut également que le reste de la division de n par 5 soit égal à 3... Mon nombre préféré de la journée est *un nombre qui change tous les jours*. Le code secret est le plus petit nombre supérieur ou égal à mon nombre préféré, parmi les nombres que j'aime."

Pour chacune des deux énigmes, vous n'aurez que 5 secondes pour répondre, sinon la sortie sera verrouillée et vous resterez enfermés dans la pyramide à tout jamais. 
Pour éviter cela à tout prix, vous décidez d'écrire un programme que vous emporterez sur votre smartphone et qui vous aidera à résoudre les énigmes. Pour cela:

    Ecrire une fonction est_premier qui prend en argument un entier supérieur ou égal à 2 et qui renvoie True si l'entier en premier, False sinon.
    Ecrire une fonction sphinx_aime qui prend en argument un entier supérieur ou égal à 2 et qui renvoie True si l'entier est un nombre que le sphinx aime, False sinon.
    Ecrire une fonction code_hall qui prend en argument le nombre préféré du sphinx ce jour-là (un entier strictement positif) et qui renvoie le code secret du hall.
    Ecrire une fonction est_puissance2 qui prend en argument un entier positif et qui renvoie True s'il s'agit d'une puissance de 2, False sinon.
    On vous demande ici de ne pas utiliser le logarithme, et de fournir une solution efficace (par exemple, sur un immense entier impair, votre fonction doit immédiatement répondre False)
    Ecrire une fonction osiris_aime qui prend en argument un entier positif et qui renvoie True si Osiris aime cet entier, False sinon.
    Ecrire une fonction code_tresor qui prend en argument le nombre préféré d'Osiris ce jour-là (un entier strictement positif) et qui renvoie le code secret permettant d'accéder au trésor.

"""



def est_premier(N):
    """prend en argument un entier N supérieur ou égal à 2 et renvoie true si l'entier est premier, false sinon"""
    ans = True
    div_curr = 2    # on initialise le premier diviseur possible du nombre N
    while ans and div_curr < N:
        if N % div_curr == 0:  # si N est divisible par div_curr, alors N n'est pas premier
            ans = False
            
        # condition additionnelle pour diminuer le temps de calcul
        if div_curr % 2 != 0:
            div_curr += 2  # on passe au prochain nombre impair
        else:
            div_curr += 1  # si div_curr est 2, on passe au prochain impair (3)
            
    return ans

def sphinx_aime(N):
    """prend en argument un entier N supérieur ou égal à 2 et renvoie true si l'entier est un nombre que le sphinx aime, false sinon"""
    return est_premier(N) and est_premier(N + 2)  # vérifie si N et N + 2 sont des nombres premiers

def code_hall(N):
    """prend en argument le nombre préféré du sphinx N ce jour-là et renvoie le code secret du hall"""
    code = N
    while not sphinx_aime(code):  # tant que le code n'est pas aimé par le sphinx
        if code % 2 != 0:
            code += 2  # si le code est impair, on ajoute 2
        else:
            code += 1  # si le code est pair, on le rend impair en ajoutant 1
    return code
    
def est_puissance2(n):
    """prend en argument un entier positif et renvoie true s'il s'agit d'une puissance de 2, false sinon"""
    ans = False
    x = 1
    if n == 1:
        ans = True  # 1 est une puissance de 2 (2^0)
    elif n % 2 == 0:
        while n >= x and not ans:  # on vérifie si n correspond à une puissance de 2
            if n == x:
                ans = True  # n est une puissance de 2
            x *= 2  # on passe à la prochaine puissance de 2
    return ans

def osiris_aime(N):
    """prend en argument un entier positif N et renvoie true si osiris aime cet entier, false sinon"""
    return N % 5 == 3 and est_puissance2(N + 1)  # vérifie que N satisfait les deux conditions d'osiris

def code_tresor(N):
    """prend en argument le nombre préféré d'osiris ce jour-là et renvoie le code secret permettant d'accéder au trésor"""
    code = N
    if code % 2 == 0:  # si le code est pair, on le rend impair en ajoutant 1
        code += 1
    while not osiris_aime(code):  # tant qu'osiris n'aime pas le code, on l'incrémente de 2
        code += 2
    return code
        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    # Vos tests ici
    

   