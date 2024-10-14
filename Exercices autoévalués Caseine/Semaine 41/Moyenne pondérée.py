"""
Écrire une fonction moyenne_ponderee qui prend en arguments quatre nombres 
que l’on appellera note1, note2, coeff1 et coeff2 et qui calcule 
la moyenne pondérée de note1 et note2, ayant pour coefficients respectifs coeff1 et coeff2.

(Exercice proposé par Aurélie Lagoutte)
"""



def moyenne_ponderee(n1,n2,c1,c2):
    """prend en arguments quatre nombres 
    que l’on appellera note1, note2, coeff1 et coeff2 et qui calcule 
    la moyenne pondérée de note1 et note2"""
    n_arg = c1+c2
    moyenne = (n1*c1)+(n2*c2)
    return moyenne/n_arg


        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")






