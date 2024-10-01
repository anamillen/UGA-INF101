"""
Ecrire un programme qui commence par demander à l'utilisateur un nombre avec 
"Nombre max de lettres ?", puis qui demande répétitivement
 une lettre à l'utilisateur en affichant "Lettre :" jusqu'à ce que:

    soit le nombre max. de lettres soit atteint,
    soit l'utilisateur tape "stop" à la place de la lettre attendue.

Le programme doit finir en affichant le mot obtenu par 
la concaténation de toutes les lettres données par l'utilisateur.
"""



# l'initialisation de constantes
MSG ="Lettre :"
MAX = int(input("Nombre max de lettres ?"))

mot = ""    # l initialisation d'une var pour sauvegarder les lettres saisies

flag =""    # un drapeau pour sortir de la boucle s'il == "stop"
n = 0       # un decompteur pour respecter le max de lettres


while n<MAX:        # tandis que le n max de lettres n'est pas atteint on execute la boucle
    
    flag = input(MSG)
    if flag=="stop":
        n = MAX     # on sort de la boucle
    else:           # on continue a saisir les lettres, flag!="stop"
        mot+=flag
        n+=1

# l'affichage de toutes les lettres saisies
print(mot)






