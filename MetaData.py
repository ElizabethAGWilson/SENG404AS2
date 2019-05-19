from Utilities import *

SE_SITE = "softwareengineering"
SO_SITE = "stackoverflow"


def get_tag_dict(filename):
    tag_dict = dict()
    from_so_file = read_from_file(filename)
    for post in from_so_file:
        # if int(post.get("score")) > 5:
        tags = post.get("tags")
        for tag in tags:
            if tag not in tag_dict:
                tag_dict[tag] = 1
            else:
                tag_dict[tag] += 1
    return tag_dict


def get_tag_dict_with_answers(filename):
    tag_dict = dict()
    from_so_file = read_from_file(filename)
    for post in from_so_file:
        if int(post.get("score")) > 0:
            tags = post.get("tags")
            for tag in tags:
                if tag not in tag_dict:
                    tag_dict[tag] = [1, int(post.get("answer_count")), int(post.get("score"))]
                else:
                    tag_dict[tag][0] += 1
                    tag_dict[tag][1] += int(post.get("answer_count"))
                    tag_dict[tag][2] += int(post.get("score"))
    return tag_dict


def write_tags_as_csv(tag_dict, filename):
    file = open(filename, "w", encoding="utf8")
    print(tag_dict)
    for key in tag_dict.keys():
        line = '{},"{}"\n'.format(key, int(tag_dict.get(key)))
        file.write(line)
    file.close()


def write_tags_with_answers_as_csv(tag_dict, filename):
    file = open(filename, "w", encoding="utf8")
    for key in tag_dict.keys():
        line = '{},"{}","{}","{}"\n'.format(key, int(tag_dict.get(key)[0]), int(tag_dict.get(key)[1]),
                                            int(tag_dict.get(key)[2]))
        file.write(line)
    file.close()


def main():
    se_tags = get_tag_dict_with_answers("data_json/results.txt")
    so_tags = get_tag_dict_with_answers("data_json/test.txt")
    all_tags = {**se_tags, **so_tags}
    print(all_tags)
    write_tags_with_answers_as_csv(all_tags, "metadata_json/tags_with_answers.csv")
    # write_results_to_file(all_tags, "metadata_json/tags_with_answers.txt")


main()
