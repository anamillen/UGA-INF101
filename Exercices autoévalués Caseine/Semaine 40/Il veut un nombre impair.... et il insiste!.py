"""
Ecrire un programme qui demande à l'utilisateur de taper un nombre impair. 
Si l'utilisateur tape un nombre pair, le programme doit afficher 
"J'ai demandé un nombre impair! Re-essayez:" et ainsi de suite jusqu'à ce 
que l'utilisateur tape enfin un nombre impair. Lorsque c'est le cas, 
le programme affiche "Merci" et s'arrête.
"""



# l'initialisation de messages pour afficher a l'utilisateur
INIT = "Nombre impair"
END = "Merci"
INCOR = "J'ai demande un nombre impair! Re-essayez:"


nmbr = int(input(INIT))     # on donne la possibilite a l'utilisateur d'entrer
                            # le bon nombre tout de suite et ne pas entrer dans la boucle
while nmbr%2==0:            # si le nombre saisi est impair la boucle s'execute
    nmbr = int(input(INCOR))
# a partir d'ici nmbr est impair

print(END)
    