"""

        Ecrire une fonction sommeDivPropre qui reçoit un entier naturel n, 
        et calcule et renvoie la somme de ses diviseurs propres (ses diviseurs autres que lui-même).
        Exemples:
            sommeDivPropre(0) renvoie 0
            sommeDivPropre(1) renvoie 0
            sommeDivPropre(4) renvoie 3
            sommeDivPropre(6) renvoie 6

        Un entier naturel est dit parfait s’il est égal à la somme de tous ses diviseurs propres. 
        Ecrire une fonction estParfait qui teste si un entier naturel reçu en paramètre est parfait (en utilisant la fonction précédente).
        Exemples:
            estParfait(6) renvoie True
            estParfait(10) renvoie False

    Ecrire une fonction parfaits_entre qui reçoit deux entiers binf et bsup (optionnels, valeurs par défaut respectivement 2 et 100),
      et affiche tous les nombres parfaits de l’intervalle \texttt{[binf,bsup]}, sur une seule ligne, séparés par un espace. 
      On respectera strictement le modèle des exemples ci-dessous.
    Exemples:

    	 >>> parfaits_entre()
             Nombres parfaits de [2,100]
             6 28
             >>> parfaits_entre(binf=7)
             Nombres parfaits de [7,100]
             28


"""

# definitions de fonctions
def sommeDivPropre(n):
    """Reçoit un entier naturel n, et calcule et renvoie la somme de ses diviseurs propres
    (ses diviseurs autres que lui-même). """
    # definitions de constantes et variables
    somme_divs = 0
    for div_curr in range(1,round(n/2)+1):
        if n%div_curr==0:
            somme_divs+=div_curr
    return somme_divs
    
def estParfait(n):
    """Teste si un entier naturel reçu en paramètre est parfait.
    Un entier naturel est dit parfait s’il est égal à la somme de tous ses diviseurs propres. """
    res = False
    if n==sommeDivPropre(n):
        res = True
    return res
    
def parfaits_entre(binf = 2,bsup = 100):
    """Reçoit deux entiers binf et bsup (optionnels, valeurs par défaut respectivement 2 et 100), 
    et affiche tous les nombres parfaits de l’intervalle [binf,bsup],
    sur une seule ligne, séparés par un espace. """
    MSG = "Nombres parfaits de ["+str(binf)+","+str(bsup)+"]"
    print(MSG)
    for num in range(binf,bsup+1):
        if estParfait(num):
            print(num,end=" ")
    
    

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")