from histogram import read_in_data, histogram
import sys
from random import randrange, choices

def random_word(histogram_DS):
    rand_index = randrange(len(histogram_DS) - 1)
    return list(histogram_DS)[rand_index]

# Divide num of occurances by total words
# dart = random.random()
# random can generate perfect 0.0 but not perfect 1.0
def sample_by_frequency(histogram_DS):
    histo_keys = [key for key in histogram_DS]
    tokens = sum(histogram_DS.values())

    weighted_values = []
    for value in histo.values():
        weighted = value / tokens
        weighted_values.append(weighted)

    weighted_choice = choices(histo_keys, weighted_values, k=1)

    chosen_word = "".join(weighted_choice)
    word_index = histo_keys.index(chosen_word)

    return f"{chosen_word}: {weighted_values[word_index]}"

if __name__ == '__main__':
    # Store params as string
    words = read_in_data('sample_wordz.txt')

    # Make histogram with words input to console
    histo = histogram(words)

    # print(random_word(histo))
    print(sample_by_frequency(histo))