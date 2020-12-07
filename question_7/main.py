import re


def get_all_bags(data):
    bag_mappings = {}
    for line in data:
        holder, others = line.split('contain')
        m = re.match('(.+) bag[s]', holder)
        if m:
            holder = m.group(1)
        for bag in others.split(','):
            m = re.match('.*(\d+ )(\S+ \S+) bag[s]?.*', bag)
            if m:
                try:
                    bag_mappings[m.group(2)].append((m.group(1), holder))
                except KeyError:
                    bag_mappings[m.group(2)] = [(m.group(1), holder)]

    return bag_mappings


def get_holders(item, mappings):
    mapping = []
    try:
        for value in mappings[item]:
            mapping.extend(get_holders(value[1], mappings))
    except KeyError:
        pass
    mapping.append(item)
    return mapping


def part1(mappings):
    holders = []
    for item in mappings['shiny gold']:
        holders.extend(get_holders(item[1], mappings))
    holders = list(set(holders))
    return len(holders)


def get_containing_bags(container, bag_mappings, num_containers=1):
    bags_total = []
    for bag, containers in bag_mappings.items():
        for c in containers:
            if c[1] == container:
                container_count = int(c[0])
                bags_total.extend(get_containing_bags(bag, bag_mappings,
                                                      num_containers * container_count))
                bags_total.append(num_containers * container_count)
    return bags_total


def part2(bag_mappings):
    total_bags = get_containing_bags('shiny gold', bag_mappings)
    return sum(total_bags)


if __name__ == '__main__':
    input_data = [x.strip() for x in open('input.txt').readlines()]
    bag_mappings = get_all_bags(input_data)
    answer = part1(bag_mappings)
    print(answer)
    assert answer == 259

    answer = part2(bag_mappings)
    print(answer)
    assert answer == 45018
