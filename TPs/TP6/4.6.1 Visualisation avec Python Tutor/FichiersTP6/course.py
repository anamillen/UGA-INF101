# definitions de fonctions

def plus_proches(li):
    """Etant donnée une liste des forces, 
    identifie les forces les plus proches et 
    renvoie la différence entre ces deux forces 
    (entier positif ou nul).
    
    Exemples :
    >>> plus_proches([2,3,15])
    1
    >>> plus_proches([34,23,12,12])
    0
    >>> plus_proches([12,13,145])
    1
    >>> plus_proches([28,24,22])
    2
    """
    min_diff = float("inf")
    long = len(li)
    for i in range(long):
        for j in range(long):
            if i!=j:
                diff = abs(li[i]- li[j])
                if diff < min_diff:
                    min_diff = diff
    return min_diff

# programme principal, pour tester la fonction plus_proches

# n'hesitez pas a completer avec vos propres tests !!!

if __name__ == "__main__":

    # test 1
    force = [5, 8, 9] # liste forces chevaux (resultat attendu : 1)
    sauvegarde = list(force)
    resultat = plus_proches(force)
    
    if resultat == 1 :
        if force == sauvegarde :
            print("Test 1 ok")
        else :
            print("Test 1 : résultat ok, mais vous avez modifie la liste en argument de la fonction !")
    else :
            print("Probleme dans test 1, vous avez trouve",resultat,"au lieu de 1")
            
    # test 2
    force = [5, 15, 17, 3, 8, 11, 28, 6, 55, 7] # liste forces chevaux (resultat attendu : 1)
    sauvegarde = list(force)
    resultat = plus_proches(force)
    
    if resultat == 1 :
        if force == sauvegarde :
            print("Test 2 ok")
        else :
            print("Test 2 : résultat ok, mais vous avez modifie la liste en argument de la fonction !")
    else :
            print("Probleme dans test 2, vous avez trouve",resultat,"au lieu de 1")

    # test 3
    force = [10,5,8,7,5,9] # liste forces chevaux (resultat attendu : 0)
    sauvegarde = list(force)
    resultat = plus_proches(force)
    
    if resultat == 0 :
        if force == sauvegarde :
            print("Test 3 ok")
        else :
            print("Test 3 : résultat ok, mais vous avez modifie la liste en argument de la fonction !")
    else :
            print("Probleme dans test 3, vous avez trouve",resultat,"au lieu de 0")

    # test 4
    force = [9999888, 9999741, 9999653, 9999595, 9999444, 9999387, 9999241, 9999140, 9999042, 9998937, 9998837, 9998724, 9998609, 9998475, 9998391, 9998321, 9998187, 9998070, 9997991, 9997902, 9997822, 9997767, 9997712, 9997651, 9997540, 9997406, 9997308, 9997210, 9997133, 9997041, 9996946, 9996841, 9996705, 9996655, 9996515, 9996379, 9996277, 9996141, 9996013, 9995910, 9995783, 9995638, 9995528, 9995474, 9995362, 9995304, 9995236, 9995171, 9995123, 9994973, 9994860, 9994798, 9994682, 9994571, 9994473, 9994337, 9994231, 9994159, 9994057, 9993936, 9993889, 9993744, 9993609, 9993469, 9993353, 9993268, 9993219, 9993162, 9993016, 9992897, 9992803, 9992721, 9992630, 9992513, 9992414, 9992326, 9992279, 9992139, 9991988, 9991872, 9991770, 9991671, 9991560, 9991477, 9991383, 9991324, 9991220, 9991071, 9991011, 9990928, 9990786, 9990668, 9990558, 9990487, 9990364, 9990225, 9990156, 9990082, 9989943, 9989835, 9989758, 9989662, 9989611, 9989505, 9989456, 9989329, 9989200, 9989115, 9989003, 9988858, 9988764, 9988635, 9988544, 9988479, 9988388, 9988300, 9988186, 9988093, 9987999, 9987923, 9987798, 9987703, 9987636, 9987557, 9987411, 9987322, 9987177, 9987027, 9986960, 9986837, 9986727, 9986646, 9986583, 9986514, 9986419, 9986315, 9986184, 9986113, 9986058, 9985996, 9985909, 9985776, 9985673, 9985570, 9985486, 9985341, 9985248, 9985141, 9984996, 9984899, 9984825, 9984691, 9984551, 9984492] # liste forces chevaux (resultat attendu : 47)
    sauvegarde = list(force)
    resultat = plus_proches(force)
    
    if resultat == 47 :
        if force == sauvegarde :
            print("Test 4 ok")
        else :
            print("Test 4 : résultat ok, mais vous avez modifie la liste en argument de la fonction !")
    else :
            print("Probleme dans test 4, vous avez trouve",resultat,"au lieu de 47")
