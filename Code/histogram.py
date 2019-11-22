from pprint import pprint
from re import split, sub

def read_in_data(fileName):

    with open(fileName, 'r') as file:
        data = file.read().lower()
        strip_punc = sub('([?:!.,;"]*)([a-z]+)([?:!.,;"]*)',r'\2', data)
        words = split(r'\s', strip_punc)

    return words

def histogram(source_text):
    words = dict()
    for word in source_text:
        word = word
        if word in words:
            words[word] += 1
        else:
            words.update({word: 1})

    return words

def unique_words(histogram_DS):
    return len(histogram_DS)

def frequency(word, histogram_DS):
    word = word.upper()
    return histogram_DS.get(word)


if __name__ == "__main__":
    words = read_in_data('sample_wordz.txt')

    u_words_hist = histogram(words)
    pprint(u_words_hist)
