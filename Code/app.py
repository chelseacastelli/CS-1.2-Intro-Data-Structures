from flask import Flask, render_template, redirect, request, url_for
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

    # Get random initial word
    initial_word = choice([word for word in markov.keys() if word != '<STOP>'])
    word = stochastic_sample(markov, initial_word)

    # Check for user input, otherwise, print sentence w/ 6 words
    usr_input = request.args.get('num')
    num_of_words = int(usr_input) if (usr_input != None and usr_input != "") else 6

    # Create sentence with specified num_of_words
    output = random_walk(word, markov, num_of_words)
    sentence = create_sentence(output)

    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))