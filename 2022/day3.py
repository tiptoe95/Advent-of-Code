#!/usr/bin/python3


#


def get_input(path):
    with open(path, 'r') as file:
        supplies = [line.strip() for line in file]
    return supplies


def verify_supplies(supplies: list[str]) -> list[chr]:
    misplaced_items = []
    for rucksack in supplies:
        split = len(rucksack) // 2
        left, right = rucksack[:split], rucksack[split:]
        common = set(left) & set(right)
        if common == None:
            raise ValueError(f"no common item between {left} and {right}")
        misplaced_items.append(common.pop())
    return misplaced_items


def evaluate_item(item: chr) -> int:
    if item == item.lower():
        return ord(item) - ord('a') + 1
    if item == item.upper():
        return ord(item) - ord('A') + 27
    return None


def badge_groups(groups: list[list[str]]) -> list[int]:
    badges = []
    for group in groups:
        common = set(group[0]) & set(group[1]) & set(group[2])
        if common == None:
            raise ValueError("no common found for group")
        badges.append(common.pop())
    return badges


def main():
    input_file = r'inputs/input_day3.txt'
    supplies = get_input(input_file)
    misplaced_items = verify_supplies(supplies)
    values = [evaluate_item(item) for item in misplaced_items]
    print(f"Part 1:\n{sum(values)}")

    groups = [supplies[n:n+3] for n in range(0, len(supplies), 3)]
    badges = badge_groups(groups)
    ans = sum(evaluate_item(item) for item in badges)
    print(f"Part 2:\n{ans}")
    


def test():
    supplies = """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """
    supplies = supplies.split("\n")
    supplies = [item.lstrip() for item in supplies[1:-1]]
    
    print("part 1")
    misplaced_items = verify_supplies(supplies)
    print(misplaced_items)

    values = [evaluate_item(item) for item in misplaced_items]
    print(values)

    print("part 2")
    groups = [supplies[n:n+3] for n in range(0, len(supplies), 3)]
    for group in groups:
        print(group)
    print(badge_groups(groups))
    

if __name__ == "__main__":
    main()
    
