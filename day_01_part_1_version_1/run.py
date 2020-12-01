#!/usr/bin/env python

import re
import sys

numbers_low_to_high = []

with open('input.txt', 'r') as input_file:
    for line in input_file:
        if re.search(r'^\d', line):
            numbers_low_to_high.append(int(line))

numbers_low_to_high.sort()
numbers_high_to_low = list(reversed(numbers_low_to_high))

for high_num in numbers_high_to_low:
    for low_number in numbers_low_to_high:
        num_sum = high_num + low_number
        print(f'{high_num} + {low_number} = {num_sum}')
        if num_sum > 2020:
            print('To high...')
            break
        elif num_sum < 2020:
            print('To low...')
            continue
        else:
            print('Found it...')
            print(f'Answer: {low_number * high_num}')
            sys.exit()




