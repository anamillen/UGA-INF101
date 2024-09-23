INCOR = "INCORRECT"
chim = int(input())
if 0<=chim<=20:
    phy = int(input())
    if 0<=phy<=20: 
        math = int(input())
        if 0<=math<=20:
            info = int(input())
            if 0<=info<=20:
                moyenne = (chim*3+phy*4+math*2+info*2)/11
                print(round(moyenne,2))
                print("Votre mention est :",end=" ")
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




