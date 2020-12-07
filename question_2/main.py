if __name__ == "__main__":
    valid_paswords = 0
    for line in [x.strip() for x in open("input.txt").readlines()]:
        requirements, password = [y.strip() for y in line.split(":")]
        count, letter = requirements.split(' ')
        min_count, max_count = [int(y) for y in count.split("-")]

        letter_count = password.count(letter)
        if letter_count >= min_count and letter_count <= max_count:
            valid_paswords += 1
    print(f'Part 1. {valid_paswords}')

    valid_paswords = 0
    for line in [x.strip() for x in open("input.txt").readlines()]:
        requirements, password = [y.strip() for y in line.split(":")]
        count, letter = requirements.split(' ')
        pos_1, pos_2 = [int(y) for y in count.split("-")]

        if (password[pos_1 - 1] == letter) ^ (password[pos_2 - 1] == letter):
            valid_paswords += 1
    print(f'Part 2. {valid_paswords}')
