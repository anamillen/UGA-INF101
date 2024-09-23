# Programme TroisDes.py

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
        
        # Lire la valeur du troisième dé
        de3 = int(input("Donner la valeur du troisième dé : "))
        
        # Vérifier si la valeur du troisième dé est correcte
        if 1 <= de3 <= 6:
            print("La valeur du troisième dé est correcte")
            
            # Afficher les dés dans l'ordre décroissant
            if de1 >= de2 and de1 >= de3:
                if de2 >= de3:
                    print("Les dés classés en ordre décroissant sont :", de1, de2, de3)
                else:
                    print("Les dés classés en ordre décroissant sont :", de1, de3, de2)
            elif de2 >= de1 and de2 >= de3:
                if de1 >= de3:
                    print("Les dés classés en ordre décroissant sont :", de2, de1, de3)
                else:
                    print("Les dés classés en ordre décroissant sont :", de2, de3, de1)
            else:
                if de1 >= de2:
                    print("Les dés classés en ordre décroissant sont :", de3, de1, de2)
                else:
                    print("Les dés classés en ordre décroissant sont :", de3, de2, de1)
            
            # Vérifier si le joueur a gagné
            if (de1 == 4 and de2 == 2 and de3 == 1) or (de1 == 4 and de2 == 1 and de3 == 2) or (de1 == 2 and de2 == 4 and de3 == 1) or (de1 == 2 and de2 == 1 and de3 == 4) or (de1 == 1 and de2 == 4 and de3 == 2) or (de1 == 1 and de2 == 2 and de3 == 4):
                print("Gagné !")
            else:
                print("Perdu !")
        else:
            print("La valeur du troisième dé est incorrecte")
    else:
        print("La valeur du deuxième dé est incorrecte")
else:
    print("La valeur du premier dé est incorrecte")

