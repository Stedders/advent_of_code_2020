def part_1(input_data):
    accumalator = 0
    instruction = 0
    processed = []
    infinite = False

    while True:
        if instruction in processed:
            infinite = True
            break

        processed.append(instruction)

        try:
            op, val = input_data[instruction].split()
        except IndexError:
            break

        if op == 'nop':
            instruction += 1

        if op == 'acc':
            instruction += 1
            accumalator = eval(f'accumalator{val}')

        if op == 'jmp':
            instruction = eval(f'instruction{val}')

    return infinite, accumalator


def part_2(input_data):
    count = 0

    while count < len(input_data):
        processing_data = input_data.copy()
        op, val = processing_data[count].split()

        if op == 'acc':
            count += 1
            continue

        if op == 'nop':
            processing_data[count] = f'jmp {val}'

        if op == 'jmp':
            processing_data[count] = f'nop {val}'

        infinite, result = part_1(processing_data)
        count += 1

        if not infinite:
            break

    return result


if __name__ == '__main__':
    input_data = [x.strip() for x in open('input.txt').readlines()]
    _, result = part_1(input_data)
    print(result)
    assert result == 1654

    result = part_2(input_data)
    print(result)
    assert result == 833
