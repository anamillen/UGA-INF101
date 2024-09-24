


"""
-----------------------------------------------------------------------------
i11_Milenkova_BassChervony_4.2.2.2.py : CR « Une IA por le prix du gros lot », groupe IMA_o5_P

Anastasiia Milenkova <Anastasiia.Milenkova@etu.univ-grenoble-alpes.fr>
Daniel Bass Chervony <Daniel.Bass@etu.univ-grenoble-alpes.fr>
-----------------------------------------------------------------------------
""" 


from random import randint      # on importe de module random le methode randint 

# l'initialisation des constantes
MSG_INIT = "Je cherche un nombre entre"
MSG_PROPO = "Je propose "
MSG_GAGNE = "J’ai gagné"
MSG_ESS = "Le nombre d'essais est :"
TIRE = randint(1,100)


#l'initialisation des variables
rep = ""
inf=0
sup=100
n_ess = 0

# le programme essaye de deviner le nombre choisi jusqu'a la reussite
while rep!="b":
    print(MSG_INIT,inf,"et",sup)
    propo = randint(inf,sup)        # le programme choisi un nombre aleatoire entre les deux bornes
    print(MSG_PROPO,propo," ? ",end="")
    n_ess+=1            # on augmente le nombre d'essais
    if propo<TIRE:      # si le nombre devenu est plus petit que le nombre tire alors
        rep="p"
        print(rep)
        inf=propo+1    # l'echange de la borne inferieure
    elif propo>TIRE:    # si le nombre devenu est plus grande que le nombre tire alors
        rep="g"
        print(rep)
        sup=propo-1    # l'echange de la borne superieure
    else:               # si le nombre devenu est egal au nombre choisi alors
        rep="b"
        print(rep)
# quand on sort de la boucle rep="b", le programme a devine le nombre choisi par l'util
print(MSG_GAGNE)
print(MSG_ESS,n_ess)


"""
TEST 1:
Je cherche un nombre entre 0 et 100
Je propose  26  ? p
Je cherche un nombre entre 27 et 100
Je propose  91  ? g
Je cherche un nombre entre 27 et 90
Je propose  90  ? g
Je cherche un nombre entre 27 et 89
Je propose  66  ? p
Je cherche un nombre entre 67 et 89
Je propose  83  ? g
Je cherche un nombre entre 67 et 82
Je propose  81  ? g
Je cherche un nombre entre 67 et 80
Je propose  68  ? p
Je cherche un nombre entre 69 et 80
Je propose  77  ? g
Je cherche un nombre entre 69 et 76
Je propose  70  ? p
Je cherche un nombre entre 71 et 76
Je propose  75  ? g
Je cherche un nombre entre 71 et 74
Je propose  74  ? g
Je cherche un nombre entre 71 et 73
Je propose  73  ? b
J’ai gagné
Le nombre d'essais est : 12
oskorusha@anna-osk-pc:~/Documents/uni/INF101$ ^C
oskorusha@anna-osk-pc:~/Documents/uni/INF101$ ^C

 cd /home/oskorusha/Documents/uni/INF101 ; /usr/bioskorusha@anna-osk-pc:~/Documents/uni/INF101$  cd /home/oskorusha/Documents/uni/INF101 ; /usr/bin/env /bin/python3 /home/oskorusha/.vscode/extensions/ms-python.debugpy-2024.8.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher 57459 -- /home/oskorusha/Documents/uni/INF101/TPs/TP2/4.2.2\ Une\ IA\ pour\ le\ prix\ du\ gros\ lot/4.2.2.2.py 
Je cherche un nombre entre 0 et 100
Je propose  18  ? p
Je cherche un nombre entre 19 et 100
Je propose  33  ? p
Je cherche un nombre entre 34 et 100
Je propose  93  ? g
Je cherche un nombre entre 34 et 92
Je propose  74  ? g
Je cherche un nombre entre 34 et 73
Je propose  62  ? g
Je cherche un nombre entre 34 et 61
Je propose  45  ? p
Je cherche un nombre entre 46 et 61
Je propose  56  ? p
Je cherche un nombre entre 57 et 61
Je propose  58  ? p
Je cherche un nombre entre 59 et 61
Je propose  61  ? b
J’ai gagné
Le nombre d'essais est : 9

"""