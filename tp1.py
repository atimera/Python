# -*-coding:Latin-1 -*

#import os # On importe le module os
#print("Bonjour le monde !")
#os.system("pause")

# ANNEE BISSEXTILE OU PAS ?
annee = input('Saisissez une année : ')
annee = int(annee)
if (annee % 4) != 0:
    print("l'année ",annee," n'est pas bissextile")
elif (annee % 100) == 0:
    if (annee % 400) == 0:
        print("l'année ",annee," est bissextile")
    else:
        print("L'année ",annee," n'est pas bissextile")
else:
    print("L'année ",annee," est bissextile")
