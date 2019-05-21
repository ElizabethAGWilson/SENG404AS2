import re
import json

elicitation = ["business", "client-relations", "communication", "customer-relations", "functional-requirements",
               "planning",
               "project-planning", "quality-attributes", "system-requirements"]
documentation = ["diagrams", "documentation", "modeling", "prototyping", "report", "specifications", "srs", "uml",
                 "use-case",
                 "user-stories", "user-story"]

analysis = ["analysis", "estimation", "metrics", "systems-analysis", "enterprise-architect"]

validation = ["acceptance-testing", "quality", "testing", "usability", "user-experience", "validation", "verification"]

management = ["management", "product-management", "project-management", "requirements-management", "scope",
              "scope-creep"]

implement = ["api", "architecture", "cardinality", "database-design", "design", "iphone", "language-agnostic", "tfs",
             "tfs2010",
             "web-development"]

methodology = ["agile", "development-process", "extreme-programming", "kanban", "methodology", "scrum", "sdlc",
               "waterfall"]

misc = ["engineering", "freelancing", "productivity", "project", "software", "standards", "system", "teamwork",
        "terminology", "tools"]


def read_ids_from_csv():
    line_list = []
    with open("data_csv/filtered_SE_ids.txt", "r") as file:
        line_list.extend(file.readlines())
    with open("data_csv/filtered_SO_ids.txt", "r") as file:
        line_list.extend(file.readlines())
    i = 0
    while i < len(line_list):
        line_list[i] = int(line_list[i].strip('\n'))
        i += 1
    return line_list

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
