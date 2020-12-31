#!/usr/bin/python3


def get_input():
    with open('input_day3.txt', 'r') as file:
        trees = [line.strip() for line in file]
    return trees


def part1(trees, slope):
    pos = 0
    hits = 0
    for row in trees:
        if row[pos % len(row)] == '#':
            hits += 1
        pos += slope[0]
    return hits


import math
def part2(trees):
    slopes = {(1,1):0, (3,1):0, (5,1):0, (7,1):0, (1,2):0}
    for slope in slopes.keys():
        pos = 0
        row = 0
        hits = 0
        while row < len(trees):
            if trees[row][pos%len(trees[0])] == '#':
                hits += 1
            pos += slope[0]
            row += slope[1]
        slopes[slope] = hits
    return math.prod(slopes.values()) 


if __name__ == '__main__':
    trees = get_input()
    hits = part1(trees, (3,1))
    print(hits)
    hits = part2(trees)
    print(hits)
