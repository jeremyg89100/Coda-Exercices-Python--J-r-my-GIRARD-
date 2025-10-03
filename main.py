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
            print(f"{nombre2} est plus grand.")
    
    except ValueError:
        print(f"Veuillez rentrer un nombre ou un chiffre.")

def exercice25():
    try:
        nombre1 = int (input("Veuillez rentrer un chiffre ou un nombre"))
        nombre2 = int(input("Veuillez rentrer un chiffre ou un nombre"))

        if nombre1 > nombre2:
            print(f"Ordre décroissant")

        elif nombre1 == nombre2:
            print(f"Les données rentrées sont égales.")

        else:
            nombre1 < nombre2
            print(f"Ordre croissant.")
    
    except ValueError:
        print(f"Veuillez rentrer un nombre ou un chiffre.")

def exercice26():
    try:
        nombre = int (input("Veuillez rentrer un nombre ou un chiffre"))

        if nombre % 5 == 0:
            print(f"{nombre} est divisible par 5")

        else:
            print(f"{nombre} n'est pas divisible par 5")

    except ValueError:
        print(f"Veuillez rentrer un nombre ou un chiffre.")

def exercice27():
    try:
        age = int (input("Veuillez rentrer votre âge"))

        if age < 12:
            print(f"Enfant")
        elif age > 12 and age < 18:
            print(f"Ado")
        else:
            print(f"Adulte")

    except ValueError:
        print(f"Veuillez rentrer un âge valide.")

def exercice28():
    try:
        temperature = int (input("Veuillez rentrer une température"))

        if temperature < 0:
            print(f"Glace")
        elif temperature > 0 and temperature < 100:
            print(f"Liquide")
        else:
            print(f"Gaz")

    except ValueError:
        print(f"Veuillez rentrer une température valide.")

def exercice29():
    try:
        note = int (input("Veuillez rentrer votre note : "))

        if note < 10:
            print(f"Recalé !")
        
        elif note > 10 and note < 12:
            print(f"Passable.")
        
        elif note > 12 and note < 16:
            print(f"Bien")

        else:
            print(f"Très bien !")

    except ValueError:
        print(f"Veuillez rentrer une note valide.")

def exercice30():
    try:
        nombre = int (input("Veuillez entrer un chiffre ou un nombre."))
        
        for compteur in range (1 , nombre + 1):
            print(f"{compteur}")

            if nombre == compteur:
                break

    except ValueError:
        print(f"Veuillez entrer un nombre valide.")

def exercice31():
    try:
        nombre = int (input("Veuillez entrer un chiffre ou un nombre : "))

        for compteur in range (nombre , -1 , - 1):
            print(f"{compteur}")

            if compteur == 0:
                break
            
    except ValueError:
        print(f"Veuillez entrer un nombre ou un chiffre")


def exercice32():

    try:
        nombre = int (input("Veuillez entrer un chiffre ou un nombre"))
        total = 0
        compteur = 0

        for compteur in range( compteur , nombre + 1 ):
            total = total + compteur
            print(f"{total}")
          
    except ValueError:
        print(f"Veuillez rentrer un nombre ou chiffre valide.")

def exercice33():
    try:
    
        nombre = int (input("Veuillez choisir un chiffre : "))

        for compteur in range( 1 , 11):
            total = compteur * nombre
            print(f"{total}")

    except ValueError:
        print(f"Veuillez rentrer un nombre ou chiffre valide.")

def exercice34():
    try:
        nombre = int (input("Veuillez choisir un chiffre/ nombre : "))

        for compteur in range (0 , nombre ):
            if compteur % 2 == 0:
                print(compteur)

    except ValueError:
        print(f"Veuillez entrer un chiffre ou nombre correct.")

def exercice35():

    try:
        nombre = int (input("Veuillez choisir un chiffre / nombre : "))

        for compteur in range ( 1 , nombre + 1):
            carre = compteur ** 2
            print(f"{carre}")

    except ValueError:
        print(f"Veuillez rentrer un chiffre / nombre.")

def exercice36():
    try:
        nombre = int (input("Veuillez entrer un chiffre ou un nombre : "))
        message = "Salut "

        for compteur in range ( 1 , nombre + 1):
            print(f"{message}")

    except ValueError:
        print(f"Veuillez entrer un chiffre ou nombre valide.")

def exercice37():
    compteur = 1
    hauteur = int (input("Veuillez rentrer la hauteur de la pyramide."))
    try:
        for i in range(hauteur):
            print(f"0"*(hauteur - 1 - i),"1"*(compteur),"0"*(hauteur - 1 - i))
            compteur = compteur + 2

    except ValueError:
        print(f"Veuillez rentrer une donnée valide.")


def exercice39():

    input("Pair ou impair ? ")
    import random
    
    nombreRandom = random.randint ( 1 , 10)
    print(f"{nombreRandom}")

    if nombreRandom % 2 == 0:
        print(f"La réponse était paire")

    else:
        print(f"La réponse était impaire")


def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    nom_fonction = f"exercice{choix}"
    if nom_fonction in globals():
        globals()[nom_fonction]()
   
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()


