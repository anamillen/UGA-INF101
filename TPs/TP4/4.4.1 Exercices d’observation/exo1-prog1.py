# TP4
# Exercice 1
# Programme 1
def est_solution(x,a,b,c):
    # Renvoie True si x est solution de 
    # ax^2+bx+c=0
    y=a*x**2+b*x+c
    if y==0:
        rep=True
    else:
        rep=False
    return rep

# prog. principal
rep=est_solution(1,1,-2,1)
print(rep)
print(est_solution(5, 2, -20, 50))
print(est_solution(2.5, 1, 2, 3))



"""
Il y a 3 appels en total

1er appel
Arguments :
x = 1 ; a = 1 ; b = -2 ; c = 1 ; y = 0
rep = True
Return value :
True

2er appel
Arguments : 
x = 5 ; a = 2 ; b = -20 ; c = 50 ; y = 0
rep = True
Return value :
True

3er appel
Arguments : 
x = 2.5 ; a = 1 ; b = 2 ; c = 3 ; y = 14.25
rep = False
Return value :
False
"""
