import random
import json

# Initialize score and number of answered words
punkte = 0
summe_words = 0

# --- Load vocabulary from JSON file ---
# Open the file in read mode and load it as a Python dictionary
with open("vocabulary.json", "r", encoding="utf-8") as file:
    vocabulary = json.load(file)
print("Vokabeln geladen:", len(vocabulary))

# --- Prepare a list of all German words ---
# Convert dictionary keys to a list and shuffle them for random order
words = list(vocabulary.keys())
random.shuffle(words)

for random_word in words:
    print(f"Wie heißt '{random_word}' auf Englisch?")
    choice = input("> ")

    if (choice == 'q'):
        break

    #Zahl von Wörter
    summe_words += 1
    value_vocab = vocabulary[random_word]
    if (value_vocab.lower() == choice.lower()):
        print("Richtig!")
        punkte += 1
    else:
        print(f"Falsch! Richtige Antwort: {value_vocab}")


if summe_words > 0:
    quote = (punkte / summe_words) * 100
    print(f"Spiel beendet. Deine Punkte: {punkte} von {summe_words}")
    print(f"Du hast {quote:.1f} %")
else:
    print("Keine Antworten gegeben.")