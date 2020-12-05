def get_seat_id(bp):
    rows = [x for x in range(0, 128)]
    seats = [x for x in range(0, 8)]
    row_bp = bp[:7]
    seats_bp = bp[-3:]

    for code in row_bp:
        half = int(len(rows) / 2)
        rows = rows[:half] if code == 'F' else rows[half:]
    row = rows[0]

    for code in seats_bp:
        half = int(len(seats) / 2)
        seats = seats[:half] if code == 'L' else seats[half:]
    seat = seats[0]

    return row * 8 + seat


def get_ticket_ids_from_boarding_pass_file(filename):
    return [get_seat_id(x.strip())
            for x in open(filename).readlines()]


def part_1():
    bp_ids = get_ticket_ids_from_boarding_pass_file('input')
    max_id = max(bp_ids)
    print(max_id)
    return max_id


def part_2():
    all_ids = [r * 8 + s
               for s in [x for x in range(0, 8)]
               for r in [y for y in range(1, 127)]]

    bp_ids = get_ticket_ids_from_boarding_pass_file('input')

    seats = [seat_id for seat_id in all_ids if all((seat_id not in bp_ids,
                                                    seat_id + 1 in bp_ids,
                                                    seat_id - 1 in bp_ids))]

    return seats[0]


assert part_1() == 850
assert part_2() == 599
