# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


# definitions de fonctions

def carte_valide(nom_carte):
    """Vérifie si la carte saisie est une carte valide"""
    TARIFS = {"Jeune":50, "Senior":60}
    return nom_carte in TARIFS
    
def trajet_existant(ville_depart, ville_arrivee):
    """Vérifie si le trajet saisi est un trajet existant"""
    TRAJETS = {
        "Grenoble": {
            "Lyon": 20,
            "Paris": 100
        },
        "Paris": {
            "Grenoble": 100,
            "Lyon": 80
        }, 
        "Lyon": {
            "Grenoble": 20,
            "Paris": 80
        }
    }
    return ville_depart in TRAJETS and ville_arrivee in TRAJETS[ville_depart]

def prix_nonmod():
    """Renvoie le prix avec la réduction pour les billets nonmodifiables"""
    RED = 0.1
    return RED
    
def red_selon_periode(periode, carte):
    """Renvoie le prix avec la réduction appliquée selon la période"""
    red = 0
    if periode=="bleue":
        red = 0.5
    elif periode=="blanche":
        if carte=="Jeune":
            red = 0.3
        elif carte=="Senior":
            red = 0.25
    return red
        
    

def tarif_carte(nom_carte):
    """Prend en argument une chaîne correspondant au nom de la carte ("Jeune" ou "Senior") et
    renvoie le prix de la carte.
    Si un autre nom que "Jeune" ou "Senior" est utilisé, 
    la fonction affichera "Carte inconnue" et ne renverra rien"""
    # definitions de constantes et de variables
    MSG_ERR = "Carte inconnue"
    TARIFS = {"Jeune":50, "Senior":60}
    prix = None
    if carte_valide(nom_carte):
        prix = TARIFS[nom_carte]
    else : # si le nom de la carte saisi ne correspond à aucun tarif existant alors
        print(MSG_ERR)
    return prix
        
def plein_tarif(ville_depart, ville_arrivee):
    """Prend en argument deux chaînes correspondant respectivement à la ville de départ de la ville d'arrivée
    renvoie le prix d'un billet plein tarif sur ce trajet-là. 
    Si le trajet demandé n'est aucun des 6 trajets, 
    la fonction affichera "Trajet inconnu" et renverra None."""
    # definitions de constantes et de variables
    TRAJETS = {
        "Grenoble": {
            "Lyon": 20,
            "Paris": 100
        },
        "Paris": {
            "Grenoble": 100,
            "Lyon": 80
        }, 
        "Lyon": {
            "Grenoble": 20,
            "Paris": 80
        }
    }
    prix = None
    MSG_ERR = "Trajet inconnu"
     # si le trajet demandé existe alors
    if trajet_existant(ville_depart, ville_arrivee):
        prix = TRAJETS[ville_depart][ville_arrivee]
    else: # si le trajet demandé n'existe pas alors
        print(MSG_ERR)
        
    return prix

def tarif_billet(ville_depart, ville_arrivee, modifiable = True, carte = None, periode = None):
    """Prend en argument la ville de départ, la ville d'arrivée et 3 arguments optionnels : 
    - un booléen modifiable indiquant si le billet est modifiable (True par défaut)
    - un argument carte correspondant au nom de l'éventuelle carte de réduction (None par défaut; pourra valoir "Jeune" ou "Senior")
    - un argument periode  (None par défaut; pourra valoir "bleue" ou "blanche"=). 
    La fonction renvoie le tarif du billet correspondant. 
    Si le trajet ou la carte demandé(e) est inconnu(e), un message d'erreur s'affiche et la fonction renvoie None."""
    MSG_ERR = "Carte ou trajet inconnu(e) "
    total = None
    if trajet_existant(ville_depart, ville_arrivee) and (carte_valide(carte) or carte==None):
        total = plein_tarif(ville_depart, ville_arrivee)
        red = 0
        if carte!=None:
            red += red_selon_periode(periode, carte)
        elif not modifiable:
            red += prix_nonmod()
            
        total -= total*red
    else:
        print(MSG_ERR)
    return total
    
def prix_client():
    """Renvoie le prix total de la commande du client"""
    MSG_CARTE = "Voulez-vous acheter une carte de réduction ? (oui/non) "
    MSG_BILLET = "Voulez-vous acheter un billet ? (oui/non) "
    MSG_PERIODE = "Precisez la periode (bleue/blanche) : "
    nom_carte = None
    modifiable = True
    periode = None
    achete_carte = input(MSG_CARTE)
    prix_total = 0
    red = 0
    if achete_carte == 'oui':
        nom_carte = input("Choisissez votre carte : (Jeune/Senior) ")
        prix_carte = tarif_carte(nom_carte)
        if prix_carte!= None:
            prix_total += prix_carte
    achete_billet = input(MSG_BILLET)
    if achete_billet == "oui":
        ville_depart = input("Depart : ")
        ville_arrivee = input("Destination : ")
        if achete_carte == "oui":
            print("Vous avez une carte de réduction")
            periode = input(MSG_PERIODE)
            prix_total += tarif_billet(ville_depart, ville_arrivee, True, nom_carte, periode)
        else:   # si l'utilisateur ne vient pas d'acheter une carte
            precisions = input('Autres precisions a fournir ? (oui/non) ')
            if precisions=="oui":
                carte = input("Carte de reduction (Jeune, Senior, ou aucune)? ")
                if carte_valide(carte):
                    nom_carte = carte
                    periode = input(MSG_PERIODE)
                else:   # si l'utilisateur n'a pas choisi une bonne carte alors 
                    modifier = input("Billet modifiable ? (oui/non) ")
                    if modifier=="non":
                        modifiable = False
            prix_total = tarif_billet(ville_depart, ville_arrivee, modifiable, nom_carte, periode)
      
    print("Prix total:", prix_total, 'euros')
    return prix_total
        
    
        
        
        
        
        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    prix_client()

