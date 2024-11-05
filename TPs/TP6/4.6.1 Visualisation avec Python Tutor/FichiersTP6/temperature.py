def proche_zero(l):
    # enlever la ligne ci-dessous et ecrivez a la place le code de la fonction
    return None


# fonction pour tester proche_zero, ne pas modifier
def tester_fonction(ltemp, res_attendu, num_test) :
    sauvegarde = list(ltemp)
    res = proche_zero(ltemp)

    if res == res_attendu :
        if ltemp == sauvegarde :
            print("Test", num_test, "ok")
        else :
           print("Test", num_test,": résultat ok, mais vous avez modifie la liste en argument de la fonction !")
    else :
        print("Probleme dans test", num_test, ", vous avez trouve", res, "au lieu de", res_attendu, "pour la liste", sauvegarde)

# programme principal, pour tester la fonction proche_zero

# n'hesitez pas a completer avec vos propres tests !!!

if __name__ == "__main__":

    ltest = [[1, -2, -8, 4, 5], [-12, -5, -137], [42, -5, 12, 21, 5, 24],
             [42, 5, 12, 21, -5, 24], [-5, -4, -2, 12, -40, 4, 2, 18, 11, 5],
             [3, 1, 5, -1, 4], [3, -2, 5, 12, -2, 4], []]

    lres = [1, -5, 5, 5, 2, 1, -2, 0] 

    i = 0
    while i < len(ltest) :
        tester_fonction(ltest[i],lres[i],i+1)
        i = i + 1
