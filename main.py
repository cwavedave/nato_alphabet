import pandas

csv = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(csv)

dict = { row.letter:row.code for (index, row) in df.iterrows()}

username = input("What is your name?\n")

code = [dict[letter] for letter in username.upper()]
print(dict)

print(code)
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

