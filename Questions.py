import requests
from Utilities import *

API_KEY = "xqIpWTa4rMFb4VMhxLITYQ(("
SE_SITE = "softwareengineering"
SO_SITE = "stackoverflow"
OUT_FILE = "results.txt"
QUERY_FORMAT = "http://api.stackexchange.com/2.2/{}?tagged={}&site={}&filter=withbody&pagesize=100&page={}"


def query_questions(site_name, tag):
    """Gets all questions from site_url that are tagged with tag
    Returns list of questions which are json objects"""
    page = 1
    more = True
    all_data = []

    while more and page < 10:
        query = QUERY_FORMAT.format("questions", tag, site_name, page)
        result = requests.get(url=query)
        data = json.loads(result.text)
        more = data['has_more']
        questions = data['items']
        all_data.extend(questions)
        page += 1
        print(data)

    return all_data


def make_csv(filename):
    """Extract title, questions body and id from json and write to csv"""
    file = open(filename, "w", encoding="utf8")
    data = read_from_file("test.txt")

    for dat in data:
        id = dat["question_id"]
        title = dat["title"]
        body = clean_text(dat["body"])

        line = '{},"{}","{}"\n'.format(id, title, body)
        file.write(line)
    file.close()

    print(data)


def filter_questions(in_file, out_file):
    """Takes csv file and creates csv file containing all valid question ids"""
    data = open(in_file, "rb").readlines()
    outfile = open(out_file, "w")
    valid_ids = []

    for line in data:
        line = line.strip().split(b"\t")
        if len(line) == 4:
            info = tuple(line)
            # question_id, title, body, boolean = line
            if line[3] == b'TRUE':
                valid_ids.append(info)

    for dat in valid_ids:
        qid, title, body, _ = dat
        outfile.write('{}\t{}\t{}\n'.format(str(qid), str(title), str(body)))


def main():
    """Queries API to get questions, write these to file and produces csv"""
    # questions = query_questions(SO_SITE, "requirements")
    # print("There are this many: {}".format(len(questions)))
    # write_results_to_file(questions, "output.txt")
    # make_csv()

    filter_questions("SE.tsv", "filtered_SE.txt")


main()
