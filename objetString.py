# -*-coding:utf-8 -* 
# -*-coding:Latin-1 -*

# help(str) for more infos
def quitter():
    #crée une chaine vide | comme int() crée un entier null:0
    chaine = str()
    while chaine.lower() != "q":
        print("taper 'Q' pour quitter ")
        chaine = input()
    print("Merci !")

chaine = "hamza mallé timere"
print(chaine.capitalize())
print(chaine.strip().center(20))
print(len(chaine))

# formter un string 1ère syntaxe de format()
nom = "timera"
prenom = "hamza"
age = 26
date = "31 novembre 1990"
heure = "17h00"
print("je m'appelle {0} {1}, j'ai {2} ans."\
      .format(prenom.capitalize(), nom.upper(), age))
print("je suis né un {} {} à {} .".format("vendredi",date,heure))

# seconde syntaxe de format()
adresse = """
    {num_rue} {nom_rue}
    {code_postal} {ville}
""".format(num_rue = 15, nom_rue = "avenue auguste renoir",\
           code_postal = 77680, ville = "roissy-en-brie")
print(adresse)

# concatenation de chaine
prix = 15
print(" ce mobilier coûte " + str(prix) +"€.")

chaine = "salut"
i = 0
while i<len(chaine):
    print(chaine[i])
    i += 1
