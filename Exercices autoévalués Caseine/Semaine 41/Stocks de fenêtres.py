"""
Laurence doit gérer les stocks d'un entrepôt de fenêtres, 
semaine par semaine. Le stock de la semaine 1 est 1024 fenêtres. 
De plus, elle a réussi à obtenir les prévisions suivantes : 
pendant la semaine n, le nombre de fenêtres qui partent de l'entrepôt
 (en direction des magasins) est 20+n. 
 De plus, si le numéro de semaine est un multiple de 4, 
 alors l'entrepôt reçoit une livraison de 500 fenêtres venant de 
 l'usine de production. Donc le stock de la semaine 1 est 1024, 
 le stock de la semaine 2 est 1024-(20+2)=1002, 
 le stock de la semaine 3 est 1002-(20+3)=979, 
 le stock de la semaine 4 est 979-(20+4)+500=1455, etc.

Cet exercice est dédié à la conception d'un programme 
aidant Laurence dans sa gestion des stocks et 
suivant le cahier des charges décrit ci-dessous.
"""



# definitions de fonctions
def calcul(stock, n):
    "La fonction calcule le stock pour la semaine n"
    # definitions de constantes et variables
    SEM_RESTOCK = 4
    RESTOCK_N = 500
    DEM = 20
    if n!=0 and n%SEM_RESTOCK==0:
        stock = stock-(n+DEM)+RESTOCK_N
    else:
        stock = stock-(n+DEM)
    return stock
        
        
def prevision(stock, n):
    """La fonction affiche les prévisions de stock de la semaine 1 à la semaine n"""
    i = 1
    while i<=n:   # on decompte toutes les semaines jusqu'a la semaine demandee
        print("Semaine",i,":","stock",stock)
        i+=1 # on augmente le decompteur pour la semaine prochaine
        stock = calcul(stock,i)        
    

def stock_max(stock, n):
    """Calcule quel sera le stock maximal entre la semaine 1 et la semaine n
    (et indique à quelle semaine ce stock maximal sera atteint)."""
    # definitions de variables
    i = 1
    stock_max = stock
    sem_max = 1

    while i<=n:   # on decompte toutes les semaines jusqu'a la semaine demandee
        if stock>stock_max:
            stock_max = stock
            sem_max = i
        i+=1 # on augmente le decompteur pour la semaine prochaine
        stock = calcul(stock, i)
    print("Stock max egal a", stock_max,"atteint en semaine",sem_max)
    
       
def err():
    """Si l'utilisateur tape autre chose que a, b ou q , le programme lui affiche un message d'erreur 
    Choix incorrect, recommencez,"""
    # def de constantes
    MSG_ERR = "Choix incorrect, recommencez "

    return MSG_ERR
    
# programme principal

# definitions de constantes
OPT_A = "a. Previsions de stock"
OPT_B = "b. Stock maximal"
OPT_Q = "(q pour quitter)"
N_SEM = "Choisissez une semaine : "
STCK_INIT = 1024

util_input = ""

while util_input!="q":
    print(OPT_A,OPT_B,OPT_Q, sep = "\n")
    util_input = input()
    while util_input not in ("a","b","q"):
        util_input = input(err())
    if util_input=="a":
        n = int(input(N_SEM))
        prevision(STCK_INIT, n)
    elif util_input=="b":
        n = int(input(N_SEM))
        stock_max(STCK_INIT, n)
        
        
    