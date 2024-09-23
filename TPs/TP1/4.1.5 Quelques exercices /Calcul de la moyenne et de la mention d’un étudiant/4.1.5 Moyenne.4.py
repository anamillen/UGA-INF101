INCOR = "INCORRECT"

# demande à l'utilisateur d'entrer la note de chimie
chim = int(input())
if 0<=chim<=20:
    # demande à l'utilisateur d'entrer la note de physique
    phy = int(input())
    if 0<=phy<=20:
        # demande à l'utilisateur d'entrer la note de mathématiques
        math = int(input())
        if 0<=math<=20:
            # demande à l'utilisateur d'entrer la note d'informatique
            info = int(input())
            if 0<=info<=20:
                # calcule la moyenne pondérée des notes
                moyenne = (chim*3+phy*4+math*2+info*2)/11
                # affiche la moyenne arrondie à deux décimales
                print(round(moyenne,2))
                print("Votre mention est :",end=" ")
                # détermine la mention en fonction de la moyenne
                if moyenne <10:
                    print("Ajourne")
                elif moyenne<12:
                    print("Passable")
                elif moyenne<14:
                    print("Assez bien")
                elif moyenne<16:
                    print("Bien")
                else:
                    print("Tres bien")
            else:
                print("INCOR")
        else:
            print(INCOR)
    else:
        print(INCOR)
else:
    print(INCOR)




