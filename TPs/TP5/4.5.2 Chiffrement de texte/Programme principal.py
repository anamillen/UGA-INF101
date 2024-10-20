# on importe les modules necessaires
import chiffre_de_cesar_par_decalage 
import chiffrement_numerique

# programme principal
MSG_CHOIX = "Quel chiffre voulez-vous utiliser ?"
MSG_OPT = "(tapez a pour le chiffre de Cesar et b pour le chiffre numerique) "
MSG_TXT = "Tapez votre texte : "
MSG_REINIT = "Voulez-vous rejouer ? (o/n) "
MSG_END = "Au revoir !"


print(MSG_CHOIX)
init = "o"
while init=="o":
    option_choisie = input(MSG_OPT)
    txt = input(MSG_TXT)
    if option_choisie == "a":
        print(chiffre_de_cesar_par_decalage.texte_chiffre(txt))
    else:
        print(chiffrement_numerique.chiffre_texte(txt))
    init = input(MSG_REINIT)

print(MSG_END)



