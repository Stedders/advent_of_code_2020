from collections import Counter


def part_1(input_data):
    input_data.append(max(input_data) + 3)
    input_data.sort()
    counter = Counter(b - a for a, b in zip([0] + input_data, input_data))
    return counter[1] * counter[3]


def part_2(input_data):
    input_data.sort()

    counter = Counter((0,))
    for num in input_data:
        counter[num] += sum(counter[i] for i in range(num - 3, num))
    return counter[input_data[-1]]


if __name__ == '__main__':
    input_data = [int(x.strip()) for x in open('input.txt').readlines()]
    result = part_1(input_data)
    print(result)
    assert result == 2592
    input_data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    result = part_2(input_data)

    print(result)
    assert result == 8

    input_data = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39,
                  11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    result = part_2(input_data)

    print(result)
    assert result == 19208
    input_data = [int(x.strip()) for x in open('input.txt').readlines()]
    result = part_2(input_data)

    print(result)
    assert result == 198428693313536
