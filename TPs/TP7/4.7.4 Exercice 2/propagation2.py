# on importe les modules necessaires
import random

# definitions de fonctions 
def initialisation(N):
    """Initialise l'etat initial"""
    return ["C"]+["I"]*(N-1)

def choix1(N):
    """Choisit l'indice d'une personne pour la rencontre et le renvoie"""
    return random.randint(0,N-1)

def tirage(N):
    """Renvoie les indices de 2 personnes choisies aletoirement pour une rencontre"""
    i1 = choix1(N)
    i2 = choix1(N)
    while i1==i2:
        i2 = choix1(N)
    return i1,i2

def rencontre(p1,p2):
    """Simulation d'une rencontre entre p1 et p2.
    Renvoie les valeurs obtenues par p1 et p2 apres la rencontre"""
    pp = [p1,p2]
    if c_present(pp):
        if p1==p2:
            p1,p2 = "M","M"
        else:  # si p1 et p2 n'ont pas le meme statut
            if "M" in pp:
                p1,p2 = "M","M"
            else:
                p1,p2 = "C","C"
    return p1, p2

def change_indices(N, l1, l2):
    """Renvoie les indices de ces elements qui ont change stockes dans une liste"""
    res = []
    for i in range(N):
        if l1[i]!=l2[i]:
            res.append(i)
    return res

def c_present(li):
    """Verifie s'il y en a des personnes connaissantes la nouvelle"""
    return "C" in li

def modification(n1, n2, per_avant):
    """Renvoie une liste deja modifiee apres la rencontre"""
    per_apres = list(per_avant)
    per_apres[n1], per_apres[n2] = rencontre(per_avant[n1], per_avant[n2])
    return per_apres

def jour(N, n1, n2, per_avant):
    """Fait les changements de chaque jour"""
    per_apres = modification(n1,n2,per_avant)
    changement = change_indices(N, per_avant, per_apres)
    return per_apres, changement

def compter_ignor(personnes):
    """Compte le nb de personnes ignorantes en personnes"""
    return personnes.count("I")

def compter_muet(personnes):
    """Compte le nb de personnes muettes en personnes"""
    return personnes.count("M")


# les fonctions avec les effets de bord
def paire_choisie_affiche(n1,n2, personnes):
    """Affiche les nombres de personnes choisises et leurs natures"""
    print(str(n1)+",",n2,"\t\t", personnes[n1], personnes[n2], end = "\t")

def changement_affiche(N,changement, personnes):
    """Affiche les changements"""
    for i in range(N):
        if i in changement:
            print(str(personnes[i]).rjust(0), end="     ")
        else:
            print("-".rjust(0), end="     ")

def header(N):
    """Affiche le 'chapeau' de l'affichage"""
    print(
        "jour",
        "rencontre",
        "nature",
        sep="\t",
        end="\t"
    )
    for i in range(N):
        print("st."+str(i),end="  ")
    print()

def msg(personnes):
    """Affiche les derniers messages qui comptent combien il y a de muetes et de ignorants"""
    ignor = compter_ignor(personnes)
    print("Nombre d'ignorants :",ignor)
    print("Nombre de muets :",len(personnes)-ignor)

def simulation(N):
    # initialisation 
    personnes = initialisation(N)
    jour_decompt = 1
    while c_present(personnes):
        n1, n2 = tirage(N)
        personnes, changement = jour(N, n1,n2, personnes)
        jour_decompt+=1
    # a partir d'ici l n'y a pas de personnes "C" parmis toutes les personnes
    print("La propagation a dure",jour_decompt,"jours")
    print("Le nombre d'ignorants restant est :", compter_ignor(personnes))



# programme principal pour tester
N = 10
simulation(N)

