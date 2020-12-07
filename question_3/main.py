if __name__ == "__main__":
    puzzle_input = open('input.txt').read().splitlines()

    trees = 0
    for i, line in enumerate(puzzle_input):
        if line[(i * 3) % len(line)] == '#':
            trees += 1
    print(trees)

    trees = 0
    results = [0, 0, 0, 0, 0]
    for i, line in enumerate(puzzle_input):
        if line[(i * 1) % len(line)] == '#':
            results[0] += 1
        if line[(i * 3) % len(line)] == '#':
            results[1] += 1
        if line[(i * 5) % len(line)] == '#':
            results[2] += 1
        if line[(i * 7) % len(line)] == '#':
            results[3] += 1

    for i, line in enumerate(puzzle_input[::2]):
        if line[(i * 1) % len(line)] == '#':
            results[4] += 1

    print(results[0]*results[1]*results[2]*results[3]*results[4])

