
# definitions des fonctions
def valeur_abs(x):
    """Prend en argument un nombre x et qui renvoie sa valeur absolue
    """
    if x<0:
        x = -x
    return x
    
def signe_different(x,y):
    """Prend en arguments deux nombres x et y et renvoie True
    si x et y ont des signes différents, False sinon"""
    
    res = False
    if x*y<0:
        res = True
    return res
    
def f(x):
    """Soit f la fonction mathématique définie sur R par f (x) = 3x^2 + 2x + 3. 
    La fonction prend en argument un réel x et renvoie la valeur de f(x)."""
    A = 3; B = 2; C = 3
    y = A*x**2 + B*x + C
    return y
    
def nb_racines(a,b,c):
    """Prend en argument trois réels a, b, c et renvoie le nombre de racines réelles du polynôme ax^2 + bx + c."""
    delta = b**2 - 4*a*c
    n_sol = 2
    if delta < 0:
        n_sol = 0
    elif delta==0:
        n_sol = 1
    return n_sol
        
    
        



# Programme principal
if __name__=='__main__': # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")



