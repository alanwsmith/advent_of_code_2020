# byr - Required - (Birth Year)
# iyr - Required -  (Issue Year)
# eyr - Required -  (Expiration Year)
# hgt - Required -  (Height)
# hcl - Required -  (Hair Color)
# ecl - Required -  (Eye Color)
# pid - Required -  (Passport ID)
# cid - Optional -  (Country ID)

from passport import Passport

class PassportValidator:

    def __init__(self):
        self.raw_input = None
        self.passports = []
        self.valid_passports = 0

    def parse_raw_input(self):
        self.passports = []
        raw_passports = self.raw_input.split("\n\n")
        for raw_passport in raw_passports:
            self.passports.append(raw_passport.replace("\n", ' '))

    def process_passports(self):
        for passport in self.passports:
            p = Passport(data=passport)
            if p.is_passport_valid():
                self.valid_passports += 1


if __name__ == '__main__':
    pv = PassportValidator()
    with open('passport_validator_input.txt') as _file:
        pv.raw_input = _file.read()
    pv.parse_raw_input()
    pv.process_passports()
    print(pv.valid_passports)
