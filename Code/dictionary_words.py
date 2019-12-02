
import random
import sys
import time


def read_in_data(fileName):
    '''Read data in from file'''
    with open(fileName, 'r') as file:
        data = file.read().splitlines()

    return data


def get_random_words(words, num_words):
    '''Get random words from file'''
    new_words = []
    for iteration in range(num_words):
        rand_index = random.randrange(len(words) - 1)
        new_words.append(words[rand_index])

    return new_words


def print_sentence(words):
    print(' '.join(words))


if __name__ == '__main__':

    dictionary_words = read_in_data('/usr/share/dict/words')

    if len(sys.argv) >= 2:
        num_words = int(sys.argv[1])

        start = time.perf_counter()
        words = get_random_words(dictionary_words, num_words)
        elapsed = time.perf_counter()

        print('\n')
        print_sentence(words)

        print(f'\nTime spent getting random words: {elapsed - start}\n')



    else:
        print("Need argument for number of words to pick")
