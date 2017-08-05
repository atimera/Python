

# création et édition de dictionnaire

d = dict()
print(d)
d["pseudo"] = "laenzo"
d["password"] = "***"
d[""]= "nom"
print(d)

inventaire = {
        "pommes":45, "oranges":26, "mangues":32, "poires":21, "fraises":18
    }
print(inventaire)
v = inventaire.pop("mangues") #ou bien: del inventaire["mangues"]
print(inventaire)

def aboie():
    print("wof wof !!!")
def miole():
    print("miaaw miaaw !!")       
def crie():
    print("ahhhhhhh... !!")
print2 = print
print2("OK c'est bon")
          
dic = {"chat":miole, "chien":aboie, "enfant":crie}
dic["chien"]()
dic["enfant"]()
dic["chat"]()

# les methodes de parcours

for cle in dic.keys():
    print(cle)
for valeur in dic.values():
    print(valeur)
    valeur()
for cle, valeur in dic.items():
    print((cle, valeur))


# dictionnaire et parametre de fonctions

def parametre_nom(*liste, **nomme):
    print("parametres nommés : {}\n".format(nomme))
    print("liste de parametre : {}\n".format(liste))

liste = [1,2,3,5,"e","o"]
parametre_nom(liste, x="7", y=8)

#transformer un dictionnaire en parametre de fonctions
parametre = {"sep": " >> ", "end": " -fin\n"}
print(0,1,2,3,4,5,6,7,8,9,**parametre)





    
