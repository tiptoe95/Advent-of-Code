#!/usr/bin/python3


def get_input():
    with open("input_day2.txt", 'r') as file:
        return [line.strip() for line in file]


def part1(passwords):
    valid_passwords = 0
    for line in passwords:
        limits, letter, password = line.split(' ')
        letter = letter[:-1]
        letter_min, letter_max = map(int, limits.split('-'))

        if password.count(letter) in range(letter_min, letter_max+1):
            valid_passwords += 1
    return valid_passwords

        
def part2(passwords):
    valid_passwords = 0
    for line in passwords:
        positions, letter, password = line.split(' ')
        pos1, pos2 = map(int, positions.split('-'))
        letter = letter[:-1]

        MATCH = False
        for pos in (pos1, pos2):
            if password[pos-1] == letter:
                if MATCH == False:
                    MATCH = True
                else:
                    MATCH = False
                    break
        if MATCH == True:
            valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    passwords = get_input()
    print(part1(passwords))
    print(part2(passwords))
