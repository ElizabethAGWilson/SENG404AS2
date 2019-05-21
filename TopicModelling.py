import pandas as panda
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from Utilities import *

import nltk
nltk.download('wordnet')

allowed_words = ["uml"]

# panda.read_csv('output.csv', error_bad_lines=False)
example = "I have a set of User Stories and I have a set of business rules (primarily laws binding my requirements to "\
          "be compliant). In Agile SDLC I'm not sure where these 'rules' are attached to my user stories.  For " \
          "example, a user story like:     As a doctor I want to add patient information in order to create a new " \
          "patient file. "


def stem_lem(text):
    lemma = WordNetLemmatizer().lemmatize(text)
    stem = PorterStemmer().stem(lemma)
    return stem


def is_valid_token(token):
    if token in allowed_words:
        return True
    return token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3


def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if is_valid_token(token):
            result.append(stem_lem(token))

    return result


def strip_bytes(line):
    """removes bytes things that shouldn't be there"""
    for i, word in enumerate(line):
        line[i] = word[2:-1]

    return line


def read_data(infile):
    """Read data from infile. Returns list of tuples of:
    (id, title, body)"""
    file = open(infile, "rb").readlines()
    data = []

    for line in file:
        line = line.strip().split(b"\t")
        line = strip_bytes(line)
        q_id, title, body = line
        data.append((int(q_id), title, body))

    return data


def process_data(data):
    """Puts title and body through lemmatization
    Returns list of tuples with the question id,
    and a list of the topic words"""
    result = []
    for q_id, title, body in data:
        text = title + body
        processed = preprocess(text)
        result.append((q_id, processed))

    return result


def make_dictionary(data):
    """does a thing?"""
    result = []

    for q_id, tokens in data:
        dictionary = dict()
        for token in tokens:
            dictionary[token] = dictionary.get(token, 0) + 1
        result.append((q_id, dictionary))

    return result


def generate_master(dictionaries):
    master_dictionary = dict()

    for q_id, dictionary in dictionaries:
        for key in dictionary.keys():
            master_dictionary[key] = master_dictionary.get(key, 0) + 1

    return master_dictionary


def prune_common_tokens(dictionaries, master_dictionary):
    common_tokens = []
    uncommon = []
    allowed_tokens = ['document', 'function']
    max_occurrence = 150
    min_occurence = len(dictionaries) // 10

    print('uml stuff')
    print(master_dictionary['uml'])
    print(min_occurence)

    for key, value in master_dictionary.items():
        if value > max_occurrence:
            common_tokens.append(key)
            print(key)
        elif value < min_occurence:
            common_tokens.append(key)
        else:
            uncommon.append(key)

    # common_tokens -= allowed_tokens

    for dictionary in dictionaries:
        for token in common_tokens:
            if token in dictionary:
                del dictionary[token]
                print("deleted a thing")

    print(len(common_tokens))
    print(len(master_dictionary))

    print(master_dictionary['function'])


def main():
    """does the things"""
    infile_SE = "filtered_SE.txt"
    infile_SO = "filtered_SO.txt"
    # outfile = "SE_stem_lem.txt"

    data_SE = read_data(infile_SE)
    data_SO = read_data(infile_SO)
    data = data_SE + data_SO
    processed_data = process_data(data)
    #  todo this needs to be both SE and SO
    dictionaries = make_dictionary(processed_data)
    # for dictionary in dictionaries:
    #     print(dictionary)
    master_dictionary = generate_master(dictionaries)
    prune_common_tokens(dictionaries, master_dictionary)


main()
