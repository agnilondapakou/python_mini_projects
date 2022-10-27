import random
print("Entrez 1 pour lancer le dé ou 0 pour quitter le jeu")
while True:
 valeure = input("1 ou 0 ? ")
 try:
     decision = int(valeure)
     if decision == 1:
        print(random.randint(1,6))
     elif decision == 0:
        print("Merci d'avoir jouer!")
        break
     else:
        print("Veuillez entrer 1 ou 0")
 except:
    print("Veuillez entrer 1 ou 0")