"""
Ecrire un programme qui:

    affiche le titre "Maximum de trois entiers",
    puis qui demande successivement trois entiers à l'utilisateur,
    puis qui affiche "Le maximum est" suivi de la valeur du maximum des trois entiers fournis.

Pour les phrases à afficher, vous suivrez le modèle de l'exemple suivant:

Maximum de trois entiers
1er entier= * l'utilisateur tape 3*
2eme entier= * l'utilisateur tape 9*
3eme entier= * l'utilisateur tape -4*
Le maximum est : 9 

(Exercice proposé par Julie Peyre et Aurélie Lagoutte)
"""


print("Maximum de trois entiers")
a = int(input("1er entier="))
b = int(input("2eme entier="))
c = int(input("3eme entier="))

"""On peur faire aussi juste 
print("Le maximum est:", max(a,b,c))"""

print("Le maximum est :",max(a,b,c))