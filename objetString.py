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

#selection de chaine
chaine = "bonjour5t"
print(chaine[:4]) # 4 premier caracteres (du debut jusquau 5em exclus)
print(chaine[4:]) # sans les 4 premier caracteres (du 5em a la fin)
print(chaine[:len(chaine)-1]) # tout sauf le dernier caratere
print(chaine[-1]) # rien sauf le dernier caractere
print(chaine[-2]) # rien sauf l'avant dernier
print(chaine[2:len(chaine)-2]) # sans 2 premiers ni les 2 derniers

# modifier une chaine par indice n'est pas possible, on utlise les selection
# count() find() replace() sont bien pour cela
chaine = "donjtur"
# chaine[0] = "b" pas possible
chaine = "b"+chaine[1:]
print(chaine)
chaine = chaine[:4] +"o" + chaine[5:]
print(chaine)
chaine = chaine[:4] +"oU" + chaine[6:]
print(chaine)
