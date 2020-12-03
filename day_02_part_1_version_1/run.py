#!/usr/bin/env python3


class Runner:

    def __init__(self):
        self.compressed_number = None
        self.diff_number = None
        self.high_number = None
        self.low_number = None
        self.original_number_count = None
        self.password_line = None
        self.password_string = None
        self.target_letter = None

    def make_compressed_number(self):
        self.compressed_number = len(self.password_string.replace(self.target_letter, ''))

    def make_diff_number(self):
        self.diff_number = self.original_number_count - self.compressed_number

    def split_password_line(self):
        self.low_number = int(self.password_line.split('-')[0])
        self.high_number = int(self.password_line.split('-')[1].split(' ')[0])
        self.target_letter = self.password_line.split(' ')[1][0]
        self.password_string = self.password_line.split(' ')[2]
        self.original_number_count = len(self.password_string)

    def is_password_valid(self):
        self.split_password_line()
        self.make_compressed_number()
        self.make_diff_number()
        if self.diff_number < self.low_number:
            return False
        elif self.diff_number > self.high_number:
            return False
        else:
            return True


if __name__ == '__main__':

    r = Runner()
    true_count = 0

    with open('input.txt', 'r') as _file:
        for line in _file:
            r.password_line = line
            if r.is_password_valid():
                true_count += 1

    print(true_count)
