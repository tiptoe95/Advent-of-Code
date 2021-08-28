#!/bin/python3


#


def main():
    input_file = 'inputs/input_day6.txt'
    with open(input_file, 'r') as file:
        memory = [int(block) for block in file.readline().split()]
    passes = part1(memory)
    print(passes)


def part1(memory):
    passes = 0
    configs = []
    while (config := ' '.join(map(str, memory))) not in configs:
        configs.append(config)
        memory = redistribute(memory)
        passes += 1
    loop = len(configs) - configs.index(config)
    print(f"{loop} passes in loop")
    return passes


def redistribute(memory):
    i = memory.index(max(memory))
    amt = max(memory)
    memory[i] = 0
    for n in range(amt):
        memory[(i+n+1)%len(memory)] += 1
    return memory


if __name__ == "__main__":
    main()
