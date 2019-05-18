import re
import json


def clean_text(raw_html):
    """Cleans html, new lines, and quotation marks from text"""
    clean_reg = re.compile('<.*?>')
    text = re.sub(clean_reg, '', raw_html)
    text = text.replace('\n', ' ')
    text = text.replace('\"', "\'")
    print(text)
    return text


def write_results_to_file(result, filename):
    """Input: List of json object
    Turns input into json with base object 'output' and writes
    to file 'filename'"""

    file = open(filename, 'w')
    results = {"output": result}
    to_json = json.dumps(results)
    file.write(to_json)
    file.close()


def read_from_file(filename):
    """Reads json file and returns list with 'output' header"""
    file = open(filename, encoding="utf8")
    data = json.load(file)
    return data['output']
