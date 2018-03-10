## Ici il est question d'écrire des fonctions qui écrivent les tables de multiplications

def table(n):
    i = 0 # Notre compteur ! L'auriez-vous oublié ?
    while i < 10: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", n, "=", (i + 1) * n)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.


table(8)


import math

nombre = int(input("Entrez un nombre. On calcule la racine de celui-ci. "))
print(math.sqrt(nombre))
