maliste = [[1], [3], [9], [6], [4]]

print(maliste)

i = 0
while i < len(maliste):
    element = maliste[i]
    print ("indice", i, " contient: ", element)
    i = i+1

print("Avant:", maliste)
maliste[3]=maliste[2]
maliste[2].append(0)
print("Apres:", maliste)
