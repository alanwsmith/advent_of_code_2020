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

    def test_integration_passport_invalid_eyr(self):
        p = Passport(data='eyr:1000 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm')
        actual = p.is_passport_valid()
        self.assertFalse(actual)

    def test_integration_passport_invalid_ecl(self):
        p = Passport(data='eyr:2029 ecl:red cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm')
        actual = p.is_passport_valid()
        self.assertFalse(actual)

    def test_integration_passport_invalid_byr(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1900 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm')
        actual = p.is_passport_valid()
        self.assertFalse(actual)

    def test_integration_passport_invalid_iyr(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1990 iyr:3014 pid:896056539 hcl:#a97842 hgt:165cm')
        actual = p.is_passport_valid()
        self.assertFalse(actual)

    def test_integration_passport_invalid_pid(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1990 iyr:2014 pid:89605653 hcl:#a97842 hgt:165cm')
        actual = p.is_passport_valid()
        self.assertFalse(actual)

    def test_integration_passport_invalid_hcl(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1990 iyr:2014 pid:896056531 hcl:#z97842 hgt:165cm')
        actual = p.is_passport_valid()
        self.assertFalse(actual)

    def test_integration_passport_invalid_hgt(self):
        p = Passport(data='eyr:2029 ecl:blu cid:129 byr:1990 iyr:2014 pid:896056531 hcl:#a97842 hgt:165in')
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

    def test_validate_expiration_year_valid(self):
        p = Passport(data='eyr:2020')
        actual = p.validate_expiration_year()
        self.assertTrue(actual)

    def test_validate_expiration_year_invalid(self):
        p = Passport(data='eyr:2019')
        actual = p.validate_expiration_year()
        self.assertFalse(actual)

    def test_validate_expiration_year_valid_if_missing(self):
        p = Passport(data='place_holder:1234')
        actual = p.validate_expiration_year()
        self.assertTrue(actual)

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.

    def test_validate_height_valid_cm(self):
        p = Passport(data='hgt:160cm')
        actual = p.validate_height()
        self.assertTrue(actual)

    def test_validate_height_invalid_cm(self):
        p = Passport(data='hgt:140cm')
        actual = p.validate_height()
        self.assertFalse(actual)

    def test_validate_height_valid_in(self):
        p = Passport(data='hgt:59in')
        actual = p.validate_height()
        self.assertTrue(actual)

    def test_validate_height_invalid_in(self):
        p = Passport(data='hgt:58in')
        actual = p.validate_height()
        self.assertFalse(actual)

    def test_validate_height_invalid_string(self):
        p = Passport(data='hgt:58sin')
        actual = p.validate_height()
        self.assertFalse(actual)

    def test_validate_height_valid_missing_height(self):
        p = Passport(data='place_holder:1234')
        actual = p.validate_height()
        self.assertTrue(actual)

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

    def test_validate_hair_color_with_valid_color(self):
        p = Passport(data='hcl:#aaaaaa')
        actual = p.validate_hair_color()
        self.assertTrue(actual)

    def test_validate_hair_color_with_invalid_color(self):
        p = Passport(data='hcl:#zzzz')
        actual = p.validate_hair_color()
        self.assertFalse(actual)

    def test_validate_hair_color_passes_with_no_color(self):
        p = Passport(data='place_holder:1234')
        actual = p.validate_hair_color()
        self.assertTrue(actual)

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

    def test_validate_eye_color_is_valid(self):
        p = Passport(data='ecl:blu')
        actual = p.validate_eye_color()
        self.assertTrue(actual)

    def test_validate_eye_color_is_invalid(self):
        p = Passport(data='ecl:red')
        actual = p.validate_eye_color()
        self.assertFalse(actual)

    def test_validate_eye_color_is_missing_but_valid(self):
        p = Passport(data='place_holder:1234')
        actual = p.validate_eye_color()
        self.assertTrue(actual)

    # pid (Passport ID) - a nine-digit number, including leading zeroes.

    def test_validate_pid_with_valid_id(self):
        p = Passport(data='pid:000000000')
        actual = p.validate_passport_id()
        self.assertTrue(actual)

    def test_validate_pid_with_invalid_id(self):
        p = Passport(data='pid:11')
        actual = p.validate_passport_id()
        self.assertFalse(actual)

    def test_validate_pid_when_missing_is_true(self):
        p = Passport(data='place_holder:1234')
        actual = p.validate_passport_id()
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()

