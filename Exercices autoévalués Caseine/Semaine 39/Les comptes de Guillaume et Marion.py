"""
Guillaume et Marion veulent un petit programme pour gérer leurs comptes bancaires. Ils ont chacun un compte, et veulent recevoir différents messages selon l'état de leur compte et celui de leur conjoint: les deux positifs, ou bien les deux négatifs, ou bien l'un positif et l'autre négatif avec un transfert possible pour rétablir la situation, ou bien l'un positif et l'autre négatif sans transfert possible pour rétablir la situation.

Exemples d'execution :

Exemple 1:

Lancement de la gestion des comptes? *l'utilisateur entre non*
OK. A bientot.

Exemple 2:

Lancement de la gestion des comptes? *l'utilisateur entre oui*
Solde du compte de Guillaume? *l'utilisateur entre 150.5*
Solde du compte de Marion? *l'utilisateur entre 340.12*
Tous les deux en positif!

Exemple 3:

Lancement de la gestion des comptes? *l'utilisateur entre oui*
Solde du compte de Guillaume? *l'utilisateur entre -112*
Solde du compte de Marion? *l'utilisateur entre -240.4*
Tous les deux en négatif!
Impossible de rétablir la situation.

Exemple 4:

Lancement de la gestion des comptes? *l'utilisateur entre oui*
Solde du compte de Guillaume? *l'utilisateur entre 350.87*
Solde du compte de Marion? *l'utilisateur entre -240*
Marion est en négatif.
Guillaume peut lui transférer 240.0 euros (il lui restera 110.87 euros).

Exemple 5:

Lancement de la gestion des comptes? *l'utilisateur entre oui*
Solde du compte de Guillaume? *l'utilisateur entre -270*
Solde du compte de Marion? *l'utilisateur entre 250*
Guillaume est en négatif.
Impossible de rétablir la situation.

 /!\ Lorsque que l'on vous demande d'afficher une phrase à l'écran, vous devez suivre celle de l'exemple à la lettre (seuls les différences de ponctuation, d'espaces, de majuscules, et de certains accents sont tolérées).

(Exercice proposé par Aurélie Lagoutte)s
"""

# l'initialisation des constantes
MSG_INIT = "Lancement de la gestion des comptes?"
MSG_QUIT = "OK. A bientot."
MSG_SOLD = "Solde du compte de"

MSG_1 = "est en"
MSG_2 = "Tous les deux en"
MSG_POS = "positif"
MSG_NEG = "négatif"
MSG_IMP = "Impossible de rétablir la situation."

NOM_G = "Guillaume"
NOM_M = "Marion"


lance = input(MSG_INIT)


if lance=="non":
    print(MSG_QUIT)
    
else:       # si l'utilisateur entre oui alors on lui demande les soldes de ses comptes
    sold_g = float(input(MSG_SOLD+" "+NOM_G+"?"))
    sold_m = float(input(MSG_SOLD+" "+NOM_M+"?"))
    
    if sold_g >=0:
        if sold_m>=0:
            print(MSG_2,MSG_POS,end="!\n")      #tous les deux sont en positif
        else:       # si Guillame est en positif et Marion est en negatif on affiche le message suivant
            print(NOM_M,MSG_1,MSG_NEG,end=".\n")
            
            # on evalue si transfert est possible pour retablir la situation
            if sold_g+sold_m>=0:
                print(NOM_G,"peut lui transférer",-1*sold_m,"euros (il lui restera",sold_g+sold_m,"euros).")
            else:       # il n'y pas suffisament d'argent sur les deux somptes pour retablir la situation
                print(MSG_IMP)
                
    else: # si la solde de Guillame est en negatif alors :
    
        if sold_m<0:  #les deus soldes sont negatives alors
            print(MSG_2,MSG_NEG,end="!\n")      #les deus soldes sont negatives 
            print(MSG_IMP)
        else:       # Guillame est en negatif et Marion est en positif alors :
            print(NOM_G,MSG_1,MSG_NEG,end=".\n")
            
            if sold_g+sold_m>=0:
                print(NOM_M,"peut lui transférer",-1*sold_g,"euros (il lui restera",sold_m+sold_g,"euros).")
            else:       # il n'y pas suffisament d'argent sur les deux somptes pour retablir la situation
                print(MSG_IMP)
            
