def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    prenom = input("Entrez votre prénom")
    print (f"Bonjour {prenom}")

def exercice3():
    print(f" Première ligne\n Deuxième ligne\n Troisième ligne \n")

def exercice4():
    annee_naissance = int (input("Entez votre année de naissance"))
    annee = 2025
    age = 0
    
    if annee_naissance < 2025:
        age = annee - annee_naissance
        print(f"Tu as approximativement {age} ans")
         

    else: print(f"Tu ne viens pas du futur,veuillez rentrer une année valide")
   

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
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()


