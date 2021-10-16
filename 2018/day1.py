#!/bin/python3


from pathlib import Path


def findfreq(changes):
    freq = sum(map(int, changes))
    print(f"frequency at end of series: {freq}")


def calibrate(changes):
    freq = 0
    freqs = set([0])
    duplicate_flag = False
    while not duplicate_flag:
        for change in changes:
            freq += int(change)
            if freq in freqs:
                duplicate_flag = True
                print(f"first repeated value: {freq}")
                break
            freqs.add(freq)


def main():
    file = 'day1input.txt'
    path = Path.cwd() / 'inputs' / file
    with path.open('r') as input_file:
        changes = [line.strip() for line in input_file]
    findfreq(changes)
    calibrate(changes)


if __name__ == '__main__':
    main()
