# -*-coding:Latin-1 -*

import os
import pickle # pour enregister ou charger des données depuis un fichier

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


# Enregister de objets dans un fichier

inventaire = {
    "pommes": 54, "oranges": 62, "poires": 82, "mangues": 63
    }

# mieux de creer un fichier de donnée par objet
with open("files/donnees", "wb") as fichier : #wb:write binary
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(inventaire)
   

with open("files/donnees", "rb") as fichier : #wb:read binary
    mon_depickler = pickle.Unpickler(fichier)
    invent = mon_depickler.load()
    print(invent) # affiche les données chargées



