#!/bin/python3


import copy


def main():
    input_file = 'inputs/input_day5.txt'
    with open(input_file, 'r') as file:
        maze = [int(item.strip()) for item in file.readlines()]

    steps = part1(copy.deepcopy(maze))
    print(f"{steps} steps taken")

    steps = part2(copy.deepcopy(maze))
    print(f"{steps} steps taken after changeup")


def part1(maze):
    IN_MAZE = True
    index = 0
    steps = 0
    while IN_MAZE:
        try:
            jump = maze[index]
        except IndexError as e:
            IN_MAZE = False
            print(' '*80, end='\r')
            continue
        maze[index] += 1
        index += jump
        steps += 1
        print(f"{steps} steps taken", end='\r')
    return steps


def part2(maze):
    IN_MAZE = True
    index = 0
    steps = 0
    while IN_MAZE:
        try:
            jump = maze[index]
        except IndexError as e:
            IN_MAZE = False
            print(' '*80, end='\r')
            continue
        if jump > 2:
            maze[index] -= 1
        else:
            maze[index] += 1
        index += jump
        steps += 1
        print(f"{steps} steps taken", end='\r')
    return steps


if __name__ == '__main__':
    main()
