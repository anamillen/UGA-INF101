def demander_mot(joueur):
    """Demande au joueur de saisir un mot secret."""
    mot = input(f"Joueur {joueur}, entrez un mot secret : ")
    print("\n" * 50)  # Efface l'écran pour cacher le mot
    return mot

def afficher_squelette(mot, lettres_trouvees):
    """Retourne une chaîne représentant le mot avec les lettres trouvées."""
    resultat = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            resultat += lettre + " "
        else:
            resultat += "_ "
    return resultat.strip()

def demander_lettre(lettres_essayees):
    """Demande une lettre et vérifie qu'elle n'a pas été jouée."""
    while True:
        lettre = input("Entrez une lettre : ")
        if lettre not in lettres_essayees:
            return lettre
        else:
            print("Vous avez déjà essayé cette lettre.")

def compter_occurrences(mot, lettre):
    """Compte les occurrences de lettre dans mot sans utiliser count."""
    compteur = 0
    for char in mot:
        if char == lettre:
            compteur += 1
    return compteur

def jouer_manche(joueur_mot, joueur_devine, mot, max_erreurs):
    """Joue une manche du pendu."""
    erreurs = 0
    lettres_trouvees = ""
    lettres_ratees = ""

    while erreurs < max_erreurs:
        print(f"\nDevine mon mot : {afficher_squelette(mot, lettres_trouvees)}")
        print(f"Tu as droit à {max_erreurs - erreurs} erreur(s) ({lettres_ratees})")

        lettre = demander_lettre(lettres_trouvees + lettres_ratees)

        if lettre in mot:
            lettres_trouvees += lettre
            occurrences = compter_occurrences(mot, lettre)
            print(f"Il y a {occurrences} {lettre}")
        else:
            erreurs += 1
            lettres_ratees += lettre
            print(f"Il n’y a pas de {lettre}")

        if "_" not in afficher_squelette(mot, lettres_trouvees):
            print(f"\nBravo Joueur {joueur_devine} ! Tu as trouvé le mot : {mot}")
            return True

    print(f"\nJoueur {joueur_devine} a perdu\nLe mot était : {mot}")
    return False

def jeu_du_pendu():
    """Gère le jeu du pendu complet en alternant les joueurs."""
    nb_tours = int(input("Combien de tours voulez-vous jouer ? "))
    scores = {1: 0, 2: 0}

    for tour in range(nb_tours):
        print(f"\n--- Tour {tour + 1} ---")
        joueur_mot = 1 if tour % 2 == 0 else 2
        joueur_devine = 2 if joueur_mot == 1 else 1

        mot = demander_mot(joueur_mot)
        max_erreurs = int(input(f"Joueur {joueur_devine}, combien d'erreurs maximum ? "))

        if jouer_manche(joueur_mot, joueur_devine, mot, max_erreurs):
            scores[joueur_devine] += 1
        else:
            scores[joueur_mot] += 1

    print("\n--- Scores finaux ---")
    print(f"Joueur 1 : {scores[1]} victoire(s)")
    print(f"Joueur 2 : {scores[2]} victoire(s)")

    if scores[1] > scores[2]:
        print("Le joueur 1 est le gagnant !")
    elif scores[2] > scores[1]:
        print("Le joueur 2 est le gagnant !")
    else:
        print("Match nul !")

# Lancer le jeu
jeu_du_pendu()
