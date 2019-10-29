

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
            # unique_words.update(word += 1)
            words[word] += 1
        else:
            words.update({word: 1})

    return words

def unique_words(histogram_dictionary):
    total = 0
    for key in histogram_dictionary:
        total += histogram_dictionary[key]

    return total

def frequency(word, histogram):
    pass

words = read_in_data('sample_wordz.txt')
# print(words)
u_words_hist = histogram(words)
print(u_words_hist)

total_u_words = unique_words(u_words_hist)
print(total_u_words)
