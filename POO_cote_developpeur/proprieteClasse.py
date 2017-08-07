

# les propriétés
"""
    si on souhaite aux attribut d'un objet on pourait faire en général:
    method.attribut
    Mais si on veut pas permetre cet acces ou method.attr = valeur: on crée des propriétés

    En python tout est public: pas de private
"""
class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligné _ devant le nom
    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieu_residence'"""
        
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence
    
    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)
    # ATTENTION l'ordre est important: _get_attr, _set_attr, _del_attr, _help_attr
    # accesseur, mutateur, supression(del Objet.attr), aide(help(Objet.attr)) sur l'attribut
    
"""
Les propriétés permettent de contrôler l'accès à certains attributs d'une instance.
Elles se définissent dans le corps de la classe en suivant cette syntaxe :nom_propriete = property(methode_accesseur, methode_mutateur, methode_suppression, methode_aide).
On y fait appel ensuite en écrivantobjet.nom_proprietecomme pour n'importe quel attribut.
Si l'on souhaite juste lire l'attribut, c'est la méthode définie comme accesseur qui est appelée.
Si l'on souhaite modifier l'attribut, c'est la méthode mutateur, si elle est définie, qui est appelée.
Chacun des paramètres à passer àpropertyest optionnel.
"""
