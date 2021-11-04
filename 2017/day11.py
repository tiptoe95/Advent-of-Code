#!/bin/python3


#


def getInput(filepath):
    with open(filepath, 'r') as file:
        seq = file.readline().strip().split(',')
    return seq


def consolidateSteps(seq):
    step_count = {"n":0, "ne":0, "se":0, "s":0, "sw":0, "nw":0}
    for step in seq:
        step_count[step] += 1
    # opposite steps cancel out
    delta_n = step_count["n"] - step_count["s"]
    delta_e = step_count["ne"] - step_count["sw"]
    delta_w = step_count["nw"] - step_count["se"]
    deltas = [delta_n, delta_e, delta_w]
    deltas = [_ for _ in map(abs, deltas)]
    # NE and NW combine to give one N step
    x = min(deltas[1:])
    deltas[0] += x
    deltas[1] -= x
    deltas[2] -= x
    return sum(deltas)


def maxDistance(seq):
    max = 0
    for n in range(len(seq)):
        distance = consolidateSteps(seq[:n])
        if distance > max:
            max = distance
    return max


if __name__ == "__main__":
    step_seq = getInput(r'inputs/input_day11.txt')
    steps = consolidateSteps(step_seq)
    print(f"part 1: {steps} steps")
    max_steps = maxDistance(step_seq)
    print(f"part 2: {max_steps} steps")
