from random import randint, randrange, choice
from cleanup import read_in_data, clean_text, add_stop
from dictogram import Dictogram

def markov_histo(corpus):
    '''Creates markov chain with histogram'''
    markov_dict = {}

    for i in range(len(corpus)-1):
        first = corpus[i]
        second = corpus[i+1]

        if first not in markov_dict.keys():
            markov_dict[first] = Dictogram()

        markov_dict.get(first).add_count(second)

    return markov_dict


def stochastic_sample(markov, word):
    '''Gets a weighted random word from given word's histo'''
    histo = markov.get(word)

    if word in markov:
        return histo.sample()

def random_walk(word, markov, steps):
    '''Given a starting word, picks a random word from markov list and walks to given number of steps to generate a sentence'''

    sentence = []

    i = 0
    while i != steps:
        sentence.append(word)
        next_word = stochastic_sample(markov, word)

        if next_word == '<STOP>':
            break

        word = next_word
        i += 1

    return sentence

if __name__ == "__main__":
    file = 'sample_wordz.txt'
    text = read_in_data(file)
    clean = clean_text(text)
    endstop = add_stop(clean)

    markov = markov_histo(endstop)

    init_word = choice([word for word in endstop if word != endstop[:-1]])

    word = stochastic_sample(markov, init_word)
    random_int = randint(3,10)
    walk = random_walk(init_word, markov, random_int)

    cap = " ".join(walk).capitalize()
    print(f"{cap}.")