# Programme DeuxDes.py

# Lire la valeur du premier dé
de1 = int(input("Donner la valeur du premier dé : "))

# Vérifier si la valeur du premier dé est correcte
if 1 <= de1 <= 6:
    print("La valeur du premier dé est correcte")
    
    # Lire la valeur du deuxième dé
    de2 = int(input("Donner la valeur du deuxième dé : "))
    
    # Vérifier si la valeur du deuxième dé est correcte
    if 1 <= de2 <= 6:
        print("La valeur du deuxième dé est correcte")
        
        # Afficher les dés dans l'ordre décroissant
        if de1 > de2:
            print("Les dés classés en ordre décroissant sont :", de1, de2)
        else:
            print("Les dés classés en ordre décroissant sont :", de2, de1)
    else:
        print("La valeur du deuxième dé est incorrecte")
else:
    print("La valeur du premier dé est incorrecte")
