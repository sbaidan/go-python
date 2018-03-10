import getpass

print("Bienvenue dans le jeu diabolique du pendu by Dan. Les règles sont les suivantes: \n Tu as le droit d'entrer une lettre à la fois. \n Tu as 10 essais pour trouver toutes les lettres du mot. \n Enfin, une lettre peut être répétée à plusieurs endroits...\n Indice: le mot que tu dois trouver est mythique de moovapp et est composé de 6 lettres")

#secret = getpass.getpass(prompt='Entre ton mot secret')

secret = "Sabrina"
table = []

for pendu in secret:
    table.append(pendu)
print(table)
i = 1

table_secret = []

while i <= len(table):
    table_secret.append('?')
    i = i+1

print(table_secret)

score = 10
print(score)


z = 0

score = len(table) + 7

guess_what = input("Ecris une lettre \n ")

for scan in range(0, len(table)):
    if guess_what == table[scan]:
        table_secret[scan] = guess_what
        print(table_secret)



if table == table_secret:
    print("Tu as fini par trouver le mot ! Bravo")
