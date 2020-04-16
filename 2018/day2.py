from pathlib import Path
import numpy
from collections import defaultdict


def checksum(boxes):
    count_dict = defaultdict(int)
    for k in range(25):
        count_dict[k] = 0
    for box in boxes:
        letter_set = set(box)
        count_set = set()
        for letter in letter_set:
            count_set.add(box.count(letter))
        for count in count_set:
            count_dict[count] += 1
    # factors = list(count_dict.values())
    # while 0 in factors:
    #     factors.remove(0)
    # print(factors)
    checksum_factors = [2, 3]
    short_factors = [count_dict[i] for i in checksum_factors]
    return numpy.prod(short_factors)


def match_char(boxes):
    for box in boxes:
        for otherbox in boxes:
            diffs = 0
            for tup1, tup2 in zip(box, otherbox):
                if not tup1 == tup2:
                    diffs += 1
            if diffs == 1:
                return [box, otherbox]
    return


def main():
    input_file = 'day2input.txt'
    input_path = Path.cwd() / 'inputs' / input_file
    with input_path.open('r') as box_file:
        boxes = [line.strip() for line in box_file]
    cksm = checksum(boxes)
    print(f"checksum: \n{cksm}")
    ids = match_char(boxes)
    print(f"matching IDs: \n{ids[0]}\n{ids[1]}")

    # todo: fix below to get matching letters from ids
    # letters = ids[0]
    # for letter in ids[0]:
    #     if letter != ids[1][ids[0].index(letter)]:
    #         letters = letters.replace(letter, '')
    #         break
    # print(f"matching letters:\n{letters}")


if __name__ == '__main__':
    main()
