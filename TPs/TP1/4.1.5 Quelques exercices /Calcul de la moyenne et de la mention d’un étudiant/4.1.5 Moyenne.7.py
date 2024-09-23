"""---------L'INITIALISATION------------"""
# définition des messages constants pour l'interface utilisateur
MSG_INIT = "Entrez votre note."
MSG_ARRET = "(Pour arreter le programme entrez -1) :"
MSG_COEF = "Entrez le coefficient pour la note que vous venez d'entrer :"
MSG_CHANCE = "Votre note doit etre comprise entre 0 et 20. Essayez encore une fois."
MSG_INCOR = "INCORRECT"
MYN = "Votre moyenne est :"
NT = "Votre mention est :"

# initialisation des variables pour le calcul de la moyenne
somme_coef = 0  # somme des coefficients
somme_note = 0  # somme des notes pondérées

"""---------------LES ENTREES----------------"""
# initialisation des variables pour la saisie
note = 0  # note courante
coef = 0  # coefficient courant

"""--------------L'ALGORITHME PRINCIPAL----------------"""
# boucle principale pour la saisie des notes et coefficients
while note != -1:
    # saisie de la note
    note = float(input(MSG_INIT+" "+MSG_ARRET))
    
    # vérification de la validité de la note
    if 0 <= note <= 20:
        # saisie du coefficient si la note est valide
        coef = int(input(MSG_COEF))
        # mise à jour des sommes pour le calcul de la moyenne
        somme_note += note * coef
        somme_coef += coef
    elif note != -1:  # la note est hors bornes et différente de -1
        print(MSG_INCOR, MSG_CHANCE)

# calcul de la moyenne
if somme_coef == 0:
    myn = 0
    
else: # si les notes et coeffcients ont ete saisis alors on fait du calcul
    myn = somme_note/somme_coef
    # affichage de la moyenne arrondie à deux décimales
    print(MYN, round(myn, 2))

    # détermination et affichage de la mention en fonction de la moyenne
    if myn < 10:
        print(NT, "Ajourne")
    elif myn < 12:
        print(NT, "Passable")
    elif myn < 14:
        print(NT, "Assez bien")
    elif myn < 16:
        print(NT, "Bien")
    else:
        print(NT, "Tres bien")


