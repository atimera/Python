""" Module multipli contient les fonction:

    table_mult_par(n)
    table_mult_de(n, maxi)
"""

import os

def table_mult_par(n):
    # docstring
    """ param : n (int)
        affiche la table de multiplication de n """
    i = 1
    while i <= 10:
        print(i," * ",n," = ",i * n)
        i += 1

def table_mult_de(n,maxi=10):
    i = 1
    while i <= maxi:
        print(i," * ",n," = ",i * n)
        i += 1

#test de table_mult_par() dans le module lui meme
#
if __name__ == "__main__":
    table_mult_par(7)

os.system('pause')

