import pandas

nato_phonetic = pandas.read_csv('nato_phonetic_alphabet.csv')


# print(nato_phonetic)
def generate_nato_words():
    word = input('Enter your name: ')
    try:
        nato_words_generated = [nato_phonetic.loc[nato_phonetic.letter == letter.upper(), 'code'].item() for letter in
                                word]
    except ValueError:
        print('Sorry, only letters in the alphabet please.')
        generate_nato_words()
    else:
        print(nato_words_generated)


generate_nato_words()
