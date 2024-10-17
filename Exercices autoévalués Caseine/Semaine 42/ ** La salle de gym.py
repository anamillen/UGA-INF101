"""Alain vient d'ouvrir un club de gym en 2017 et il a déjà 100 adhérents. D'après ses pronostics, 
le nombre d'adhérents devrait augmenter de 8% par an. Ecrire un programme pour aider Alain dans ses prévisions de nombre d'adhérents, 
en suivant le cahier des charges décrit ci-dessous.

Le nombre d'adhérents chaque année sera arrondi à l'entier le plus proche grâce à la fonction round(...). Par exemple, round(6.8) vaut 7.

Lorsqu'Alain lance l'application, le menu suivant doit s'afficher:
Menu, veuillez choisir:
1. Prévisions adhérents à l'année N (resumé)
2. Prévisions adhérents à l'année N (détails)
3. Adhésions cumulées à l'année N
4. Année à laquelle on obtiendra M adhérents
Q. Quitter

Si Alain tape 1, le programme lui affiche Choisissez une année : puis le nombre d'adhérents qu'il y aura à l'année choisie, 
par exemple si Alain tape 2018, le programme doit afficher En 2018 il y aura 108 adherents. Ensuite, le programme doit ré-afficher le menu.

Si Alain tape 2, le programme lui affiche Choisissez une année : puis le détail des nombres d'adhérents prévus de l'année 2017 à l'année choisie.
 Par exemple si Alain tape 2019, le programme doit afficher:
En 2017 il y a 100 adherents.
En 2018 il y aura 108 adherents.
En 2019 il y aura 117 adherents.
Ensuite, le programme doit ré-afficher le menu.
Si l'année choisie est inférieure ou égale à 2017, seule la ligne En 2017 il y a 100 adherents. doit s'afficher.

Si Alain tape 3, le programme lui affiche Choisissez une année : puis le nombres d'adhésions cumulées entre l'année 2017 
et l'année choisie (car chaque adhérent doit renouveler son adhésion chaque année). Par exemple si Alain tape 2019, 
le programme doit afficher De 2017 à 2019 il y aura 325 adhésions cumulées. (c'est la somme des nombres affichés dans le choix 2 du menu).
 Ensuite, le programme doit ré-afficher le menu.

Si Alain tape 4, le programme lui affiche Entrez le nombre d'adherents voulus : puis l'année à partir de laquelle ce nombre d'adhérents sera atteint.
 Par exemple si Alain tape 115, le programme doit afficher On atteindra 115 adhérents en 2019. Ensuite, le programme doit ré-afficher le menu.

Si Alain tape Q, le programme lui affiche Au revoir. et s'arrête.

Si Alain tape autre chose que 1, 2, 3, 4 ou Q, le programme doit lui répondre Choix invalide, recommencez : 
(sans ré-afficher le menu) et recommencer à lui afficher cette phrase jusqu'à ce que son choix devienne valide."""

# definitions de fonctions
def prevision_prochaine(INIT,AUG):
    """Calcule les adherents a la prochaine annee a partir de nombre initial d'adherents INIT et taux d'accroissement AUG"""
    res = INIT+INIT*AUG
    return round(res)

def prevision_annee_resume(N0, INIT,AUG,N1):
    """Calcule les adherents pour l'annee N1 a partir de nombre d'adherents INIT en annee N0 et taux d'acroissement AUG, affiche le nombre d'adherents en resume"""
    # definitions de constantes
    res = INIT
    delta = N1-N0
    # on calcule le nombre d'adherents pour chaque prochaine annee
    for _ in range(delta):
        res = prevision_prochaine(res,AUG)
    print("En",N1,"il y aura",res,"adherents.")
    
def prevision_annee_details(N0, INIT,AUG,N1):
    """Calcule les adherents pour l'annee N1 a partir de nombre d'adherents INIT en annee N0 et taux d'acroissement AUG, affiche en details chaque annee"""
    print("En",N0,"il y a",INIT,"adherents.")
    res = INIT
    delta = N1-N0
    
    for i in range(1,delta+1):
        res = prevision_prochaine(res,AUG)
        print("En",N0+i,"il y aura",res,"adherents.")
        
def adhesions_cumulees(N0, INIT,AUG,N1):
    """Affiche le nombre d'adhesions cumulees a partir de N0 a N1"""
    res = INIT
    delta = N1-N0
    somme = INIT
    for i in range(1,delta+1):
        res = prevision_prochaine(res,AUG)
        somme+=res
    print("De",N0,"a",N1,"il y aura",somme,"adhesions cumulees.")
    
def annee_but_dadherents(N0, INIT,AUG,ADH_N):
    """Affiche l'annee quand le nombre souhaitee d'adherents ADH_N sera atteint a partir d'annee N0 et de nombre INITd'adherents et taux d'accroissement AUG"""
    delta = 0; res = INIT
    while res<ADH_N:
        res = prevision_prochaine(res,AUG)
        delta+=1
    print("On atteindra",ADH_N,"adherents en",N0+delta,".")
    
    
        
def menu():
    """Le menu principal pour l'util s'affiche jusqu'a qu'il decide d'arreter le programme"""
    # definitions de constantes
    MSG_INIT = "Menu, veuillez choisir:"
    MSG_OPT1 = "1. Prévisions adhérents à l'année N (resumé)"
    MSG_OPT2 = "2. Prévisions adhérents à l'année N (détails)"
    MSG_OPT3 = "3. Adhésions cumulées à l'année N"
    MSG_OPT4 = "4. Année à laquelle on obtiendra M adhérents"
    MSG_QUIT = "Q. Quitter"
    MSG_ERR = "Choix invalide, recommencez : "
    
    # l'affichage du menu principal
    reponse = ""
    while reponse!="Q":
        print(MSG_INIT,MSG_OPT1,MSG_OPT2,MSG_OPT3,MSG_OPT4,MSG_QUIT, sep="\n")
        reponse = input()
        while reponse not in ("1","2","3","4","Q"):
            reponse = input(MSG_ERR)
        choix_doption(reponse)
            
def choix_doption(rep):
    """Choisit la fonction a appeler d'apres la reponse de l'tuilisateur"""
    # definitions de constantes
    MSG_AN = "Choisissez une année : "
    MSG_ADH ="Entrez le nombre d'adherents voulus : "
    MSG_END = "Au revoir."
    N0 = 2017; INIT = 100; AUG = 0.08; 

    if rep=="Q":
        print(MSG_END)
    elif rep in ("1","2","3"):
        annee = int(input(MSG_AN))
        if rep=="1":
            prevision_annee_resume(N0,INIT,AUG, annee)
        elif rep=="2":
            prevision_annee_details(N0, INIT,AUG,annee)
        else:
            adhesions_cumulees(N0, INIT,AUG,annee)
    else:    # si l'option choisie est option 4
        nombre_souhaite = int(input(MSG_ADH))
        annee_but_dadherents(N0, INIT,AUG,nombre_souhaite)
    return
    
    


# programme principal
menu()