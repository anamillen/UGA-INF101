"""1) Ecrire une fonction factorielle qui prend en argument un entier naturel n et qui renvoie la valeur de n!.

Rappel: n!=1 × 2× ... n

2) Ecrire une fonction coeff_binomial qui prendre en argument deux entiers naturels n et k (avec k≤n) et 
qui renvoie la valeur du coefficient binomial correspondant "k parmi n", donnée par le formule ci-dessous:

(nk)=n!(n−k)! k!

3) Ecrire une fonction triangle_pascal qui prend en argument un entier nb_lignes et qui affiche le triangle de Pascal
 (voir définition ci-dessous) en s'arrêtant au bout du nombre de lignes indiqué par l'argument. 
 """

# definitions de fonctions
def factorielle(n):
    """Prend en argument un entier naturel n et renvoie la valeur de n!"""
    facto = 1
    for i in range(2, n+1):  # on ajuste les bornes pour pas multiplier par 0 et multiplier par n, on evite aussi multiplication par 1
        facto*=i
    return facto
    
def coeff_binomial(n,k):
    """Prend en argument deux entiers naturels n et k (avec k≤n) et renvoie la valeur du coefficient binomial correspondant "k parmi n",
    donnée par le formule suivant : (n k)= n!/((n−k)!*k!)"""
    res = factorielle(n)/(factorielle(n-k)*factorielle(k))
    return res
    
def triangle_pascal(nb_lignes):
    """Prend en argument un entier nb_lignes et affiche le triangle de Pascalen s'arrêtant au bout du nombre de lignes indiqué par l'argument."""
    for n in range(nb_lignes):
        for k in range(n+1):
            coeff = int(coeff_binomial(n,k))
            print(coeff, end=" ")
        print()
        
        


        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")