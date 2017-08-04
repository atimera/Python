""" Module multipli contient la fonction:

    table(n, maxi)
"""

def table(n,maxi=10):
    # docstring
    """ param : n, maxi (int)
        affiche la table de multiplication de n de 1 à maxi """
    i = 1
    while i <= maxi:
        print(i," * ",n," = ",i * n)
        i += 1


