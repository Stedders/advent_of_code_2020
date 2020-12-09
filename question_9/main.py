def part_1(input_data):
    start, header = 0, 25
    for val in input_data[header:]:
        valid = False
        seen = input_data[start:header]
        for seen_val in seen:
            if (val % seen_val) in seen:
                valid = True
        if not valid:
            return val
        start += 1
        header += 1


def part_2(invalid, test_data):
    for idx in range(len(test_data)):
        results = [sum(test_data[idx:end]) for end in range(len(test_data) - idx)]
        if invalid in results:
            result_pos = results.index(invalid)
            return min(test_data[idx:result_pos]) + max(test_data[idx:result_pos])


if __name__ == '__main__':
    input_data = [int(x.strip()) for x in open('input.txt').readlines()]

    result = part_1(input_data)
    print(result)
    assert result == 133015568
    result = part_2(result, input_data)
    print(result)
    assert result == 16107959
