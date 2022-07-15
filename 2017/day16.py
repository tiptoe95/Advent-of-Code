#!/bin/python3


#


class Dance():
    program_roster = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, length):
        self.lineup = [x for x in Dance.program_roster[:length]]
        self.original = self.lineup.copy()
        self.cycle_length = None

    def __repr__(self):
        return ''.join(self.lineup) 

    def spin(self, shift):
        for _ in range(shift):
            x = self.lineup.pop()
            self.lineup = [x] + self.lineup

    def exchange(self, pos1, pos2):
        x = self.lineup
        x[pos1], x[pos2] = x[pos2], x[pos1]

    def partner(self, program1, program2):
        x = self.lineup
        idx1, idx2 = x.index(program1), x.index(program2)
        x[idx1], x[idx2] = x[idx2], x[idx1]

    def parse_move(self, move_str):
        move = move_str[0]
        if move == "s":
            self.spin(int(move_str[1:]))
        elif move == "x":
            pos1, pos2 = move_str[1:].split("/")
            self.exchange(int(pos1), int(pos2))
        elif move == "p":
            prog1, prog2 = move_str[1:].split("/")
            self.partner(prog1, prog2)
        else:
            raise ValueError(f"move <{move}> not valid")


def get_input(file_path):
    with open(file_path, 'r') as input_file:
        moves = input_file.readline().strip().split(',')
    return moves


def part1():
    print("Part 1:")
    program_count = 16
    file_path = "inputs/input_day16.txt"
    moves = get_input(file_path)
    dance = Dance(program_count)
    for move in moves:
        dance.parse_move(move)
    print(dance)


def part2(index_list):
    print("Part 2:")
    program_count = 16
    file_path = "inputs/input_day16.txt"
    moves = get_input(file_path)
    dance = Dance(program_count)
    count = 0
    while dance.cycle_length == None:
        count += 1
        for move in moves:
            dance.parse_move(move)
        if dance.lineup == dance.original:
            dance.cycle_length = count
    steps = int(1e6) % dance.cycle_length
    print(f"cycle found after {steps} steps")
    dance.lineup = dance.original.copy()
    for _ in range(steps):
        print(f"step {_} of {steps}", end = '\r', flush=True)
        for move in moves:
            dance.parse_move(move)
    print(dance)


def test1():
    test_commands = ["s1", "x3/4", "pe/b"]
    test = Dance(5)
    print(test)
    for command in test_commands:
        test.parse_move(command)
        print(test)


if __name__ == "__main__":
    #test1()
    index_list = part1()
    part2(index_list)
