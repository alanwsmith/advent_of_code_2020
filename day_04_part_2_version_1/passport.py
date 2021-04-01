import re

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

    def validate_birth_year(self):
        if 'byr' in self.details:
            year = int(self.details['byr'])
            if 1920 <= year <= 2002:
                return True
            else:
                return False
        else:
            return True

    def validate_eye_color(self):
        if 'ecl' in self.details.keys():
            if re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', self.details['ecl']):
                return True
            else:
                return False
        else:
            return True

    def validate_hair_color(self):
        if 'hcl' in self.details:
            match = re.search(r'^#[a-f0-9]{6}$', self.details['hcl'])
            if match:
                return True
            else:
                return False
        else:
            return True

    def validate_height(self):
        if 'hgt' in self.details.keys():
            match = re.search(r'^(\d+)(in|cm)$', self.details['hgt'])
            if match:
                numeral = int(match.group(1))
                ruler = match.group(2)
                if ruler == 'cm':
                    if 150 <= numeral <= 193:
                        return True
                elif ruler == 'in':
                    if 59 <= numeral <= 76:
                        return True
                else:
                    return False
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

    def validate_passport_id(self):
        if 'pid' in self.details.keys():
            if re.search(r'^\d{9}$', self.details['pid']):
                return True
            else:
                return False
        else:
            return True

    def is_passport_valid(self):
        if not self.confirm_the_keys():
            return False
        elif not self.validate_birth_year():
            return False
        elif not self.validate_expiration_year():
            return False
        elif not self.validate_eye_color():
            return False
        elif not self.validate_issue_year():
            return False
        elif not self.validate_passport_id():
            return False
        elif not self.validate_hair_color():
            return False
        elif not self.validate_height():
            return False
        else:
            return True

