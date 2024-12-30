#!/usr/bin/python3


#


def main():
    raw_lists = get_data()
    ans1 = part1(raw_lists)
    print(f"Part 1: {ans1}")
    ans2 = part2(raw_lists)
    print(f"Part 2: {ans2}")


def get_data():
    input_file = r"inputs/day1.txt"
    with open(input_file, 'r') as file:
        raw_lists = [line.strip().split() for line in file.readlines()]
    return raw_lists


def part1(raw_lists):
    raw_list1 = [int(x[0]) for x in raw_lists]
    raw_list2 = [int(x[1]) for x in raw_lists]
    print(raw_list1[:10])

    sorted_list1 = sorted(raw_list1)
    sorted_list2 = sorted(raw_list2)
    diffs = [abs(x - y) for x, y in zip(sorted_list1, sorted_list2)]
    sum_diffs = sum(diffs)
    return sum_diffs


def part2(raw_lists):
    raw_list1 = [int(x[0]) for x in raw_lists]
    raw_list2 = [int(x[1]) for x in raw_lists]

    score = [x*raw_list2.count(x) for x in raw_list1]
    return sum(score)

if __name__ == '__main__':
    main()
