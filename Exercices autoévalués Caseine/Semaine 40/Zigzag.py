"""
Ecrire un programme qui demande à l'utilisateur deux entiers 
qui correspondront à la numérotation de la première et 
de la dernière ligne, puis un troisième entier qui correspondra 
au nombre de z avant "zigzag" (sans compter le premier "z" de zigzag), 
puis enfin qui affiche un zig-zag suivant le modèle suivant:

Numero de début:* l'utilisateur tape 3 *
Numero de fin:* l'utilisateur tape 10 *
Nombre de z:  * l'utilisateur tape 5 *
zzzzzzigzag 3
4 zzzzzzigzag
zzzzzzigzag 5
6 zzzzzzigzag
zzzzzzigzag 7
8 zzzzzzigzag
zzzzzzigzag 9
10 zzzzzzigzag
"""




# la saisie de l'utilisateur, transformation de type 
deb = int(input("Numero de debut:"))
FIN = int(input("Numero de fin:"))
Z = int(input("Nombre de z:"))

zig = "z"*Z+"zigzag"    # l'initilisation de la chaine pour la reutilisation

while deb<=FIN:             # la boucle pour affcher le nombre exact de lignes

    if deb%2==0:        # si le nombre est pair il s'affiche avant le msg
        print(deb,zig)
    else:               # si le nombre est impair il s'affiche apres le msg
        print(zig,deb)
    deb+=1      #on enumere chaque ligne en ajoutant au compteur       
# a partir d'ici deb==FIN
