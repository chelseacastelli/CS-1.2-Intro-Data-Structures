from random import randint, randrange, choice
from cleanup import read_in_data, clean_text, add_stop
from dictogram import Dictogram
from queue import Queue

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

def higher_markov(corpus):
    '''Creates 2nd order markov chain with histogram'''
    markov_dict = {}

    for i in range(len(corpus)-1):
        first = corpus[i]
        second = corpus[i+1]

        if second != '<STOP>':
            third = corpus[i+2]

            key = (first, second)
            if key not in markov_dict.keys():
                markov_dict[key] = Dictogram()

            markov_dict.get(key).add_count(third)

    return markov_dict

def stochastic_sample(markov, word):
    '''Gets a weighted random word from given word's histo'''
    histo = markov.get(word)

    if word in markov:
        return histo.sample()

def random_state(markov):
    '''Gets states with word as first in tuple'''
    states = [state for state in markov.keys()]
    return choice(states)


def random_walk(markov, steps):
    '''Given a starting word, picks a random word from markov list and walks to given number of steps to generate a sentence'''

    sentence = []
    q = Queue()

    state = random_state(markov)
    q.enqueue(state[0])
    sentence.append(state[0])
    q.enqueue(state[1])
    sentence.append(state[1])

    i = 2
    while i != steps:
        next_word = stochastic_sample(markov, state)

        if len(q) == 3:
            q.dequeue()

        q.enqueue(next_word)
        sentence.append(next_word)

        state = (state[1], next_word)

        if next_word == '<STOP>':
            break

        i += 1

    return sentence

if __name__ == "__main__":
    file = 'static/tumblr_wordz.txt'
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