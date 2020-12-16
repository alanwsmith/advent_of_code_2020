#!/usr/bin/env python3

import re


# That's not the right answer; your answer is too high.
# If you're stuck, make sure you're using the full input data;
# there are also some general tips on the about page,
# or you can ask for hints on the subreddit. Please
# wait one minute before trying again. (You guessed 187.)
# [Return to Day 4]



def check_if_valid(fields):

    details = {k: v for k, v in [item.split(":") for item in fields]}

    try:
        details['byr'] = int(details['byr'])
        details['iyr'] = int(details['iyr'])
        details['eyr'] = int(details['eyr'])
    except:
        return False


    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if details['byr'] < 1920:
        return False
    if details['byr'] > 2002:
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if details['iyr'] < 2010:
        return False
    if details['iyr'] > 2020:
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if details['eyr'] < 2020:
        return False
    if details['eyr'] > 2030:
        return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    height_match = re.search(r"^(\d+)(cm|in)$", details['hgt'])
    if not height_match:
        return False
    else:
        if height_match.group(2) == 'cm':
            if int(height_match.group(1)) < 150:
                return False
            if int(height_match.group(1)) > 193:
                return False
        else:
            if int(height_match.group(1)) < 59:
                return False
            if int(height_match.group(1)) > 76:
                return False

        #print(height_match.group(1))

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hair_match = re.search(r'#([0-9a-f]{6})$', details['hcl'])
    if not hair_match:
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    eye_match = re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)', details['ecl'])

    if not eye_match:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    id_match = re.search(r'^\d{9}', details['pid'])

    if not id_match:
        return False



    return True


with open('passport_validator_input.txt') as _file:
    input_data = _file.read()

passports = re.split(r"\n\n", input_data)

valid_passports = 0

for passport in passports:
    fields = re.split(r"\s|\n", passport)

    if len(fields) < 7:
        continue

    elif len(fields) == 8:
        if check_if_valid(fields):
            valid_passports += 1
        continue

    elif re.search('cid', passport):
        continue

    else:
        if check_if_valid(fields):
            valid_passports += 1


print(valid_passports)
