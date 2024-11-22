import random
import matplotlib.pyplot as plt

# definitions de fonctions
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
    while i1 == i2:  # Assure que les indices soient différents.
        i2 = choix_personne(N)
    # A partir d'ici i1!=i2
    return i1, i2

def rencontre(p1, p2):
    """Retourne les nouveaux statuts de deux personnes après une rencontre."""
    pp = [p1, p2]
    if c_present(pp):  # Si au moins une personne connaît la nouvelle
        if p1 == p2:  # Les deux personnes ont le même statut
            p1, p2 = "M", "M"
        else:  # statuts différents
            if "M" in pp:  # si l'une des personnes est muette
                p1, p2 = "M", "M"
            else:  # sinon l'autre personne apprend la nouvelle
                p1, p2 = "C", "C"
    return p1, p2

def modification_statuts(n1, n2, personnes):
    """Applique une rencontre et retourne la nouvelle liste de statuts."""
    personnes_modifiees = list(personnes)
    p1, p2 = personnes[n1], personnes[n2]
    personnes_modifiees[n1], personnes_modifiees[n2] = rencontre(p1, p2)
    return personnes_modifiees

def compter_status(li, stat):
    """Compte le nombre de personnes avec statut choisi"""
    return li.count(stat)

def compte_repartition(personnes):
    """Compte la repartition sous la forme correcte pour la representation"""
    labels = ["Connaisseurs", "Ignorants", "Muets"]
    NC = compter_status(personnes, "C")
    NM = compter_status(personnes, "M")
    NI = compter_status(personnes, "I")
    data = [NC, NI, NM]
    return labels, data

def afficher_repartition(personnes):
    """Affiche pour chaque rencontre une suite de caractères représentant la répartition
    de la population en connaisseurs, muets et ignorants.
    ’#’ - les connaisseurs
    ’*’ - les muets
    ’.’ - les ignorants."""
    NC = compter_status(personnes, "C")
    NM = compter_status(personnes, "M")
    NI = compter_status(personnes, "I")
    res = "#" * NC + "*" * NM + "." * NI
    return res

def afficher_entete(N):
    """Affiche l'entête du tableau de simulation."""
    print("jour".ljust(5), "rencontre".ljust(10), "nature".ljust(10), end="")
    for i in range(N):
        print(("st." + str(i)).ljust(5), end="")
    print("repartition".ljust(5))

def afficher_jour_0(jour, personnes):
    """Affiche les conditions initiales de la simulations"""
    print("0".ljust(5), "".ljust(22), end="")
    for personne in personnes:
        print(personne.ljust(5), end="")
    print(afficher_repartition(personnes))

def afficher_etat(jour, n1, n2, personnes_avant, personnes_apres):
    """Affiche l'état de la simulation pour un jour donné."""
    ind = str(n1) + ", " + str(n2)
    nature = personnes_avant[n1] + ", " + personnes_avant[n2]
    print(str(jour).ljust(6), ind.ljust(10), nature.ljust(10), end="")
    for i in range(len(personnes_apres)):
        if personnes_avant[i] != personnes_apres[i]:  # affiche uniquement si le statut a change
            print(personnes_apres[i].ljust(5), end="")
        else:    # si le statut n'a pas change, affiche un tiret
            print("-".ljust(5), end="")
    print(afficher_repartition(personnes_apres))

def affiche_camembert(personnes):
    """Affiche le graphique Camembert pour la repartition de personnes de la liste
    personnes par leur statut"""
    labels, data = compte_repartition(personnes)
    while 0 in data:
        ind = data.index(0)
        data.remove(0)
        labels.pop(ind)
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, labeldistance=.6)
    plt.show()

def simulation_en_detail(N):
    """Simule la propagation d'une nouvelle dans une population en affichant les étapes."""
    personnes = initialisation(N)
    afficher_entete(N)
    jour_decompt = 0
    while c_present(personnes):  # continue tant qu'il reste des personnes avec le statut 'C'
        if jour_decompt == 0:
            afficher_jour_0(jour_decompt, personnes)
        else:  # s'il n'est pas le jour 0
            n1, n2 = tirage(N)
            personnes_apres = modification_statuts(n1, n2, personnes)
            afficher_etat(jour_decompt, n1, n2, personnes, personnes_apres)
            personnes = personnes_apres
        jour_decompt += 1
        affiche_camembert(personnes)
    # a partir d'ici il n'y a pas de connaiseurs

    # resume final
    print("\nNombre d’ignorants :", compter_status(personnes, "I"))
    print("Nombre de muets :", compter_status(personnes, "M"))


# programme principal pour tester
N = 20  # taille de la population
simulation_en_detail(N)

