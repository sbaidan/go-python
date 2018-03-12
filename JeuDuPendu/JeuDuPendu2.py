import random  ## Module pour générer des nombres aléatoirements
import time

##1st step open the file containing the different words

f =  open("Names.txt", "r")
prepare_list = f.read()

## Now we've got the whole text let's split it according to a rule we establish
## and put it in a list

liste = prepare_list.split("\n")

# Take a random element of the list : this will be our secret word to guess

secret = random.choice(liste)

# Create a list that will split the text between each caracter and put them into a new list

table = []

for pendu in secret:
    table.append(pendu)

i = 1

# Now we create a table which is used to inform the user about the missing
# letters and how many of them he found

table_secret = []

while i <= len(table):
    table_secret.append('_')
    i = i+1

print(table_secret)

# A little code that informs the users on how many attemps he bahouais
# to find the word

score = 10
print("You start with ", score, "attemps")

# Measure the value before starting the game

t0 = time.time()


# Let the game start.

z = 0

while z < len(table):  #We are going to scan each
    guess_what = input("Ecris une lettre \n ")  #
    letterFound = False
    for letterIndex in range(0, len(table)):
        if guess_what == table[letterIndex]:
            table_secret[letterIndex] = guess_what
            letterFound = True
    if letterFound == True:
        print("Pas mal! Tu as trouvé une lettre!")
        print(table_secret)
        z = z + 1

    else:
        score = score - 1
        print("Non, c'est faux. Tu dois retenter l'exercice ! Il te reste ", score, " essais")
        if score <= 0 :
            print("Tu as perdu. Le mot à trouver était...", secret)
            t1 = time.time()
            print("Tu as mis " , t1-t0 , "secondes pour faire ce score misérable")
            break

fin = "".join(table_secret)

print(fin)

if table == table_secret:
    t1 = time.time()
    print("Tu as fini par trouver le mot ! Bravo")
    current_time = int(t1-t0)
    nb_essai = 10-score
    print("Il t'a fallu ", current_time, " secondes" )
    print("Tu as réussi en ", nb_essai)

    records = str(nb_essai) + "," + str(current_time)

    z = open("records.txt", "r")
    read_records = z.read()
    liste_read_records = read_records.replace("\n", "").split(",")
    print(liste_read_records)

    ## until here everything's working
    liste_read_records = list(map(int,liste_read_records))
    if liste_read_records[0] > nb_essai:
        new_score = open("records.txt", "w")
        new_score.write(records)
        print("Meilleur score à ce jour: " , read_records)
        new_score.close() ## Apparently when you call the method open you have to close it at the end of the writing
