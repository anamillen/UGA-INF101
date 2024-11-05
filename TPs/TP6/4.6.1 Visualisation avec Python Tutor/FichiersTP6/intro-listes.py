def parcours (liste):
    i = 0
    while i < len(liste):
        print ("Element a l'indice", i, ":", liste[i])
        i = i+1

def parcours_envers (liste):
    i = len(liste)-1
    while i >= 0:
        print ("Element a l'indice", i, "(envers) :", liste[i])
        i = i-1
        
def croissante (liste):
    crois = True
    i = 1
    while i < len(liste):
        if liste[i-1] > liste[i] :
            crois = False
        i = i+1
    return crois

# programme principal
liste_desord = [2, 12, 7, 9, 3, 4]
liste_croiss = [2, 3, 4, 5, 7, 9, 12]

parcours(liste_desord)

parcours_envers(liste_desord)

print (liste_desord, "est croissante :", croissante(liste_desord))
print (liste_croiss, "est croissante :", croissante(liste_croiss))



maliste = [1, 3, 9, 6, 4, 10]
maliste[5] = 12
print(maliste)
maliste.pop()
maliste[5] = 12    # Affiche Index error
maliste0[5] =12    # Affiche Name error