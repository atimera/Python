

# Les classes
class Personne: # définition de la classe
    """ Une classe qui represente une personne
        Une personne est caracterisée par
        - son nom
        - son prenom
        - son age
        - son lieu de résidence (ex: Paris)

        et un attribut de class compteur du nombre d'objet crée
    """

    compteur = 0 #attribut de classe
    
    def __init__(self): # le constructeur: (__init__) est une fonction speciale
        self.nom = "inconnu" 
        self.prenom = "inconnu"
        self.age = 18
        self.residence = "paris".capitalize()

        Personne.compteur += 1 #attribut de classe

class TableauNoir:
    """ un tableau noir sur laquelle on peut ecrire """

    compteur = 0 #attribut de class

    def __init__(self):
        """ le constructeur """
        self.surface = "" # la surface du tableau
        TableauNoir.compteur += 1 #attribut de class

    def ecrire(self, message): #methon d'instance
        """ ecrit un message sur le tableau """
        if self.surface != "":
            self.surface += "\n"
        self.surface += message

    def lire(self): #methon d'instance
        """ affiche ce qui ecrit sur le tableau """
        print(self.surface)
    def effacer(self): #methon d'instance
        """ efface ce qui a écrit sur le tableau """
        self.surface = ""

    # Methode de classe et methode static
    def combien(cls):
        """ affiche combien d'objet ont été crées """
        print("Jusqu'à présent {} objets ont été crées".format(TableauNoir.compteur))

    combien = classmethod(combien) # un build-in pour dire que c une method de class
    # TableauNoir.combien() marchera ou encore unObjet.combien()
    # une methode de classe prend en parametre 'cls' et non 'self'

    #POUR LES METHODE STATIC
    # la methode ne prendra ni 'cls' ni 'self' en parametre
    # on utilise le build-in "laMethode = staticmethod(leMethode)"
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")

        afficher = staticmethod(afficher)

# la fonction dir(unObjet) renvoit les nom des attribut et methode de l'objet
# __dict__ renvoit un dictionnaire avec comme cles les nom des attribut et comme valeur leur valeurs

# utilisation: unObjet.__dict__
