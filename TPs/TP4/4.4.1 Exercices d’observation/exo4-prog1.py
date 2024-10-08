# TP 4
# Exercice 4
# Programme 1
def incremente (a):
    a = a+1

# prog. principal
if __name__=="__main__":
    b=3
    incremente(b)
    print (b)
    a=5
    incremente(a)
    print (a)


"""
La fonction incremente recois b comme argument, le modifie, 
mais ne renvoie pas le resultat obtenu, alors le b global reste le meme

Le meme est valdie pour a global


Si dans le programme principal on ajoute
a = incremente(a)
Alors a sera egal au None, comme icnremente(...) ne renvoie aucune valeur
"""