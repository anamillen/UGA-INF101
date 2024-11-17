import random

def c_present(li):
    """Verifie s'il y en a des personnes connaissantes la nouvelle"""
    return "C" in li

def initialisation(N):
    """Initialise l'état initial avec la personne 0 connaissant la nouvelle."""
    return ["C"] + ["I"] * (N - 1)

def choix_personne(N):
    """Renvoie l'indice d'une personne choisie au hasard."""
    return random.randint(0, N - 1)

def tirage(N):
    """Renvoie deux indices distincts de personnes choisies au hasard."""
    i1 = choix_personne(N)
    i2 = choix_personne(N)
    while i1 == i2:     # Assure que les indices soient différents.
        i2 = choix_personne(N)
    return i1, i2

def rencontre(p1, p2):
    """Retourne les nouveaux statuts de deux personnes après une rencontre."""
    pp = [p1,p2]
    if c_present(pp):       # Si au moins une personne connaît la nouvelle
        if p1==p2:          # Les deux personnes ont le même statut
            p1,p2 = "M","M"
        else:               # Statuts différents
            if "M" in pp:   # Si l'une des personnes est muette
                p1,p2 = "M","M"
            else:           # Sinon l'autre personne apprend la nouvelle
                p1,p2 = "C","C"
    return p1, p2

def modification_statuts(n1, n2, personnes):
    """Applique une rencontre et retourne la nouvelle liste de statuts."""
    personnes_modifiees = list(personnes)   # Copie de la liste initiale
    p1, p2 = personnes[n1], personnes[n2]
    personnes_modifiees[n1], personnes_modifiees[n2] = rencontre(p1, p2)
    return personnes_modifiees

def afficher_entete(N):
    """Affiche l'entête du tableau de simulation."""
    print("jour".ljust(5), "rencontre".ljust(10), "nature".ljust(10), end="")
    for i in range(N):
        print(("st."+str(i)).ljust(5), end="")
    print()

def afficher_etat(jour, n1, n2, personnes_avant, personnes_apres):
    """Affiche l'état de la simulation pour un jour donné."""
    ind = str(n1)+", "+str(n2)
    nature = personnes_avant[n1]+", "+personnes_avant[n2]
    print(str(jour).ljust(6), ind.ljust(10), nature.ljust(10), end="")
    for i in range(len(personnes_apres)):
        if personnes_avant[i] != personnes_apres[i]:    # Affiche uniquement si le statut a changé
            print(personnes_apres[i].ljust(5), end="")
        else:
            print("-".ljust(5), end="")     # Sinon, affiche un tiret
    print()

def simulation_globale(N):
    """Simule la propagation d'une nouvelle dans une population en affichant les resultats."""
    personnes = initialisation(N)
    jour_decompt = 1
    while c_present(personnes):     # Continue tant qu'il reste des personnes avec le statut 'C'
        n1, n2 = tirage(N)
        personnes_apres = modification_statuts(n1, n2, personnes)
        personnes = personnes_apres
        jour_decompt += 1
    
    # Résumé final
    print()
    print("Le nombre de jours qu’a duré la propagation de la nouvelle :", jour_decompt)
    print("Nombre d’ignorants :", personnes.count("I"))

def lancages_successifs(N, NS):
    """Lance successivement NS simulations
    avec N personnes"""
    for _ in range(NS):
        simulation_globale(N)


# Programme principal
# saisie par l'utilisateur du numero de lancages

NS = int(input("Entrez le numero de simulations a effectuer : "))
# N = int(input("Entrez le numero de personnes: "))
N = 100
lancages_successifs(N, NS)