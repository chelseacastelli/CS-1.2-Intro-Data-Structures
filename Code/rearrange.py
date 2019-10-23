from random import choice
import sys

words = []

def randomize_words():
    words_after_shuffle = []

    while len(words) > 0:
         random_word = choice(words)
         words_after_shuffle.append(random_word)
         words.remove(random_word)

    print(' '.join(words_after_shuffle))


if __name__ == "__main__":
    params = sys.argv[1:]

    for param in params:
        words.append(str(param))

    randomize_words()


