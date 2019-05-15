import requests
import json
import re

API_KEY = "xqIpWTa4rMFb4VMhxLITYQ(("
SE_SITE = "softwareengineering"
SO_SITE = "stackoverflow"
OUT_FILE = "results.txt"
QUERY_FORMAT = "http://api.stackexchange.com/2.2/{}?tagged={}&site={}&filter=withbody&pagesize=100&page={}"


def clean_text(raw_html):
    clean_reg = re.compile('<.*?>')
    text = re.sub(clean_reg, '', raw_html)
    text = text.replace('\n', ' ')
    text = text.replace('\"', "\'")
    print(text)
    return text


def query_questions(site_name, tag):
    """Gets all questions from site_url that are tagged with tag"""
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


def write_results_to_file(result):
    file = open("test.txt", 'w')
    # print(result.content)
    # data = json.loads(result.text)
    # print(data["items"])
    results = {"questions": result}
    to_json = json.dumps(results)
    file.write(to_json)
    file.close()

    # for repo_name, average in data:
    #     result_string = RESULT_TEMPLATE.format(repo_name, average)
    #     file.write(result_string)


# def combine_results():
#     data1 = read_from_file("results1.txt")
#     data2 = read_from_file("results2.txt")
#     data3 = read_from_file("results3.txt")
#     data4 = read_from_file("results4.txt")
#
#     results = {"questions": data1 + data2 + data3 + data4}
#     to_json = json.dumps(results)
#
#     file = open("results.txt", "w")
#     file.write(to_json)


def read_from_file(filename):
    file = open(filename, encoding="utf8")
    data = json.load(file)
    print(len(data["questions"]))
    return data['questions']


def make_csv():
    file = open("so_output.csv", "w", encoding="utf8")
    data = read_from_file("test.txt")

    for dat in data:
        id = dat["question_id"]
        title = dat["title"]
        body = clean_text(dat["body"])

        line = '{},"{}","{}"\n'.format(id, title, body)
        file.write(line)
    file.close()

    print(data)


def main():
    """does the things"""
    questions = query_questions(SO_SITE, "requirements")
    print("There are this many: {}".format(len(questions)))
    write_results_to_file(questions)
    # combine_results()
    # read_from_file("results.txt")
    make_csv()


main()
