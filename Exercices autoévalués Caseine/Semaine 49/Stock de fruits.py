def ajoute1(stock, nom):
    """Prend en argument un stock (dictionnaire) et un nom de fruit, 
    et renvoie le nouveau stock, dans lequel un fruit du type donné a été ajouté.
    """
    new_stock = dict(stock)
    if nom in stock :
        new_stock[nom]+=1
    else : # si le nom de la fruit n'est pas encore  
        new_stock[nom]=1
    return new_stock
    
def enleve1(stock, nom):
    """Prend en argument un stock (dictionnaire) et un nom de fruit, 
    et renvoie le nouveau stock, où un fruit du type donné a été enlevé (s'il y avait un stock suffisant). 
    Si le stock de ce fruit tombe à zéro, on enleve la clé du dictionnaire. 
    Si le stock n'était pas suffisant, le programme affichera Erreur et renverra le stock initial non modifié. 
    """
    new_stock = dict(stock)
    if nom in stock:
        new_stock[nom]-=1
        if new_stock[nom]==0:
            del new_stock[nom]
    else:  # si le fruit n'est pas present alors
        print("Erreur: quantité insuffisante de", nom)
    return new_stock
        
def ajoute(stock, fruit, q):
    """
    Prend en argument un stock (dictionnaire), un nom de fruit et une quantité q, 
    et renvoie le nouveau stock, dans lequel on a ajouté une quantité q du type de fruit précisé. 
    """
    new_stock = dict(stock)
    if fruit in stock:
        new_stock[fruit]+=q
    else:  # si le fruit n'est pas present dans le stock
        new_stock[fruit]=q
    return new_stock
    
def enleve(stock, fruit, q):
    """Prend en argument un stock (dictionnaire), un nom de fruit et une quantité q, 
    et renvoie le nouveau stock où l'on a enlevé la quantité q du type de fruit précisé. 
    De même que pour la fonction enleve1, si le stock de ce fruit tombe à zéro, on enleve la clé du dictionnaire. 
    Si le stock n'était pas suffisant, le programme affichera "Erreur)" et renverra le stock initial non modifié."""
    new_stock = dict(stock)
    insuffisant = False
    if fruit in stock:
        if new_stock[fruit]-q>0:
            new_stock[fruit]-=q
        elif new_stock[fruit]-q==0:
            del new_stock[fruit]
        else:
            insuffisant = True
    
    else:  # si le fruit n'est pas present alors
        insuffisant = True
        
    if insuffisant:
        print("Erreur: quantité insuffisante de", fruit)
    return new_stock

def apres_livraison(stock, livraison):
    """Prend en argument un stock (dictionnaire) ainsi que le contenu de la livraison (représenté aussi par un dictionnaire) 
    et renvoie le nouveau stock après la livraison (sachant que le contenu de la livraison vient augmenter le stock actuel). """
    new_stock = dict(stock)
    for fruit in livraison:
        new_stock = ajoute(new_stock, fruit, livraison[fruit])
    return new_stock
        
def commande(stock, stock_voulu):
    """Prend en argument le stock actuel (dictionnaire) ainsi que le stock minimum voulu (dictionnaire aussi) 
    et renvoie le dictionnaire correspondant à la commande qu'il faut faire pour obtenir le stock voulu. 
    Si le fruit apparaît déjà en quantité suffisante dans le stock actuel (supérieure ou égal au stock voulu), 
    il ne va pas apparaître dans la commande. """
    a_commander = dict(stock_voulu)
    
    for fruit in stock_voulu:
        if fruit in stock:
            a_commander[fruit]-= stock[fruit]
        if a_commander[fruit]<=0:
            del a_commander[fruit]
    return a_commander
    
def total(stock):
    """Prend en argument le stock et renvoie le nombre total de fruits présents dans le stock"""
    total_count = 0
    for fruit in stock:
        total_count+=stock[fruit]
    return total_count
    
def quantite(stock, fruits_a_compter):
    """Prend en argument le stock ainsi qu'une liste de noms de fruits fruits_a_compter, 
    et renvoie la quantité de fruits présents dans le stock dont le nom est dans la liste fruits_a_compter."""
    total = 0
    for fruit in fruits_a_compter:
        if fruit in stock:
            total+=stock[fruit]
    return total
    
def quantite_agrumes(stock):
    """Prend en argument le stock et renvoie la quantité d'agrumes présents dans le stock. 
    Seront considérés comme noms d'agrumes: orange, citron, mandarine, clémentine et pamplemousse """
    agrumes = ['orange', 'citron', 'mandarine', 'clementine', 'pamplemousse']
    quantite = 0
    for agrume in agrumes:
        if agrume in stock:
            quantite+=stock[agrume]
    return quantite