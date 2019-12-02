from pprint import pprint
from re import split, sub

def read_in_data(fileName):

    with open(fileName, 'r') as file:
        data = file.read().lower()
        strip_punc = sub('([?:!.,;"]*)([a-z]+)([?:!.,;"]*)',r'\2', data)
        words = split(r'\s', strip_punc)

    return words