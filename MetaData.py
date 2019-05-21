from Utilities import *

SE_SITE = "softwareengineering"
SO_SITE = "stackoverflow"


def get_tag_dict_with_answers(filename, ids, area_list):
    tag_dict = dict()
    from_so_file = read_from_file(filename)
    for post in from_so_file:
        if int(post.get("score")) > 0 and int(post.get("question_id")) in ids:
            tags = post.get("tags")
            for tag in tags:
                if tag in area_list:
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
    ids = read_ids_from_csv()
    # se_tags = get_tag_dict_with_answers("data_json/results.txt", ids)
    # so_tags = get_tag_dict_with_answers("data_json/test.txt", ids)
    # all_tags = {**se_tags, **so_tags}
    elicitation_dict_se = get_tag_dict_with_answers("data_json/results.txt", ids, elicitation)
    elicitation_dict_so = get_tag_dict_with_answers("data_json/test.txt", ids, elicitation)
    all_elicitation = {**elicitation_dict_se, **elicitation_dict_so}
    write_tags_with_answers_as_csv(all_elicitation, "metadata_json/elicitation.csv")

    elicitation_dict_se = get_tag_dict_with_answers("data_json/results.txt", ids, documentation)
    elicitation_dict_so = get_tag_dict_with_answers("data_json/test.txt", ids, documentation)
    all_elicitation = {**elicitation_dict_se, **elicitation_dict_so}
    write_tags_with_answers_as_csv(all_elicitation, "metadata_json/documentation.csv")

    elicitation_dict_se = get_tag_dict_with_answers("data_json/results.txt", ids, analysis)
    elicitation_dict_so = get_tag_dict_with_answers("data_json/test.txt", ids, analysis)
    all_elicitation = {**elicitation_dict_se, **elicitation_dict_so}
    write_tags_with_answers_as_csv(all_elicitation, "metadata_json/analysis.csv")

    elicitation_dict_se = get_tag_dict_with_answers("data_json/results.txt", ids, validation)
    elicitation_dict_so = get_tag_dict_with_answers("data_json/results.txt", ids, validation)
    all_elicitation = {**elicitation_dict_se, **elicitation_dict_so}
    write_tags_with_answers_as_csv(all_elicitation, "metadata_json/validation.csv")

    elicitation_dict_se = get_tag_dict_with_answers("data_json/results.txt", ids, management)
    elicitation_dict_so = get_tag_dict_with_answers("data_json/test.txt", ids, management)
    all_elicitation = {**elicitation_dict_se, **elicitation_dict_so}
    write_tags_with_answers_as_csv(all_elicitation, "metadata_json/management.csv")

    elicitation_dict_se = get_tag_dict_with_answers("data_json/results.txt", ids, implement)
    elicitation_dict_so = get_tag_dict_with_answers("data_json/results.txt", ids, implement)
    all_elicitation = {**elicitation_dict_se, **elicitation_dict_so}
    write_tags_with_answers_as_csv(all_elicitation, "metadata_json/implement.csv")

    elicitation_dict_se = get_tag_dict_with_answers("data_json/results.txt", ids, methodology)
    elicitation_dict_so = get_tag_dict_with_answers("data_json/test.txt", ids, methodology)
    all_elicitation = {**elicitation_dict_se, **elicitation_dict_so}
    write_tags_with_answers_as_csv(all_elicitation, "metadata_json/methodology.csv")

    elicitation_dict_se = get_tag_dict_with_answers("data_json/results.txt", ids, misc)
    elicitation_dict_so = get_tag_dict_with_answers("data_json/test.txt", ids, misc)
    all_elicitation = {**elicitation_dict_se, **elicitation_dict_so}
    write_tags_with_answers_as_csv(all_elicitation, "metadata_json/misc.csv")

    # write_results_to_file(all_tags, "metadata_json/tags_with_answers.txt")


main()
