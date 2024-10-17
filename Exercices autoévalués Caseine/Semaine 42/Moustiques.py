
# definitions de fonctions
def f(x):
    """Prend en argument le nombre x de moustiques à une certaine année et
    renvoie le nombre de moustiques l’année suivante. 
    La valeur de retour de f s'arrondit à l'entier inférieur."""
    return int(x*1.09 - 200)
    
def nb_moustiques(nb_debut,annee_voulue):
    """Renvoie le nombre de moustiques qu’il y aura en annee_voulue"""
    # definitions de constantes et de variables
    CUR_AN = 2017
    delta = annee_voulue-CUR_AN
    nb_fin = nb_debut
    for _ in range(delta):
        nb_fin=f(nb_fin)
    return nb_fin
    
def annee_atteindra(seuil,nb_debut):
    """Prend en argument un entier seuil et un entier nb_debut (qui correspondra au nombre de moustiques en 2017) et
    renvoie l’année à partir de laquelle le nombre de moustiques sera supérieur ou égal à seuil."""
    nmbr_mstqs = nb_debut
    annee = 2017
    while nmbr_mstqs<seuil:
        nmbr_mstqs=f(nmbr_mstqs)
        annee+=1
    return annee
    

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
