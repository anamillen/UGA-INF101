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


"""
L'affichage :

Variables locales de pente : {'xA': 1, 'yA': 1, 'xB': 2, 'yB': 2, 'p': 1.0}
Pente 1:  1.0
Variables locales de pente : {'xA': 0, 'yA': 2, 'xB': 1, 'yB': 4.5, 'p': 2.5}
Pente 2:  2.5

La fonction locals() renvoie les variables locales d'une fonction et leurs valeurs
"""