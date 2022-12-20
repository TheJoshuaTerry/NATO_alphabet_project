import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')
NATO_dict = {row.letter: row.code for (index, row) in df.iterrows()}

choice = input('Enter a word: ').upper()

NATO_list = [NATO_dict[letter] for letter in choice]

print(NATO_list)


