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
    delta_n = step_count["n"] - step_count["s"]
    delta_e = step_count["ne"] - step_count["sw"]
    delta_w = step_count["nw"] - step_count["se"]
    deltas = [delta_n, delta_e, delta_w]
    print(deltas)


if __name__ == "__main__":
    step_seq = getInput(r'inputs/input_day11.txt')
    consolidateSteps(step_seq)
