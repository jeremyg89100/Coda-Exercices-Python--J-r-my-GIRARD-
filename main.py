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

    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()


