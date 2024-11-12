# on importe les modules necessaires
import doctest
import random

# definitions de fonctions

def choix1(N):
    """Choisit l'indice d'une personne pour la rencontre"""
    return random.randint(0,N-1)

def tirage(N):
    """Renvoie les nombres de 2 choisis aletoirement pour une rencontre"""
    i1 = choix1(N)
    i2 = choix1(N)
    while i1==i2:
        i2 = choix1(N)
    return i1,i2

def rencontre(p1,p2):
    """Simulation d'une rencontre entre p1 et p2"""
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

def change(N, l1, l2):
    """Renvoie les indices de ces elements qui ont change"""
    res = []
    for i in range(N):
        if l1[i]!=l2[i]:
            res.append(i)
    return res


def c_present(li):
    """Verifie s'il y en a des personnes connaissantes la nouvelle"""
    return "C" in li

def jour(N, per_avant):
    """Affiche les changements de chaque jour"""
    n1, n2 = tirage(N)
    print(str(n1)+",",n2,"\t\t", per_avant[n1], per_avant[n2], end = "\t")
    per_apres = list(per_avant)
    
    per_apres[n1],
    per_apres[n1], per_apres[n2] = rencontre(per_avant[n1], per_avant[n2])
    changement = change(N, per_avant, per_apres)

    for i in range(N):
        if i in changement:
            print(str(per_apres[i]).rjust(0), end="     ")
        else:
            print("-".rjust(0), end="     ")

    return per_apres




def simulation(N):
    personnes = ["C"]+["I"]*(N-1)
    jour_decompt = 0
    while c_present(personnes):
        print(str(jour_decompt).rjust(3), end="\t  ")
        personnes = jour(N, personnes)
        jour_decompt+=1
        print()
    # a partir d'ici l n'y a pas de personnes "C" parmis toutes les personnes
    return


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


N = 5

header(N)
simulation(N)

