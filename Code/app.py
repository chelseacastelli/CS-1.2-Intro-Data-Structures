from flask import Flask
from histogram import read_in_data, dictogram
from stochastic import random_word

app = Flask(__name__)

source_text = 'sample_wordz.txt'

@app.route('/')
def index():
    words = read_in_data(source_text)
    dict_hist = dictogram(words)
    return random_word(dict_hist)

if __name__ == '__main__':
    app.run(debug=True)