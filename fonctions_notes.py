# Mini-projet Python : gestion des notes des etudiants
# Les notes sont fictives.


etudiants = ["Samba", "Evan", "Princia Celeste", "Noam", "Jean", "Alexandre", "Clement"]

# Le dictionnaire associe chaque etudiant a ses trois notes.
notes = {
    "Samba": [12, 15, 14],
    "Evan": [16, 14, 17],
    "Princia Celeste": [13, 12, 15],
    "Noam": [9, 11, 10],
    "Jean": [14, 16, 13],
    "Alexandre": [17, 18, 16],
    "Clement": [8, 10, 9]
}

# Cette fonction calcule une moyenne.
def calculer_moyenne(trois_notes):
    total = 0
    for note in trois_notes:
        total = total + note
    return total / 3

# Cette fonction donne une mention selon la moyenne.
def donner_mention(moyenne):
    if moyenne >= 16:
        return "Excellent"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Insuffisant"

# Cette fonction affiche les resultats et les ecrit dans un fichier.
def afficher_resultats():
    fichier = open("resultats.txt", "w", encoding="utf-8")
    fichier.write("RESULTATS DE LA CLASSE\n\n")
    print("\nRESULTATS DE LA CLASSE")

    total_moyennes = 0
    nombre_valides = 0
    meilleur_nom = ""
    meilleure_moyenne = -1

    for nom in etudiants:
        moyenne = calculer_moyenne(notes[nom])
        mention = donner_mention(moyenne)
        total_moyennes = total_moyennes + moyenne

        if moyenne >= 10:
            nombre_valides = nombre_valides + 1
        if moyenne > meilleure_moyenne:
            meilleure_moyenne = moyenne
            meilleur_nom = nom

        print(nom, "- Notes :", notes[nom], "- Moyenne :", round(moyenne, 2), "- Mention :", mention)
        fichier.write(nom + "\n")
        fichier.write("Notes : " + str(notes[nom]) + "\n")
        fichier.write("Moyenne : " + str(round(moyenne, 2)) + "\n")
        fichier.write("Mention : " + mention + "\n\n")

    moyenne_classe = total_moyennes / len(etudiants)
    print("\nMoyenne generale :", round(moyenne_classe, 2))
    print("Meilleur etudiant :", meilleur_nom, "-", round(meilleure_moyenne, 2))
    print("Etudiants ayant valide :", nombre_valides)
    print("Etudiants n'ayant pas valide :", len(etudiants) - nombre_valides)

    fichier.write("Moyenne generale : " + str(round(moyenne_classe, 2)) + "\n")
    fichier.write("Meilleur etudiant : " + meilleur_nom + "\n")
    fichier.write("Etudiants ayant valide : " + str(nombre_valides) + "\n")
    fichier.write("Etudiants n'ayant pas valide : " + str(len(etudiants) - nombre_valides) + "\n")
    fichier.close()
    print("Les resultats sont enregistres dans resultats.txt")

# Cette fonction cherche un etudiant.
def rechercher_etudiant():
    prenom = input("Quel prenom veux-tu rechercher ? ")
    if prenom in notes:
        moyenne = calculer_moyenne(notes[prenom])
        print("Notes :", notes[prenom])
        print("Moyenne :", round(moyenne, 2))
        print("Mention :", donner_mention(moyenne))
    else:
        print("Etudiant introuvable.")

# Le programme commence ici.
afficher_resultats()

choix = ""
while choix != "3":
    print("\nMENU")
    print("1 - Rechercher un etudiant")
    print("2 - Afficher les resultats")
    print("3 - Quitter")
    choix = input("Ton choix : ")

    if choix == "1":
        rechercher_etudiant()
    elif choix == "2":
        afficher_resultats()
    elif choix == "3":
        print("Au revoir !")
    else:
        print("Choisis 1, 2 ou 3.")
