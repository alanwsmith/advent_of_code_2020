#!/usr/bin/env python3

import unittest

from passport import Passport


class PassportTest(unittest.TestCase):

    def test_integration_passport_with_all_valid_fields(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm')
        actual = p.is_passport_valid()
        self.assertTrue(actual)

    def test_integration_passport_missing_field(self):
        p = Passport(data='iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929')
        actual = p.is_passport_valid()
        self.assertFalse(actual)

    def test_integration_invalid_byr(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1919 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm')
        actual = p.is_passport_valid()
        self.assertFalse(actual)

    def test_setup_keys(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm')
        expected = {
            'eyr': '2029',
            'ecl': 'blu',
            'cid': '129',
            'byr': '1989',
            'iyr': '2014',
            'pid': '896056539',
            'hcl': '#a97842',
            'hgt': '165cm',
        }
        actual = p.details
        self.assertEqual(expected, actual)

    def test_confirm_the_keys_is_true(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm')
        actual = p.confirm_the_keys()
        self.assertTrue(actual)

    def test_confirm_the_keys_false_less_than_seven(self):
        p = Passport(data='cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm')
        actual = p.confirm_the_keys()
        self.assertFalse(actual)


    # byr (Birth Year) - four digits; at least 1920 and at most 2002.

    def test_validation_birth_year_valid(self):
        p = Passport(data='byr:1989')
        actual = p.validate_birth_year()
        self.assertTrue(actual)

    def test_validation_birth_year_invalid(self):
        p = Passport(data='byr:1900')
        actual = p.validate_birth_year()
        self.assertFalse(actual)

    def test_validation_birth_year_true_if_missing(self):
        p = Passport(data='place_holder:1234')
        actual = p.validate_birth_year()
        self.assertTrue(actual)

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.

    def test_validate_issue_year_valid(self):
        p = Passport(data='iyr:2010')
        actual = p.validate_issue_year()
        self.assertTrue(actual)

    def test_validate_issue_year_invalid(self):
        p = Passport(data='iyr:2009')
        actual = p.validate_issue_year()
        self.assertFalse(actual)

    def test_validate_issue_year_valid_if_missing(self):
        p = Passport(data='place_holder:1234')
        actual = p.validate_issue_year()
        self.assertTrue(actual)





# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.

if __name__ == '__main__':
    unittest.main()

