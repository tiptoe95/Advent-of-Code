#!/usr/bin/python3


class Passport():
    census = []
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, passport_string):
        Passport.census.append(self)
        self.entries = {k:v for (k,v) in Passport.parse(passport_string)}
        self.passed = True
        for field in Passport.fields:
            if not self.validate(field):
                self.passed = False
                break

    def parse(passport_string):
        split_passport = passport_string.split()
        for item in split_passport:
            field, value = item.split(':')
            yield field, value 

    def validate(self, entry):
        try:
            value = self.entries[entry]
        except:
            return False
        if entry == 'byr':
            if len(value) > 4: return False
            try:
                value = int(value)
                if value > 2002 or value < 1920:
                    return False
            except:
                return False
        elif entry == 'iyr':
            if len(value) > 4: return False
            try:
                value = int(value)
                if value > 2020 or value < 2010:
                    return False
            except:
                return False
        elif entry == 'eyr':
            if len(value) > 4: return False
            try:
                value = int(value)
                if value > 2030 or value < 2020:
                    return False
            except:
                return False
        elif entry == 'hgt':
            unit = value[-2:]
            try: height = int(value[:-2])
            except: return False
            if unit == 'in':
                if height < 59 or height > 76:
                    return False
            elif unit == 'cm':
                if height < 150 or height > 193:
                    return False
            else: return False
        elif entry == 'hcl':
            if value[0] != '#' or len(value) != 7:
                return False
            for digit in value[1:]:
                if digit not in 'abcdef0123456789':
                    return False
        elif entry == 'ecl':
            if len(value) != 3 or value not in {'amb','blu','brn','gry','grn','hzl','oth'}:
                return False
        elif entry == 'pid':
            try:
                _ = int(value)
                if len(value) != 9:
                    return False
            except:
                return False
        elif entry == 'cid':
            pass
        # all tests passed
        return True
        
 
def get_input():
    with open('input_day4.txt', 'r') as file:
        passports = [[]] 
        for line in file:
            if line == '\n':
                passports.append([])
            else:
                passports[-1].append(line.strip())
    passports = [' '.join(person) for person in passports]
    return passports


def part1(passports):
    passed = 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        if verify(passport, fields):
            passed += 1
    return passed


def part2(passports):
    passed = 0
    for passport in passports:
        this = Passport(passport)
        if this.passed == True:
            passed += 1
    return passed


def verify(passport, fields):
    for field in fields:
        if field not in passport:
            return False
    return True


if __name__ == '__main__':
    passports = get_input()
    print(part1(passports))
    print(part2(passports))
