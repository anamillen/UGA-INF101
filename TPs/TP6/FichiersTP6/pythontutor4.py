def incremente(i):
    i = i+1


def incr_liste(liste):
    i = 0
    while i < len(liste):
        liste[i] = liste[i] + 1
        i = i+1


x = 12
maliste = [1, 3, 9, 6, 4]

incremente(x)
incr_liste(maliste)


print(x)
print(maliste)

