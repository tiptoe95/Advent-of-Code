#!/bin/python3


from collections import defaultdict


def main():
    # read input
    with open("inputs/input_day8.txt", 'r') as file:
        instructions = [line.strip() for line in file.readlines()] 

    # initialize registers and commands
    registers = {}
    def inc(n, amt): registers[n] += amt 
    def dec(n, amt): registers[n] -= amt
    def lt(n, m): return n < m
    def leq(n, m): return n <= m
    def eq(n, m): return n == m
    def gt(n, m): return n > m
    def geq(n, m): return n >= m
    def neq(n, m): return n != m
    commands = {"inc": inc, "dec": dec, "<":lt, "<=": leq, "==": eq, ">": gt, ">=": geq, "!=": neq}
    running_max = 0

    # carry out instructions
    for instruction in instructions:
        instruction = instruction.split()
        register = instruction[0]
        command = instruction[1]
        amt = int(instruction[2])
        test1 = instruction[4]
        operator = instruction[5]
        test2 = int(instruction[6])

        if register not in registers:
            registers[register] = 0
        if test1 not in registers:
            registers[test1] = 0
        if commands[operator](registers[test1], test2):
            commands[command](register, amt)

        current_max = max(registers.values())
        if current_max > running_max:
            running_max = current_max

    print(current_max)
    print(running_max)


if __name__ == "__main__":
    main()

