from random import choices

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

