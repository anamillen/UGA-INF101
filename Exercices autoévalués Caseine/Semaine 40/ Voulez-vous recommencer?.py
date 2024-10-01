"""
Ecrire un programme qui demande à l'utilisateur un nombre puis qui 
affiche "Le carré de ce nombre est: " suivi de la bonne valeur. 
Ensuite, le programme demande à l'utilisateur s'il veut recommencer,
 et continue ainsi jusqu'à ce que l'utilisateur réponde "non" à 
 cette question. Dans ce cas, le programme écrit "Au revoir" puis s'arrête.
"""

# l'initialisation de messages pour ameliorer le management au cas ou
INIT ="Nombre:"
RES = "Le carre de ce nombre est"
REINIT = "Voulez-vous recommencer?"
END = "Au revoir"

# l'initialisation du flag pour prendre en compte les reponses de
# l'utilisateur
flag = "oui"

# la boucle s'execute jusqu'a l'util repond non ou qqch different de oui
while flag=="oui":
    nmbr = float(input(INIT))
    print(RES,nmbr**2)
    flag = input(REINIT)   # on redemande l'util chaque fois s'il veut continuer

# a partir d'ici flag!="oui", le message de salutation s'affiche
print(END)

