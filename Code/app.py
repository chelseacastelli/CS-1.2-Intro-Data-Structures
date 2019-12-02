from flask import Flask, render_template, redirect, url_for
from histogram import read_in_data, dictogram
from stochastic import random_word

app = Flask(__name__)

source_text = 'sample_wordz.txt'

@app.route('/')
def index():
    words = read_in_data(source_text)
    dict_hist = dictogram(words)
    ran_word = random_word(dict_hist)
    return render_template('index.html', ran_word=ran_word)

@app.route('/new', methods=['POST'])
def new_word():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))