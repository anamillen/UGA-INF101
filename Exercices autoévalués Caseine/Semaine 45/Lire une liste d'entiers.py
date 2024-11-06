# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


def LireListeEntiers():
    """Permet de lire des entiers positifs ou nuls saisis au clavier.
    La saisie s’arrête lorsque l’on entre un nombre négatif.
    Sans argument"""
    # initialisation de constantes et variables
    MSG = "Element?"
    li = []
    nb = int(input(MSG))
    while nb>=0:
        li.append(nb)
        nb = int(input(MSG))
    # a partir d'ici nb<0    
    return li
    
def LireListeReelsBornes(bmin = 0, bmax = 100):
    """Permet de lire des réels saisis au clavier. 
    La saisie s’arrête lorsque l’utilisateur 
    saisit une valeur en dehors de l’intervalle [bmin ;  bmax]. 
    Par défaut, les valeurs de min et max sont fixées à 0 et 100"""
    MSG = "Element?"
    li = []
    nb = float(input(MSG))
    while bmin<=nb<bmax:
        li.append(nb)
        nb = float(input(MSG))
    # a partir d'ici nb<0    
    return li
    
def minim(li):
    """Renvoie le minimum d'une liste li"""
    if len(li)<1:
        res = None
    else:  # s'il y a au moins 1 element dans la liste li alors
        res = li[0]
        for el in li:
            if el<res: 
                res = el
    return res
    
def maxim(li):
    """Renvoie le maximum d'une liste li"""
    if len(li)<1:
        res = None
    else:  # s'il y a au moins 1 element dans la liste li alors
        res = li[0]
        for el in li:
            if el>res: 
                res = el
    return res
    
def somme(li):
    """Renvoie la somme d'elements de la liste li"""
    res = 0
    for el in li:
        res+=el
    return res
    

def MMSListe(li):
    """Prend en argument une liste li et retourne le minimum, 
    le maximum et la somme de la liste.
    Sans utiliser les fonctions max, min et sum pré-définies. """
    return minim(li), maxim(li), somme(li)
    
    
    

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Tapez ici votre programme principal
    # Respectez bien ce niveau d'identation.
    
    # programme principal
    print(LireListeEntiers())
    li = LireListeReelsBornes()
    minim, maxim, somme = MMSListe(li)
    print(minim, maxim, somme)
    