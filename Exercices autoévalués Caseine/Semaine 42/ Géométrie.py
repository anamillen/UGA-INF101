# import de modules
import math

# definitions de fonctions
def coord_centre_cercle(x1,y1,x2,y2):
    """Prend en arguments les coordonnées x1, y1, x2, y2 de deux points diamétralement opposés sur un cercle, 
    et renvoie les coordonnées x, y du centre du cercle."""
    x = (x1+x2)/2
    y = (y1+y2)/2
    return x,y
    
def coord_bas_losange(x1,y1,x2,y2):
    """Prend en arguments les coordonnées x1,y1,x2,y2 de deux points placés sur un losange vertical 
    (le premier sur le sommet gauche, le second sur le sommet supérieur) et renvoie les coordonnées x, y du sommet inférieur du losange."""
    x = x2
    y = y2-abs(y2-y1)*2
    return x, y
    
def coordDEF():
    """Ne prend pas d'argument, et demande à l'utilisateur les coordonnées des points A, B, C
    puis renvoie 6 valeurs de retours xD, yD, xE, yE, xF, yF correspondant aux coordonnées des points D, E, F dans cet ordre."""
    # definitions de constantes
    MSG_COORD  ="Entrez les coordonnees du point"
    MSG_X = "x = ? "
    MSG_Y = "y = ? "
    
    # input de l'util
    print(MSG_COORD,"A")
    xA = float(input(MSG_X))
    yA = float(input(MSG_Y))
    print(MSG_COORD,"B")
    xB = float(input(MSG_X))
    yB = float(input(MSG_Y))
    print(MSG_COORD,"C")
    xC = float(input(MSG_X))
    yC = float(input(MSG_Y))
    
    # cherchons D(xD,yD)
    xD, yD = coord_centre_cercle(xA,yA,xB,yB)
    
    # cherchons E(xE,yE)
    xE, yE = coord_bas_losange(xA,yA,xB,yB)
    
    # cherchons F(xF,yF)
    xF, yF = coord_centre_cercle(xE,yE,xC,yC)
    
    return xD, yD, xE, yE, xF, yF
    

def volume_sphere(r = 1):
    """Prend en argument le rayon r de la sphere (qui vaut 1 par défaut) et renvoie son volume : 
    V = 4πr^3/3."""
    pi = math.pi
    return 4*pi*r**3/3

def volume_cone(h,r = 1):
    """Prend en argument la hauteur h ainsi que le rayon r de la base d’un cône de révolution 
    (r vaut 1 par défaut) et renvoie le volume du cône : V = πr^2h/3."""
    pi = math.pi
    return pi*r**2*h/3
    
def volume_figure():
    # initialisation de constantes
    MSG_R = "Entrez le rayon de :"
    MSG_H = "Entrez la hauteur"
    MSG_CONE1 = "cone de devant"
    MSG_CONE2 = "cone au-dessus"
    
    # saisies de l'util
    print(MSG_R)
    rG = float(input("la sphere de gauche"))
    rM = float(input("la sphere du milieu"))
    rD = float(input("la sphere de droite"))
    c1_r = float(input(MSG_CONE1))
    print(MSG_H)
    c1_h = float(input(MSG_CONE1))
    print(MSG_R)
    print(MSG_H)
    c2_h = float(input(MSG_CONE2))
    
    # l'algorithme principal pour trouver le volume de la figure
    V=volume_sphere(rG)+volume_sphere(rM)+volume_sphere(rD)
    V+=volume_cone(c1_h,c1_r)+volume_cone(c2_h,rM)
    return V
    
    
    
    
    

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
