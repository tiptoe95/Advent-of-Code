from pathlib import Path
import re


def main():
    seq = get_input()
    ans1 = sum_next(seq)
    ans2 = sum_half(seq)
    print(f"Part 1: {ans1}\nPart 2: {ans2}")


def get_input():
    base_path = Path(__file__).parent
    file_path = (base_path / 'inputs/day1_input.txt')
    with open(file_path, 'r') as inputFile:
        seq = [int(num) for num in inputFile.readline().rstrip('\n')]
        return seq


def sum_next(seq):
    newseq = seq[:]
    newseq.append(newseq[0])
    sumlist = []
    for i, num in enumerate(newseq):
        try:
            if newseq[i+1] == num:
                sumlist.append(num)
        except IndexError:
            pass
    return sum(sumlist)


def sum_half(seq):
    step = int(len(seq) / 2)
    circle_seq = seq * 2
    sumlist = []
    for i, num in enumerate(seq):
        if circle_seq[i+step] == num:
            sumlist.append(num)
    return sum(sumlist)


if __name__ == '__main__':
    main()


