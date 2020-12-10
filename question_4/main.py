import re

keys = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
input = open("input").read().strip()
records = input.split("\n\n")
passports = []
for record in [x.replace("\n", " ").split(" ") for x in records]:
    passport = {}
    for item in record:
        key, val = item.split(":")
        passport[key] = val
    passports.append(passport)
valid = [keys.issubset(p.keys()) for p in passports]
print(valid.count(True))

valid_count = 0
for passport in passports:
    try:
        byr = int(passport["byr"])
        if byr < 1920 or byr > 2002:
            continue
    except KeyError:
        continue
    try:
        iyr = int(passport["iyr"])
        if iyr < 2010 or iyr > 2020:
            continue
    except KeyError:
        continue
    try:
        eyr = int(passport["eyr"])
        if eyr < 2020 or eyr > 2030:
            continue
    except KeyError:
        continue

    try:
        ecl = passport["ecl"]
        if ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
    except KeyError:
        continue

    try:
        pid = passport["pid"]
        if len(pid) == 9 and int(pid) > 0:
            continue
    except KeyError:
        continue

    hgt = passport["hgt"]
    m = re.compile("(\d+)(cm|in)").match(hgt)
    if m:
        key = m.group(2)
        val = int(m.group(1))
        if key == "cm" and (val < 150 or val > 193):
            continue
        elif key == "int" and (val < 59 or val > 76):
            continue
    else:
        continue

    hcl = passport["hcl"]
    m = re.compile("#[0-9a-f]]{9}").match(hcl)
    if not m:
        continue
    valid_count += 1

print(valid_count)
count = 0
for idx, v in enumerate(passports):
    keys = passports[idx]
    if not all(k in keys for k in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}):
        continue
    if not keys['byr'].isdigit():
        continue
    if not (1920 <= int(keys['byr']) <= 2002):
        continue
    if not keys['iyr'].isdigit():
        continue
    if not (2010 <= int(keys['iyr']) <= 2020):
        continue
    if not keys['eyr'].isdigit():
        continue
    if not (2020 <= int(keys['eyr']) <= 2030):
        continue
    if not keys['pid'].isdigit():
        continue
    if not len(keys['pid']) == 9:
        continue
    if not keys['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        continue
    if not keys['hcl'].startswith('#') or not len(keys['hcl']) == 7:
        continue
    if not (keys['hcl'][1:].isalnum()):
        continue
    if keys['hgt'][-2:] not in {'cm', 'in'}:
        continue
    if not keys['hgt'][:-2].isdigit():
        continue
    if keys['hgt'].endswith('cm') and not (150 <= int(keys['hgt'][:-2]) <= 193):
        continue
    if keys['hgt'].endswith('in') and not (59 <= int(keys['hgt'][:-2]) <= 76):
        continue
    count += 1
print(count)
