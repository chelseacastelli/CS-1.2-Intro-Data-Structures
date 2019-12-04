import sys
from re import split, sub

def read_in_data(fileName):
    with open(fileName, 'r') as file:
        data = file.read()

    return data

def clean_text(fileName):
    data = fileName.lower()
    strip_punc = sub('([?:!.,;"]*)([a-z]+)([?:!.,;"]*)',r'\2', fileName)
    words = split(r'\s', strip_punc)

    return words

def add_start(text):
    '''Adds an start signaler to last word'''
    text.insert(0, '<START>')
    return text

def add_stop(text):
    '''Adds an end stop signaler to last word'''
    text.append('<STOP>')
    return text

def create_sentence(text):
    cap = " ".join(text).capitalize()
    sentence = f"{cap}."
    return sentence
