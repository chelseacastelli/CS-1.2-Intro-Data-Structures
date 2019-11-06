from histogram import histogram
import sys
import random

words = " "

def random_word(histogram_DS):
    rand_index = random.randrange(len(histogram_DS) - 1)
    return list(histogram_DS)[rand_index]


# Divide num of occurances by total words
# dart = random.random()
# random can generate perfect 0.0 but not perfect 1.0
def sample_by_frequency(histogram_DS):
    pass



if __name__ == '__main__':
    params = sys.argv[1:]

    # Store params as string
    words = data = ' '.join(params)

    # Make histogram with words input to console
    histo = histogram(words)

    print(random_word(histo))