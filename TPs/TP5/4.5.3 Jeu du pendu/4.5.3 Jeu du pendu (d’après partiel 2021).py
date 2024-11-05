# definitions de fonctions

def affichage_mot():
    """Affiche les lettres devinees ou tirets"""

def a_gagne():
    """Renvoi le booleen indiquant si le jouer a gagne"""

def n_ess():
    """Calcule le nombre d'erreurs restant"""

def lettre_existe():
    """Verifie si la lettre est present dans le mot"""
# programme principal

# definitions de constantes
MSG_INIT = "Entrez le mot a deviner"
MSG_DEVINE = "Devine mon mot :"
MSG_ERR = "Il vous restent d'erreurs :"

mot_a_deviner = input(MSG_INIT)


"""
while not a_gagne() and n_ess()>0:
    print(MSG_DEVINE, affichage_mot())
    print(MSG_ERR, n_ess)
    lettre_devine = input()
    if lettre_existe():
        affichage_mot(ltr)
        
"""
