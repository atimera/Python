import operator # utlisé pour trier nos objets

# Trier avec sort() (une fonction des listes) ou sorted() (un buildin)

etudiants = [("hamza",15,16), ("dramane",15,11), ("hamza",15,14), ("moussa",13,17)]
#etudiants.sort() ne retourne rien et modifie la liste triée par defaut
#liste = sorted(etudiants) # renvoit la liste triée des étudiants sans que liste soit modifiée

#CRITERE de TRI avec le parametre key 
#etudiants.sort(key = lambda colonne: colonne[2]) # Trie par "(nom, age, note)" note Décroissante
#etudiants.sort(key = lambda colonne: colonne[2], reverse = TRUE) # Trie par "(nom, age, note)" note Décroissante
#IDEM avec sorted()

#Trier une liste d'un objet qu'on a crée
class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(
                self.prenom, self.age, self.moyenne)

    
etudiants = [ # création des étudiants
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]
# etudiants = sorted(etudiants) ou etudiants.sort() ne marchera pas ici
# Il faut redefinir la fonction spéciale __lt__() qui est appelé quand on fait l'opération <:lower than) en fonction
    # de la relation d'ordre de notre objet s'il en a
# alors utiliser le parametre "key"
# OU BIEN utiliser le module operator PLUS EFFICACE
    # - importer le module: import operator
etudiants.sort(key = operator.attrgetter("age"), reverse = True) # tri les étudiant ordre décroissant de l'age
Liste = sorted(etudiants, key = operator.attrgetter("moyenne")) # moyenne croissante

#chainage de tri:
liste = sorted(etudiants, key = operator.attrgetter("age", "moyenne"))

