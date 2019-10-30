import pprint

def read_in_data(fileName):

    with open(fileName, 'r') as file:
        data = file.read().splitlines()

    data = ' '.join(data)
    return data

def histogram(source_text):
    words = dict()
    for word in source_text.split():
        word = word.upper()
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
    print(pprint.pprint(u_words_hist))

    total_u_words = unique_words(u_words_hist)
    print(total_u_words)

    frequency_of_word = frequency('the', u_words_hist)
    print(frequency_of_word)