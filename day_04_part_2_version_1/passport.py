# Validation rules
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.

class Passport:

    def __init__(self, *, data):
        self.data = data
        self.is_valid = True
        self.details = {}
        self._parse_data()

    def _parse_data(self):
        pairs = self.data.split(' ')
        for pair in pairs:
            key, value = pair.split(':')
            self.details[key] = value

    def confirm_the_keys(self):
        if len(self.details) == 8:
            return True
        elif len(self.details) <= 6:
            return False
        else:
            if 'cid' in self.details.keys():
                return False
            else:
                return True

    def is_passport_valid(self):
        if not self.confirm_the_keys():
            return False
        elif not self.validate_birth_year():
            return False
        else:
            return True

    def validate_birth_year(self):
        if 'byr' in self.details:
            year = int(self.details['byr'])
            if 1920 <= year <= 2002:
                return True
            else:
                return False
        else:
            return True

    def validate_issue_year(self):
        if 'iyr' in self.details:
            year = int(self.details['iyr'])
            if 2010 <= year <= 2020:
                return True
            else:
                return False
        else:
            return True

    def validate_expiration_year(self):
        if 'eyr' in self.details:
            year = int(self.details['eyr'])
            if 2020 <= year <= 2030:
                return True
            else:
                return False
        else:
            return True
