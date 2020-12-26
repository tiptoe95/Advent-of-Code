#!/usr/bin/python3


import time


def get_input():
    with open('input_day1.txt', 'r') as input_file:
        expense_report = [int(line.strip()) for line in input_file]
    return expense_report

    
def part1(expense_report):
    for _, i in enumerate(expense_report):
        print(f"\rmatching item {_} of {len(expense_report)}", end='', flush=True)
        time.sleep(.02)
        for j in expense_report:
            if i+j == 2020:
                print('\n', i*j, sep='')
                return 


def part2(report):
    for _, i in enumerate(report):
        print(f"\rmatching item {_} of {len(report)}", end='', flush=True)
        time.sleep(.01)
        for j in report:
            for k in report:
                if i+j+k == 2020:
                    print('\n', i*j*k, sep='')
                    return


if __name__ == "__main__":
    report = get_input()
    part1(report)
    part2(report)
