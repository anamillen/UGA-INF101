
# definitions de fonctions
def moyenne_etudiant(etudiant):
    """Prend en argument un élément de la liste notes_groupe (décrite précédemment) et retourne la moyenne de l’étudiant."""
    somme_notes = 0
    matieres = etudiant['notes']
    n_matieres = len(matieres)
    for matiere in matieres:
        somme_notes+=matieres[matiere]
    if n_matieres!=0:
        myn = somme_notes / n_matieres
    else: # si le nombre de matieres est 0
        myn = somme_notes
    return myn
    
def meilleur(notes_groupe):
    """Prend la liste du groupe en argument et retourne la meilleure moyenne du groupe ainsi que le nom de l’étudiant qui l’a obtenue."""
    meilleure_myn = 0
    meilleur_etudiant = ""
    for etudiant in notes_groupe:
        myn = moyenne_etudiant(etudiant)
        if myn>meilleure_myn:
            meilleure_myn = myn
            meilleur_etudiant = etudiant['nom']
    return meilleure_myn, meilleur_etudiant

def myns_par_matiere(notes_group):
    """Calcule et renvoie un dictionnaire avec les moyennes par toutes les matieres"""
    matieres = {}
    myns = {}
    for etudiant in notes_group:
        for matiere in etudiant['notes']:
            if matiere in matieres:
                matieres[matiere]['n etudiants']+=1
                matieres[matiere]['somme']+=etudiant['notes'][matiere]
            else:    # si la matiere est rencontree par la 1ere fois alors
                matieres[matiere] = {}
                matieres[matiere]['n etudiants']=1
                matieres[matiere]['somme']=etudiant['notes'][matiere]
    
    for matiere in matieres:
        myns[matiere] = matieres[matiere]['somme'] / matieres[matiere]['n etudiants']
    return myns
   
def matiere_difficile(notes_group):
    """Retourne le nom de la matière la plus difficile (celle qui a la pire moyenne de groupe)"""
    myns  = myns_par_matiere(notes_group)
    pire_myn = 21
    pire_matiere = ''
    for matiere in myns:
        if myns[matiere]<pire_myn:
            pire_myn = myns[matiere]
            pire_matiere = matiere
    return pire_matiere