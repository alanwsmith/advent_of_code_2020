#!/usr/bin/env python3

import unittest

from passport_validator import PassportValidator

class PassportValidatorTest(unittest.TestCase):

    def setUp(self):
        global pv
        pv = PassportValidator()

    def test_parse_input(self):
        with open('test_data/test_input_1.txt') as _file:
            pv.raw_input = _file.read()
        pv.parse_raw_input()
        expected = [
            'pid:2306523501 eyr:2032 hcl:z ecl:brn cid:266 hgt:151in iyr:2024 byr:2008',
            'hcl:#a97842 hgt:191cm eyr:2025 ecl:gry byr:1923 pid:574171850 iyr:2019',
            'hgt:140 iyr:1987 byr:2003 eyr:2013 cid:242 hcl:z ecl:#19177c pid:150cm',
        ]
        actual = pv.passports
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
