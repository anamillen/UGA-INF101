"""---------L'INITIALISATION------------"""
# définition des messages constants pour l'interface utilisateur
MSG_ENT = "Entrez votre note en "
MSG_CH = "Chimie"
MSG_PH = "Physique"
MSG_MA = "Mathematiques"
MSG_IN = "Informatique"
MSG_CHANCE = "Votre note doit etre comprise entre 0 et 20. Essayez encore une fois :"
MSG_INCOR = "INCORRECT"
MYN = "Votre moyenne est :"
NT = "Votre note est :"
# définition des coefficients pour chaque matière
C_CHI = 3
C_PHY = 4
C_MAT = 2
C_INF = 2

"""---------------LES ENTREES----------------"""
# saisie et validation des notes pour chaque matière
# si la note n'est pas valide (hors de l'intervalle [0, 20]), une seconde chance est donnée
chi = float(input(MSG_ENT+MSG_CH+" : "))
if not (0<=chi<=20):
    chi = float(input(MSG_CHANCE))
phy = float(input(MSG_ENT+MSG_PH+" : "))
if not (0<=phy<=20):
    phy = float(input(MSG_CHANCE))
mat = float(input(MSG_ENT+MSG_MA+" : "))
if not (0<=mat<=20):
    mat = float(input(MSG_CHANCE))
inf = float(input(MSG_ENT+MSG_IN+" : "))
if not (0<=inf<=20):
    inf = float(input(MSG_CHANCE))

"""--------------L'ALGORITHME PRINCIPAL----------------"""
# vérification finale de la validité de toutes les notes
if not (0<=chi<=20 and 0<=phy<=20 and 0<=mat<=20 and 0<=inf<=20):
    print(MSG_INCOR)
else: 
    # calcul de la moyenne pondérée
    s_de_coef = C_CHI+C_PHY+C_INF+C_MAT
    moyenne = (chi*C_CHI+phy*C_PHY+mat*C_MAT+inf*C_INF)/s_de_coef
    print(MYN, round(moyenne,2)) # affichage de la moyenne arrondie à deux décimales
    
    # détermination et affichage de la mention en fonction de la moyenne
    if moyenne <10:
        print(NT,"Ajourne")
    elif moyenne<12:
        print(NT,"Passable")
    elif moyenne < 14:
        print(NT,"Assez bien")
    elif moyenne <16:
        print(NT, "Bien")
    else:
        print(NT, "Tres bien")

