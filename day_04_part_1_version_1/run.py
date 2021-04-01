#!/usr/bin/env python3

import re

with open('input.txt') as _file:
    input_data = _file.read()

passports = re.split(r"\n\n", input_data)

valid_passports = 0

for passport in passports:
    fields = re.split(r"\s|\n", passport)

    if len(fields) == 8:
        valid_passports += 1
        continue

    if len(fields) < 7:
        continue

    if re.search('cid', passport):
        continue

    else:
        valid_passports += 1


print(valid_passports)
