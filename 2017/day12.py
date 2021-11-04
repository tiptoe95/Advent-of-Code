#!/bin/python3


#


class PipeDict(dict):

    def __init__(self):
        self.visited = set()
        self.groups = []

    def __missing__(self, wonky_key):
        pass

    def __str__(self, head=10):
        for idx in range(head):
            print(self[idx])
        return str(self[idx+1])


def getInput(file_path):
    pipes = PipeDict()
    with open(file_path, 'r') as file:
        for line in file:
            key, val = line.strip().split('<->')
            val = [int(x.strip()) for x in val.split(", ")]
            pipes.update({int(key): val})
    return pipes


def find_connections(pipes, idx=0):
    if idx in pipes.visited:
        return
    else:
        pipes.visited.add(idx)
    for program in pipes[idx]:
        find_connections(pipes, program)


def find_groups(pipes):
    pipes.visited = set()
    for program in pipes:
        if is_revisited(pipes, program):
            continue
        find_connections(pipes, program)
        pipes.groups.append(pipes.visited)
        pipes.visited = set()


def is_revisited(pipes, program):
    for group in pipes.groups:
        if program in group:
            return True
    return False


if __name__ == "__main__":
    pipes = getInput('inputs/input_day12.txt')
    find_connections(pipes)
    print(f"Part 1: {len(pipes.visited)}")
    find_groups(pipes)
    print(f"Part 2: {len(pipes.groups)}")
