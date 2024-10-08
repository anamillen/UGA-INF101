# TP4
# Exercice 3
def pente(xA, yA, xB, yB):
    p=(yB-yA)/(xB-xA)
    print("Variables locales de pente :", locals())
    return p

p1=pente(1,1,2,2)
print("Pente 1: ", p1)
p2=pente(0,2,1,4.5)
print("Pente 2: ", p2)
