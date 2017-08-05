

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

