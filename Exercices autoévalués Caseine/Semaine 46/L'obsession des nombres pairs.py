# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.






def est_pair(n):
    """Renvoie un boolean indiquant si n est pair"""
    return n%2==0
    
def somme_pairs(li):
    """Prend en argument une liste et renvoie la somme des nombres pairs contenus dans la liste"""
    res = 0
    for el in li:
        if est_pair(el):
            res+=el
    return res
    
def nb_elem_pairs(li):
    """Prend en argument une liste et renvoie le nombre d'entiers pairs contenus dans la liste"""
    res = 0
    for el in li:
        if est_pair(el):
            res+=1
    return res
    
def max_pair(li):
    """Prend en argument une liste et renvoie le plus grand entier pair contenu dans la liste"""
    maxim = 0
    for el in li:
        if el>maxim and est_pair(el):
            maxim = el
    return maxim

def min_pair(li):
    """Prend en argument une liste et renvoie le plus petit entier pair contenu dans la liste"""
    minim = None
    for el in li:
        if est_pair(el):
            if minim==None:
                minim = el
            elif el<minim:
                minim = el
    return minim
    
def indice_de(ent, li):
    """Prend en argument un entier (supposé pair) et une liste, et renvoie l'indice auquel
    apparaît cet entier dans la liste. 
    Si l'entier n'apparaît pas, la fonction renverra None."""
    indice = None; long = len(li); i = 0
    while indice==None and i<long:
        if ent==li[i]: indice = i
        i+=1
    # a partir d'ici soit indice!=None (on a trouve l'indice cherche), soit i==long(li) (on l'a pas trouve et on renvoie None)
    return indice
    
def trouve_premier_pair(li):
    """Prend en argument une liste et renvoie l'entier pair qui apparaît en premier dans la liste. 
    Si la liste ne contient pas d'entier pair, la fonction renverra None."""
    res = None; i = 0; long = len(li)
    while res==None and i<long:
        if est_pair(li[i]): res = li[i]
        i+=1
    # a partir d'ici soit res!=None (on a trouve notre pair), soit i==long (on n'a pas trouve notre pair)
    return res

def extrait_pairs(l1):
    """Prend en argument une liste l1 et renvoie la liste obtenue à partir de l1
    en ne gardant que les entiers pairs (et sans changer leur ordre)."""
    res = []
    for el in l1:
        if est_pair(el):
            res.append(el)
    return res




        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")


## Ci-dessous: copie des exemples
## Pour avoir l'enonce en entier, ouvrez deux fenetres cote-a-cote.
##somme_pairs([4, 7, 12, 0, 21, 5]) vaut 16 (car 16=4+12+0).
##nb_elem_pairs([4, 7, 12, 0, 21, 5]) vaut 3 (car 4, 12 et 0 sont pairs).
##max_pair([4, 7, 12, 0, 21, 5]) vaut 12.
##min_pair([4, 7, 12, 0, 21, 5]) vaut 0
##et min_pair([9, 3, 1]) vaut None.
##indice_de(12, [4, 7, 12, 0, 21, 5]) vaut 2 (car 12 est placé à l'indice 2),
##et indice_de(6, [4, 7, 12, 0, 21, 5]) vaut None.
##trouve_premier_pair([1, 15, 4, 7, 12, 3]) vaut  4
##et trouve_premier_pair([1, 17, 7]) vaut  None.
##extrait_pairs([4, 7, 12, 0, 3]) vaut  [4, 12, 0]
##et extrait_pairs([21, 17, 3]) vaut  [ ].

