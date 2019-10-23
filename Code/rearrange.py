from random import shuffle
import sys

words = []

def randomize_words():
    shuffle(words)
    print(' '.join(words))


if __name__ == "__main__":
    params = sys.argv[1:]

    for param in params:
        words.append(str(param))

    randomize_words()


