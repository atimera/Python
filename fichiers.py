# -*-coding:Latin-1 -*

import os

# reportoire de travail

working_dir = os.getcwd()

print(working_dir)
#chdir("le rep de travail") pour changer de rep de travail

# Lecture et écriture dans une fichier

fichier = open("files/test.txt", "r") # r:read, w:write, a:append

print(fichier.closed) # true if it's closed
print("le fichier ouvert est: {}".format(fichier))

contenu = fichier.read()
lignes = contenu.split('\n')
lignes = [line for line in lignes if line != ""] # sans les ligne vides
print(lignes)
fichier.close()

with open("files/test1.txt", "w") as fichier: # fichier se close automaitquement
    fichier.write("Je viens d'écrire ceci: \nHéllo tout le monde !!")


