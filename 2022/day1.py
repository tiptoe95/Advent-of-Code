#!/usr/bin/python3


#


def get_input(path):
    with open(path, 'r') as file:
        elf_calories = {}
        count = 1
        for line in file.readlines():
            line = line.rstrip()
            if line == "":
                count += 1
                continue
            try:
                elf_calories[count].append(int(line))
            except KeyError:
                elf_calories[count] = [int(line)]
    return elf_calories


def most_calories(elf_calories):
    fatass_elf = max(elf_calories.values(), key=lambda x: sum(x))
    return sum(fatass_elf)

def sort_elves_by_calories(elf_calories):
    elves = sorted(elf_calories.values(), key=lambda x: sum(x), reverse=True)
    top3 = elves[:3]
    return sum([sum(x) for x in top3])


def main():
    input_file = r"inputs/input_day1.txt"
    elf_calories = get_input(input_file)
    part1 = most_calories(elf_calories)
    print(part1)
    part2 = sort_elves_by_calories(elf_calories)
    print(part2)
    return


if __name__ == "__main__":
    main()
