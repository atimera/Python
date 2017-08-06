

# porté des varibles
a = 8

def print_a():
    """ Essayer d'acceder à une  variable en dehors de la fonction """ # docstring
    global a # sans faire ça on ne peut pas modifier a
    print("la valeur de a est : {}".format(a)) # on accede à a en dehors de la fonction
    
print_a()

# reference

liste1 = [1,2,3,4,5]
liste2 = liste1 # elles auront la meme reference
liste3 = list(liste1) # une copie de liste1
liste1[2] = 99

print(liste2)
def modif(liste):
    try:
        liste[2] = 3
    except IndexError:
        print("l'index n'existe pas")  
modif(liste1)
print(liste2)
print(liste3)

print(liste1 is liste2) # == True car meme reference
print(liste1 is liste3 or liste2 is liste3) # == Fasle car car meme reference
print("ID liste1 est: {}\nID liste2 est: {}\nID liste3 est: {}\
        ".format(id(liste1), id(liste2), id(liste3)))

