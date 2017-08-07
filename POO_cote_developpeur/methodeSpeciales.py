
# Edition de l'objet et acces aux attributs
"""
Si on ne definit pas les fonctions speciales, python aura un comparement par defaut
on n'est pas obligé de les definir meme le constructeur __init__

création de l'objet: __init__(self,...)
supréssion de l'objet: __del__(self)
représention de l'objet: __repr__(self)
(comme toString() en java) qui n'est pas definie par defaut appel de __repr__: __str__
si on fait objet.attr alors que attr n'existe pas python fait appel à: __getattr__(self, attr)
Méthode appelée quand on fait objet.nom_attr = val_attr.: __setattr__(self, attr, valeur)


"""
class Personne:
    """ Utilisation des methodes speciales """

    def __init__(self, nom, prenom):
        """ Le constructeur """
        print("L'objet est crée")
        self.nom = nom
        self.prenom = prenom
        self.residence = "Paris"
    # Les methodes spéciales pour la classe        
    def __del__(self):
        """ Methode appelée quand l'objet est supprimé """
        print("{} {} qui habite à {} n'est plus !".format(self.prenom, self.nom, self.residence))

    def __repr__(self):
        """ présention de l'objet quand tape 'objet' dans la console Utilisé aussi pour debuguer
            Retourne une chaine de caractère """
        return "Personne: Nom:({}) Prénom:({}) Résidence:({})".format(self.nom, self.prenom, self.residence)
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet utilisé aussi pour debuguer
         - Quand on fait un print(objet)
         - Quand on fait str(objet) """
        return "{} {}, habite à {}".format(self.prenom, self.nom, self.residence)

    # Les méthodes spéciales pour les attributs
    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte ou bien on redirige vers un autre attr"""
        print("Alerte ! Il n'y a pas d'attribut '{}' ici!".format(nom))
        print("Redirection vers l'attribut Nom:{}".format(self.nom))

    #def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""        
        #object.__setattr__(self, nom_attr, val_attr)
        #self.enregistrer()
        #print("affectation effectuée")

    def __delattr__(self, nom_attr):
        """On ne peut supprimer d'attribut, on lève l'exception
        AttributeError"""
        
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")

"""
    Quelques fonctions qui peuvent etre utiles
objet = MaClasse() # On crée une instance de notre classe
getattr(objet, "nom") # Semblable à objet.nom
setattr(objet, "nom", val) # = objet.nom = val ou objet.__setattr__("nom", val)
delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon
"""

# Les méthodes spéciales pour les Conteneur (list, str, dict, tuple...)
"""
__getitem__(self) : definie quoi faire quand on fait objet[index]
__setitem__(self) : definie quoi faire quand on fait objet[index] = valeur
__delitem__(self, index) : definie quoi faire quand on fait del(objet[index])
__contains__(self, elt) : est appelé quand on fait: (elt in conteneur) return True ou False
__len__(): pour donner la taille du conteneur quand on fait len(conteneur), objet.__len__() est appelé

__repr__, __str__ : sont aussi valable pr les conteneurs

"""




























    
    
