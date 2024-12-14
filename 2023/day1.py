#!/usr/bin/python3


import re


def get_input(input_file):
    with open(input_file, 'r') as file:
        data = [line.strip() for line in file.readlines()]
        return data


def match_number_ends(s):
    expression = r"\d"
    p = re.compile(expression)
    res = p.findall(s)
    first_num = res[0]
    last_num = res[-1]
    return first_num, last_num

def insert_nums(s):
    search_pattern = r"one|two|three|four|five|six|seven|eight|nine"
    num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    prog = re.compile(search_pattern)
    while (match_obj := prog.search(s)):
        match_str = match_obj.group()
        s = s.replace(match_str, num_dict[match_str], 1)
    return s


def find_digit(s: str, direction="left") -> str:
    num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    if direction == "right":
        substr_func = right_substrs
    else:
        substr_func = left_substrs
    for substring in substr_func(s):
        if x := match_num(s):
            return x
        for num in num_dict:
            if num in substring:
                return num_dict[num]
    return False


def left_substrs(s: str) -> str:
    for i in range(len(s)):
        yield s[:i+1]

def right_substrs(s: str) -> str:
    for i in range(len(s)):
        yield s[::-1][:i+1]

def match_num(s: str) -> str:
    for num in "123456789":
        if num in s:
            return num
    return False


def main():
    input_file = r"inputs/input_day1.txt"
    data = get_input(input_file)

    # Part 1
    values = [int(''.join(match_number_ends(nums))) for nums in data]
    ans1 = sum(values)
    print(f"Part 1: {ans1}")
    
    # # Part 2
    # cleaned_data = [insert_nums(line) for line in data]
    # cleaned_values = [int(''.join(match_number_ends(nums))) for nums in cleaned_data]
    # ans2 = sum(cleaned_values)
    # print(f"Part 2: {ans2}")

    # Part 2
    coordinates = []
    for line in data:
        x = find_digit(line, direction="left")
        y = find_digit(line, direction="right")
        if not x or not y:
            print(f"Cound not find viable coordinates for line <{line}>")
        coordinates.append(int(x + y))      # string concatenation
    ans2 = sum(coordinates)
    print(f"Part 2: {ans2}")


test_data = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"]


def test1():
    input_file = r"inputs/input_day1.txt"
    #data = get_input(input_file)
    #data2 = [match_number_ends(line) for line in test_data]
    data3 = [insert_nums(line) for line in test_data]
    print(data3)
    for x in left_substrs("abcdefg"):
        print(x)
    for x in right_substrs("abcdefg"):
        print(x)

def test2():
    s = "tsgbzmgbonethreedrqzbhxjkvcnm3"
    num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    x = find_digit(s, direction="right")
    print(x)


if __name__ == "__main__":
    main()
