# -*-coding:Latin-1 -*
""" Jeu de simulation de la roulette de casino """

import os
from math import ceil
from random import *

choix = 0
solde = 100
mise = 0
valeur_alea = 0
jouer = True

while solde > 0:
    print("Votre solde est actuellement de : ",solde," $.")
    mise = int(input("Faites une mise : "))
    solde -= mise
    print(valeur_alea)
    choix = int(input("Quelle est votre choix entre 0 et 49 : "))
    valeur_alea = randrange(50)
    if choix == valeur_alea:
        print("Félicitations vous venez de gagner le triple de votre mise")
        solde += mise * 3
        print("Votre nouveau solde est de : ",solde)
    elif (choix % 2 == 0 and valeur_alea % 2 == 0) or \
         (choix % 2 != 0 and valeur_alea % 2 != 0):
        print("Bien jouer vous venez de gagner la moitié de votre mise")
        solde += ceil(mise / 2)
        print("Votre nouveau solde est de : ",solde)

    else:
        print("Oooh! Dommage pour vous venez de perdre votre mise car vous etes loin de la valeur à trouver.")
        print("Votre nouveau solde est de : ",solde)
        decision = input("Appuyer sur la touche 'r' pour rejour ou 'q' pour quitter")
        if decision == 'r':
            jouer = True
        elif decision == 'q':
            jouer = False
print("Vous quittez le jeu avec un solde de : ",solde)

os.system('pause')
