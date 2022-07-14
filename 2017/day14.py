#!/bin/python3


from functools import reduce
from itertools import accumulate, zip_longest as zipl
from operator import mul, xor


def solve2(input, n=256, g=16, rounds=64, suffix=[17, 31, 73, 47, 23], pos=0, skip=0):
    elems, lengths = [*range(n)], [ord(c) for c in input.strip()] + suffix
    for _ in range(rounds):
        elems, pos, skip = hash_round(lengths, elems, pos, skip)
    return bytes(reduce(xor, elems[g*k:g*(k+1)]) for k in range(n//g)).hex()


def solve(key_string):
    count = 0
    unseen = []
    for i in range(128):
        hash = knothash(key_string + "-" + str(i))
        bin_hash = bin(int(hash, 16))[2:].zfill(128)
        unseen += [(i, j) for j, d in enumerate(bin_hash) if d == '1']
    print("Part 1: " + str(len(unseen)))


def main():
    input_hash = "amgozmfv"
    matrix = ''.join(''.join('{:04b}'.format(int(x, 16)) for x in solve2(f'{input_hash}-{i}')) for i in range(128))
    print(matrix.count('1')


if __name__ == "__main__":
    #test()
    main()
