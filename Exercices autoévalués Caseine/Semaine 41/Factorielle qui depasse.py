"""
Écrire une fonction depasse qui prend en argument un entier A et qui renvoie le plus petit entier n 
tel que n! soit supérieur ou égal à A. 

Par exemple, depasse(120) renvoie 5 car 5!=120. De même, depasse(20) renvoie 4 car 3!=6 mais 4!=24.

(Exercice proposé par Aurélie Lagoutte)
"""


def depasse(A):
    """Prend en argument un entier A et renvoie le plus petit entier n 
    tel que n! soit supérieur ou égal à A"""
    fact = 1
    n = 0
    while fact<A:
        n+=1
        fact*=n
    return n

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")