def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    prenom = input("Entrez votre prénom")
    print (f"Bonjour {prenom}")

def exercice3():
    print(f" Première ligne\n Deuxième ligne\n Troisième ligne \n")

def exercice4():
    try:
        annee_naissance = int (input("Entez votre année de naissance : "))
        annee = 2025
        age = 0
    
        if annee_naissance < 2025:
            age = annee - annee_naissance
            print(f"Tu as approximativement {age} ans")
         
        else:
            print(f"Tu ne viens pas du futur,veuillez rentrer une année valide")

    except ValueError:
        print(f"Veuillez rentrer des chiffres.")

def exercice5():
    try:
        nombre1 = int (input("Entrez un chiffre."))
        nombre2 = int (input("Entrez un chiffre."))
        resultat = nombre1 + nombre2
        print(f"{resultat}")

    except ValueError:
        print(f"Veuillez taper un chiffre")

def exercice6():
    try:
        nombre1 = int (input("Entrez un nombre"))
        nombre2 = int (input("Entrez un nombre"))
        resultat = nombre1 - nombre2
        print(f"{resultat}")

    except ValueError:
        print(f"Veuillez entrer un nombre")

def exercice7():
    try:
        nombre1 = int (input("Entrez un nombre"))
        nombre2 = int (input("Entrez un nombre"))
        resultat = nombre1 * nombre2
        print(f"{resultat}")

    except ValueError:
        print(f"Veuillez rentrer un nombre")

def exercice8():
    try:
        nombre1 = int (input("Entrez un nombre"))
        nombre2 = int (input("Entrez un nombre"))
        resultat = 0

        if nombre2 == 0:
         print(f"Veuillez entrer une autre valeur")

        else:
         resultat = nombre1 / nombre2
        print(f"{resultat}")

    except ValueError:
        print(f"Veuillez entrer un nombre")

def exercice9():
    try:
        nombre1 = int (input("Entrez un nombre"))
        resultat = nombre1 * nombre1
        print(f"{resultat}")

    except ValueError:
        print(f"Veuillez entrer un nombre")

def exercice10():
    try:
        nombre1 = int (input("Entrez un nombre"))
        resultat = nombre1 * 2
        print(f"{resultat}")

    except ValueError:
        print(f"Veuillez entrer un nombre")

def exercice11():
    try:
        nombre1 = int (input("Entrez un nombre"))
        resultat = nombre1 / 2
        print(f"{resultat}")
    
    except ValueError:
        print(f"Veuillez entrer un nombre")

def exercice12():
    message = "Ce message s'affichera 5 fois \n"
    message5 = message + message + message + message + message
    print(f"{message5}")

def exercice13():
    compteur = 0
    
    for compteur in range( compteur + 1 , 6):
        print(f"{compteur}")

def exercice14():
    compteur = 1
   

    for compteur in range(compteur , 6):
        resultat = compteur * 2
        print(f"{compteur} x 2 = {resultat}")

def exercice15():
    try:
        nombre1 = int (input("Entrez un chiffre"))
        perimetreCarre = nombre1 * 4 
        print(f"Le périmètre du carré est de {perimetreCarre} cm.")

    except ValueError:
        print(f"Veuillez entrer un chiffre.")

def exercice16():
    try:
        nombre1 = int(input("Entrez un chiffre"))
        aireCarre = nombre1 * nombre1
        print(f"L'aire du carré est de {aireCarre} cm.")

    except ValueError:
        print(f"Veuillez entrer un chiffre")

def exercice17():
    try:
        euro = int(input("Entrez un chiffre"))
        dollar = euro * 1.1
        print(f"{euro} euros est égal à {dollar} $.")

    except ValueError:
        print(f"Veuillez entrer un chiffre.")

def exercice18():
    try:
        minute = int(input("Entrez un chiffre"))
        minuteEnSeconde = minute * 60
        print(f"{minute} minutes est égal à {minuteEnSeconde} secondes.")
    
    except ValueError:
        print(f"Veuillez rentrer un chiffre.")
    
def exercice19():
    try:
        prix = int(input("Veuillez entrer un prix"))
        taxePrix = prix * 20 / 100 + prix
        print(f"Pour un prix de {prix} euros, le coût après taxe sera de {taxePrix} euros.")

    except ValueError:
        print(f"Veuillez entrer un chiffre")

def exercice20():
        
    age = input("Veuillez entrer votre age.")
    prenom = input("Veuillez entrer votre prénom")

    if prenom.isalpha() and age.isdigit():
        print(f"Tu t'appelles {prenom} et tu as {age} ans.")
    
    else:
        print(f"Veuillez rentrer des données correctes.")

def exercice21():
    nombre1 = int (input("Veuillez rentrer un nombre"))

    if nombre1 < 0:
        print(f"Négatif")

    elif nombre1 > 0:
        print(f"Positif")

    else:
        nombre1 = 0
        print(f"Nul")

def exercice22():

    try:
        age = int (input("Veuillez rentrer votre âge."))

        if age >= 18:
            print(f"Majeur")
        
        else:
            print(f"Mineur")

    except ValueError:
        print(f"Veuillez rentrer un nombre ou chiffre.")

def exercice23():

    try:
        note = int (input("Veuillez rentrer votre note."))

        if note >= 10:
            print(f"Validé")

        else:
            print(f"Refusé")

    except ValueError:
        print(f"Veuillez rentrer un nombre ou chiffre.")

def exercice24():
    try:
        nombre1 = int (input("Veuillez rentrer un chiffre ou un nombre"))
        nombre2 = int(input("Veuillez rentrer un chiffre ou un nombre"))

        if nombre1 > nombre2:
            print(f"{nombre1} est plus grand")

        elif nombre1 == nombre2:
            print(f"Les données rentrées sont égales.")

        else:
            nombre1 < nombre2
            print(f"{nombre2} est plus grand.")
    
    except ValueError:
        print(f"Veuillez rentrer un nombre ou un chiffre.")

        


        


    
   
 
def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    if choix == "2":
        exercice2()
    if choix == "3":
        exercice3()
    if choix == "4":
        exercice4()
    if choix == "5":
        exercice5()
    if choix == "6":
        exercice6()
    if choix == "7":
        exercice7()
    if choix == "8":
        exercice8()
    if choix =="9":
        exercice9()
    if choix == "10":
        exercice10()
    if choix == "11":
        exercice11()
    if choix == "12":
        exercice12()
    if choix == "13":
        exercice13()
    if choix =="14":
        exercice14()
    if choix == "15":
        exercice15()
    if choix == "16":
        exercice16()
    if choix == "17":
        exercice17()
    if choix == "18":
        exercice18()
    if choix == "19":
        exercice19()
    if choix =="20":
        exercice20()
    if choix == "21":
        exercice21()
    if choix == "22":
        exercice22()
    if choix == "23":
        exercice23()
    if choix == "24":
        exercice24()

    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()


