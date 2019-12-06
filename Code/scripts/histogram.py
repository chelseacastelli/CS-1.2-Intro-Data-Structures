from pprint import pprint
from re import split, sub

def read_in_data(fileName):

    with open(fileName, 'r') as file:
        data = file.read().lower()
        strip_punc = sub('([?:!.,;"]*)([a-z]+)([?:!.,;"]*)',r'\2', data)
        words = split(r'\s', strip_punc)

    return words

def dictogram(source_text):
    words = {}
    for word in source_text:
        if word in words:
            words[word] += 1
        else:
            words.update({word: 1})

    return words

def listogram(source_text):
    words = []
    histo = dictogram(source_text)
    for word in histo:
        words.append([word, histo[word]])
    return words

def tuplogram(source_text):
    words = []
    histo = dictogram(source_text)
    for word in histo:
        words.append((word, histo[word]))
    return words

def unique_words(histogram_DS):
    return len(histogram_DS)

def frequency(word, histogram_DS):
    return histogram_DS.get(word)


if __name__ == "__main__":
    words = read_in_data('sample_wordz.txt')

    dict_hist = dictogram(words)
    list_hist = listogram(words)
    tup_hist = tuplogram(words)

