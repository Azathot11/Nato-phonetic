import pandas

nato_phonetic = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_phonetic)

user_input = input('Enter your name: ')

# for letter in user_input.upper():
nato_words_generated = {row.letter: row.code for (index, row) in nato_phonetic.iterrows() if
                        row.letter in user_input.upper()}
print(nato_words_generated)
