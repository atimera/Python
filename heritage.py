
# Héritage simple
class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self, nom)
        self.matricule = matricule
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

# Héritage multiple
# class MaClasseHeritee(MaClasseMere1, MaClasseMere2):

# Création de mon propre exception
class MonException(Exception):# pouvait aussi hérité de BaseException
    """Exception levée dans un certain contexte… qui reste à définir"""
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message
    def __str__(self):
        """On renvoie le message"""
        return self.message

# exemple d'utilisation
# raise MonException("OUPS... j'ai tout cassé")

# Création d'une exception avec plusieurs parametres
class ErreurAnalyseFichier(Exception):
    """Cette exception est levée quand un fichier (de configuration)
    n'a pas pu être analysé.
    
    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit"""
    
    def __init__(self, fichier, ligne, message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]: {}".format(self.fichier, self.ligne, \
                self.message)
# exemple d'utilisation: lever l'exception
#raise ErreurAnalyseFichier("plop.conf", 34, "Il manque une parenthèse à la fin de l'expression")

"""
En résumé
L'héritage permet à une classe d'hériter du comportement d'une autre en reprenant ses méthodes.
La syntaxe de l'héritage est class NouvelleClasse(ClasseMere):.
On peut accéder aux méthodes de la classe mère directement via la syntaxe : ClasseMere.methode(self).
L'héritage multiple permet à une classe d'hériter de plusieurs classes mères.
La syntaxe de l'héritage multiple s'écrit donc de la manière suivante : class NouvelleClasse(ClasseMere1, ClasseMere2, ClasseMereN):.
Les exceptions définies par Python sont ordonnées selon une hiérarchie d'héritage.
"""
