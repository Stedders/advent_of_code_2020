import string


def get_answers_by_group():
    input_data = [x.strip() for x in open('input').readlines()]

    group = {1: []}
    group_count = 1
    for answers in input_data:
        if answers == '':
            group_count += 1
            group[group_count] = []
            continue
        group[group_count].append(answers)
    return group


def part_1(group_answers):
    all_answers_per_group = []
    for group_answer in group_answers.values():
        all_answers_per_group.append(set([answer for answers in group_answer
                                          for answer in answers]))
    return sum([len(answers) for answers in all_answers_per_group])


def part_2(group_answers):
    all_answered_in_group = []
    for group_answer in group_answers.values():
        seen_answers = string.ascii_lowercase
        for answer in group_answer:
            seen_answers = [i for i in answer if i in seen_answers]
        all_answered_in_group.append(seen_answers)
    return sum([len(answers) for answers in all_answered_in_group])


if __name__ == "__main__":
    group_answers = get_answers_by_group()
    assert 6735 == part_1(group_answers)
    assert 3221 == part_2(group_answers)
