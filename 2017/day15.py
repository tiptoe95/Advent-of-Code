#!/bin/python3


#


class Generator():
    CENSUS = []
    DIVISOR = 2147483647
    MATCHES = 0

    def __init__(self, factor=1, seed=0):
        Generator.CENSUS.append(self)
        self.factor = factor
        self.value = seed
        self.seq = [seed]


    def next_value(self, divisor=None):
        self.value = (self.value * self.factor) % Generator.DIVISOR
        if divisor == None:
            return self.value
        while self.value % divisor != 0:
            self.value = self.next_value(divisor)
        return self.value


    def judge_pair(bin1, bin2):
        if bin1[-16:] == bin2[-16:]:
            Generator.MATCHES += 1


def part1():
    genA = Generator(16807, 722)
    genB = Generator(48271, 354)
    for _ in range(int(4e7)):
        print(f"{_:,}", end='\r', flush=True)
        bin1 = bin(genA.next_value())[2:].zfill(16)
        bin2 = bin(genB.next_value())[2:].zfill(16)
        Generator.judge_pair(bin1, bin2)
    print()
    print("part 2: ", Generator.MATCHES)


def part2():
    genA = Generator(16807, 722)
    genB = Generator(48271, 354)
    for _ in range(int(5e6)):
        print(f"{_:,}", end='\r', flush=True)
        bin1 = bin(genA.next_value(4))[2:].zfill(16)
        bin2 = bin(genB.next_value(8))[2:].zfill(16)
        Generator.judge_pair(bin1, bin2)
    print()
    print("part 2: ", Generator.MATCHES)


def test1():
    genA = Generator(16807, 65)
    genB = Generator(48271, 8921)
    for _ in range(int(4e7)):
        print(f"{_:,}", end='\r', flush=True)
        bin1 = bin(genA.next_value())[2:].zfill(16)
        bin2 = bin(genB.next_value())[2:].zfill(16)
        Generator.judge_pair(bin1, bin2)
    print()
    print(Generator.MATCHES)



if __name__ == "__main__":
    #test()
    #part1()
    part2()
