"""
Ecrire un programme qui demande à l'utilisateur un prix en euros, puis le convertit en dollars (avec le taux suivant: 1 euro= 1,0627 dollars). On n'arrondira pas le résultat.

Pour les phrases à afficher, vous suivrez le modèle de l'exemple suivant:

Prix en euros:

* l'utilisateur tape 100*

Prix en dollars: 106.27

/!\ Lorsque que l'on vous demande d'afficher une phrase à l'écran, vous devez suivre celle de l'exemple à la lettre (seuls les différences de ponctuation, d'espaces, de majuscules, et de certains accents sont tolérées).

(Exercice proposé par Aurélie Lagoutte)
"""
print("Prix en euros:")
eur = float(input())
dol = eur*1.0627
print("Prix en dollars :", dol)
