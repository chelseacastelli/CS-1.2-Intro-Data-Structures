from flask import Flask, render_template, redirect, url_for
from cleanup import read_in_data, clean_text, add_stop, create_sentence
from random import randint, choice
from markov_chain import markov_histo, stochastic_sample, random_walk

app = Flask(__name__)

source_text = 'static/tumblr_wordz.txt'

words = read_in_data(source_text)
cleaned_text = clean_text(words)
stripped_words = add_stop(cleaned_text)
markov = markov_histo(stripped_words)

@app.route('/')
def index():

    initial_word = choice([word for word in markov.keys() if word != '<STOP>'])
    word = stochastic_sample(markov, initial_word)
    random_int = randint(5, 15)
    output = random_walk(word, markov, random_int)

    sentence = create_sentence(output)

    return render_template('index.html', sentence=sentence)

@app.route('/new', methods=['POST'])
def new_word():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))