# -*-coding:Latin-1 -*

# help(str) for more infos
def quitter():
    #cr�e une chaine vide | comme int() cr�e un entier null:0
    chaine = str()
    while chaine.lower() != "q":
        print("taper 'Q' pour quitter ")
        chaine = input()
    print("Merci !")

chaine = "hamza mall� timere"
print(chaine.capitalize())
print(chaine.strip().center(20))
print(len(chaine))

# formter un string 1�re syntaxe de format()
nom = "timera"
prenom = "hamza"
age = 26
date = "31 novembre 1990"
heure = "17h00"
print("je m'appelle {0} {1}, j'ai {2} ans."\
      .format(prenom.capitalize(), nom.upper(), age))
print("je suis n� un {} {} � {} .".format("vendredi",date,heure))

# seconde syntaxe de format()
adresse = """
    {num_rue} {nom_rue}
    {code_postal} {ville}
""".format(num_rue = 15, nom_rue = "avenue auguste renoir",\
           code_postal = 77680, ville = "roissy-en-brie")
print(adresse)
