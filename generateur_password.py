import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+,./<>?;:[]{}|"

while True:
    nombre = input("Entrez la longueur du mot de passe ou NON pour arreter le programme: ")
    try:
        if nombre == "NON":
            print("Merci d'avoir jouer!")
            break
        taille = int(nombre)
        if taille > 0:
            mot_de_pass = "".join(random.sample(alphabet, taille))
            print("Votre mot de pass est : " + mot_de_pass)
        else:
            print("Veuillez entrer une valeur superieure a 0!")
    except:
        print("Veuillez entrer un nombre")
