#!/bin/python3


from itertools import combinations


def main():
    spreadsheet = get_input()
    checksum = part1(spreadsheet)
    print(checksum)
    combosum = part2(spreadsheet)
    print(combosum)


def get_input():
    input_file = 'inputs/day2_input.txt'
    spreadsheet = []
    with open(input_file) as file:
        for line in file:
            spreadsheet.append([int(num) for num in line.split()])
    return spreadsheet


def part1(text):
    print("PART 1: ")
    diffs = []
    for line in text:
        diff = max(line) - min(line)
        diffs.append(diff)
    return sum(diffs)


def part2(text):
    print("PART 2: ")
    divs = []
    for i, line in enumerate(text):
        print(f"line {i} of {len(text)} in progress...", end='\r')
        combos = combinations(line, 2) 
        for combo in combos:
            if max(combo) % min(combo) == 0:
                divs.append( max(combo)//min(combo) )
    print('\x1b[2K\r', end='\r')
    return sum(divs)


if __name__ == '__main__':
    main()
