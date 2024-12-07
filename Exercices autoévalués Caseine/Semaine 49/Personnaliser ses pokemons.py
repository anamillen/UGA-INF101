"""Dans un jeu vidéo Pokemon, on souhaite donner des noms personnalisés à certains types de pokémons. Pour ce faire, on définit une fonction noms_perso(pokemons, noms), qui prend en argument une liste de pokémons attrapés, et un dictionnaire faisant correspondre des noms de pokémons originaux à leurs nouveaux noms. La fonction renvoie une nouvelle liste de pokémons, avec les noms modifiés. Les noms qui n'apparaissement pas dans le dictionnaire restent inchangés.
"""

import doctest

# definitions de fonctions

def noms_perso(pokemons, noms):
    """
    La fonction renvoie une nouvelle liste de pokémons, avec les noms modifiés.
    Les noms qui n'apparaissement pas dans le dictionnaire restent inchangés.
    
    Parametres :
    - pokemons (list) : liste de pokémons attrapés
    - noms (dict) : un dictionnaire faisant correspondre des noms de pokémons originaux à leurs nouveaux noms
    
    Renvoie :
    res (list) : liste de pokemons renommes 

    Exemple:
    >>> mes_pokemons = ["pikachu", "bulbizarre", "roucarnage", "lippoutou"]
    >>> mes_noms = {"bulbizarre": "jean-jacques", "roucarnage": "gros pigeon"}
    >>> noms_perso(mes_pokemons, mes_noms)
    ['pikachu', 'jean-jacques', 'gros pigeon', 'lippoutou']
    """
    li_noms = list(noms)
    res = []
    for pkmn in pokemons:
        if pkmn in li_noms:
            res.append(noms[pkmn])
        else: # si le nom n'est pas present dans le dictionnaire alors
            res.append(pkmn)
    return res
        
# programme principal
doctest.testmod()