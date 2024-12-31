#!/usr/bin/python3


import re


def main():
    input_strings = get_data()
    part1(input_strings)
    part2(input_strings)
    return


def part1(input_strings: list[str]):
    commands = []
    for string in input_strings:
        clean_string = clean(string)
        commands.extend(clean_string)
    products = parse_commands(commands)
    final_value = sum(products)
    print(f"Part 1: {final_value}")
    return


def part2(input_strings: list[str]):
    commands = []
    for string in input_strings:
        clean_string = clean_pt2(string)
        commands.extend(clean_string)
    products = parse_commands_pt2(commands)
    final_value = sum(products)
    print(f"Part 2: {final_value}")
    return


def parse_commands(commands: list[str]) -> list[int]:
    products = []
    for command in commands:
        pattern = r"(\d+),(\d+)"
        matches = re.findall(pattern, command)[0]
        if len(matches) != 2:
            raise ValueError(f"matching error in command {command}")
        a, b = matches
        products.append(int(a) * int(b))
    return products


def parse_commands_pt2(commands: list[str]) -> list[int]:
    products = []
    INSTRUCTIONS_ENABLED = True
    for command in commands:
        if command[0:3] == r"do(":
            INSTRUCTIONS_ENABLED = True
        elif command[0:3] == r"don":
            INSTRUCTIONS_ENABLED = False
        elif command[0:3] == "mul":
            if INSTRUCTIONS_ENABLED == True:
                a, b = re.findall(r"(\d+),(\d+)", command)[0]
                products.append(int(a) * int(b))
            else:
                continue
    return products


def clean(string: str) -> list[str]:
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, string)
    return matches


def clean_pt2(string: str) -> list[str]:
    patterns = [r"mul\(\d+,\d+\)", r"don't\(\)", r"do\(\)"]
    pattern = "|".join(patterns)
    matches = re.findall(pattern, string)
    return matches


def get_data() -> list[str]:
    filepath = r"inputs/day3.txt"
    with open(filepath, 'r') as file:
        data = [x.strip() for x in file.readlines()]
    return data


if __name__ == '__main__':
    main()
