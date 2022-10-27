while True:
    texte = str(input("Entrez un texte ou NON pour arreter le programme : "))
    if texte == "NON":
        print("Merci d'avoir jouer!")
        break
    mots = texte.split()
    eccronyme = ""
    for mot in mots:
        eccronyme += mot[0].upper()
    print("L'accronyme de votre texte est : " + eccronyme)