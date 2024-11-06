

def NextElem(elm, liste):
    """
    Prend en argument un élément elm et une liste d’au moins deux éléments liste. 
    Renvoie l’élément suivant elm dans la liste liste, ou le premier élément de la liste si elm est le dernier de liste. 
    Elle renvoie None si elm n’est pas dans liste.
    """
    res = None
    long = len(liste)
    for i in range(long):
        if liste[i]==elm:
            if i+1<long:
                res=liste[i+1]
            else:   # si l'elm est le dernier element de la liste alors
                res=liste[0]
    return res

def encode(txt, ordre):
    """Prend en argument un texte (en minuscule, sans accent) et une liste ordre contenant toutes les lettres minuscules
    et la ponctuation dans un certain ordre (comme ordre_alpha et ordre2 qui vous sont fournis, par exemple) et
    renvoie le texte chiffré, où chaque caractère du texte de départ a été remplacé par son élément suivant dans la liste ordre."""
    chiffre = ""
    for ltr in txt:
        chiffre+=NextElem(ltr, ordre)
    return chiffre


        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    
    ordre1=list("abcdefghijklmnopqrstuvwxyz ,;:!?.")
    ordre2=list("az.erty,uiop:qsdfg!hjklm;wxcv?bn ")




