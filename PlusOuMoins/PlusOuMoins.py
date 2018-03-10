## Le but de ce jeu est de générer un nombre et de trouver si c'est c'est le bon ou pas

import random

nombre = random.randint(1,1000)

guess = ''

count = 0

print(nombre)
while guess != nombre:
    guess = int(input("Entre un nombre"))
    if guess > nombre:
        print("Trop grand")
        count = count + 1
    elif guess < nombre:
        print("Trop petit")
        count = count + 1
    else:
        print("Bravo: tu as trouvé le bon nombre et il t'a fallu ", count, " essais")
