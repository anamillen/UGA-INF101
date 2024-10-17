"""
Aline envisage d’ouvrir un compte à la banque Argento, mais elle veut d’abord savoir si cela sera rentable. Sur un tel compte, 
les intérêts sont de 5% par an, et la banque prélève un coût fixe annuel de 11 euros. 
Le capital de l’année n + 1 est donc obtenu par la formule un+1 = un × 1.05 − 11, où un désigne le capital à l’année n.

1) Écrire une fonction capital(nb_annees, capital_debut) qui renvoie le capital en euros qu’Aline aurait
 sur un tel compte au bout de nb_annees en plaçant initialement un capital égal à capital_debut (en euros).

2) Écrire une fonction gagne_argent(nb_annees, capital_debut) qui renvoie True si le capital au bout de nb_annees 
sur un tel compte est supérieur ou égal au capital de début.

3) Écrire une fonction capital_debut_min(nb_annees) qui renvoie le capital minimal qu’il faut mettre initialement 
sur le compte pour qu’après nb_annees, il soit supérieur ou égal au capital de début. 
On supposera ici que le capital de début est toujours un entier. Par exemple, capital_debut_min(7) renvoit 220.

(Exercice proposé par Aurélie Lagoutte)
"""

# les definitions des fonctions
def capital(nba,deb):
    """
    Renvoie le capital en euros sur un tel compte au bout
    de nba en plaçant initialement (année 0) un capital égal à deb (en euros).
    """
    # definitions des constantes
    INT = 1.05   # taux d'interet
    COUT = 11    # coût annuel
    # l'initialisation d'un decompteur pour gerer la boucle suivante
    i = 0 
    # boucle sur les années pour accumuler les intérêts et soustraire le coût
    while i<nba:
        deb=deb*INT-COUT
        i+=1
    return deb

def gagne_argent(nba,deb):
    """
    Renvoie un booléen indiquant si le capital au bout de
    nba années sur un tel compte est (ou non) supérieur ou égal au capital de début deb.
    """
    return capital(nba,deb)>=deb

def capital_debut_min(nb_annees):
    """
    Renvoie le capital minimal qu’il faut mettre initialement sur le compte pour qu’après nb_annees,
    il soit supérieur ou égal au capital de début. 
    On supposera ici que le capital de début est toujours un entier.
    """
    i = 0
    cap_min = 0
    # la boucle pour trouver le capital minimum en reversant l'algortihme principal
    while not gagne_argent(nb_annees,cap_min):
        cap_min +=1
    return cap_min

        

        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")