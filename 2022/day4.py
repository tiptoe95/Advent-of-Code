#!/usr/bin/python3


#


def get_input(path: str) -> list[tuple[int]]:

    def int_range(range: str) -> tuple[int]:
        return tuple(int(x) for x in range.split("-"))

    with open(path, 'r') as file:
        pairs = []
        for line in file.readlines():
            line = line.strip()
            range1, range2 = map(int_range, line.split(","))
            pairs.append([range1, range2])
    return pairs


def is_subrange(range1: tuple[int], range2: tuple[int]) -> bool:
    range1_start, range1_end = range1
    range2_start, range2_end = range2
    return range1_start <= range2_start and range1_end >= range2_end


def is_overlap(range1: tuple[int], range2: tuple[int]) -> bool:
    range1_start, range1_end = range1
    range2_start, range2_end = range2
    return range2_start <= range1_start <= range2_end or \
            range2_start <= range1_end <= range2_end


def main():
    input_file = r'inputs/input_day4.txt'
    pairs = get_input(input_file)

    #Part 1
    overlaps = 0
    for pair in pairs:
        range1, range2 = pair
        if is_subrange(range1, range2) or is_subrange(range2, range1):
            overlaps += 1
    print(f"Part 1:\n{overlaps}")

    #Part2
    overlaps = 0
    for pair in pairs:
        range1, range2 = pair
        if is_overlap(range1, range2) or is_overlap(range2, range1):
            overlaps += 1
    print(f"Part 2:\n{overlaps}")
    return


def test():
    return


if __name__ == "__main__":
    main()
