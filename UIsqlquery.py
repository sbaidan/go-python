## Importation du module SQLite 3

import sqlite3
connexion = sqlite3.connect('chinook.db') ## On se connecte à la base donnée
c = connexion.cursor() ## Deuxième étape, on créé un curseur
query = str(input("Entre la rquête SQL de ton choix "))
c.execute(query) # avec c.execute (On écrit la query)
## print(c.fetchall()) ## Ici on peut afficher uniquement certains éléments si on veut
## Variantes existantes : fetchone et fetchmany(param) ci-dessous
print("")
print(c.fetchall())
