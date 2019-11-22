
from random import choice
import sys


def randomize_words(words):
    '''Shuffle words'''
    words_after_shuffle = []

    while len(words) > 0:
         random_word = choice(words)
         words_after_shuffle.append(random_word)
         words.remove(random_word)

    print(' '.join(words_after_shuffle))


def reverse_word(words):
    '''Reverse word(s) by each letter'''
    for word in words:
        print(word[::-1], end=' ')


def reverse_sentence(words):
    '''Reverse order of words in sentence'''
    for word in words[::-1]:
        print(word, end=' ')


# MAIN
if __name__ == "__main__":
    words = []
    try_again = True

    params = sys.argv[1:]


    # If there are multiple arguments given, append to words list
    if len(params) >= 1:
        for param in params:
            words.append(str(param))

    # Check for no arugments given
    elif len(params) == 0:
        print("\nNeed arguments\nTerminating...\n")
        exit()

    # Loop for invalid input
    while try_again:

        usr_inpt = input("Do you want to shuffle your words (sh),\nreverse a word (rw),\nor reverse a sentence (rs)? ")

        if usr_inpt.lower() == 'sh':
            randomize_words(words)
            try_again = False

        elif usr_inpt.lower() == 'rs':
            reverse_sentence(words)
            try_again = False

        elif usr_inpt.lower() == 'rw':
            reverse_word(words)
            try_again = False

        else:
            print('\nInvalid input..')



