# TP4
# Exercice 1
# Programme 2
def distance(xA,yA,xB,yB):
    # renvoie la distance entre (xA,yA) et (xB,yB)
    d=(xB-xA)**2+(yB-yA)**2
    d=d**(1/2)
    return d

def appartient_cercle(xA,yA,rayon):
    # teste si le point (xA,yA) appartient
    # au cercle de rayon r centré à l'origine
    if distance(0,0,xA,yA)==rayon:
        return True
    else:
        return False

# prog. principal
d=distance(1,2,2,1)
print(d)
rep=appartient_cercle(1,1,2)
print(rep)
print(appartient_cercle(1,0,1))

"""
distance(...) :
Il y a 3 appels en total

1er appel
Arguments :
xA = 1 ; yA = 2 ; xB = 2 ; yB = 1 ; 
d = 2; d = 1.4142

Return value :
1.4142

2eme appel
Arguments :
xA = 0 ; yA = 0 ; xB = 1 ; yB = 1 ; 
d = 2; d = 1.4142

Return value :
1.4142

2eme appel
Arguments :
xA = 0 ; yA = 0 ; xB = 1 ; yB = 0 ; 
d = 1; d = 1.0

Return value :
1.0

---------------------------------------------------------

appartient_cercle(...) :
Il y a 2 appels en total

1er appel
Arguments :
xA = 1 ; yA = 1 ; rayon = 2

Return value :
False

2eme appel
Arguments :
xA = 1 ; yA = 0 ; rayon = 1

Return value :
True

"""