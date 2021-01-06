import pandas

csv = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(csv)

dict = { row.letter:row.code for (index, row) in df.iterrows()}


def codebreaker():
    try:
        username = input("What is your name?\n")
        code = [dict[letter] for letter in username.upper()]
        print(code)

    except KeyError:
        print("Sorry, please make sure input is letters only")
        codebreaker()

codebreaker()