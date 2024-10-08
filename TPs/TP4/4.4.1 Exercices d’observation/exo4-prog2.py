# TP 4
# Exercice 4
# Programme 2
def incremente2(a):
    return a+1

# prog. principal
if __name__=="__main__":
    b=1
    b = incremente2(b)
    print(b)
    a=incremente2(b)
    print(a)


"""
La fonction incremente recois b comme argument, le modifie, 
et renvoie le resultat obtenu, alors le b s'incrimente par 1

Le meme est valide pour a global

"""