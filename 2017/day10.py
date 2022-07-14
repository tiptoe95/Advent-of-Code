#!/bin/python3


#


# ripped from reddit
def run(lengths, times):
    position = 0
    skip = 0
    sequence = list(range(256))
    for _ in range(times):
        for l in lengths:
            for i in range(l // 2):
                now = (position + i) % len(sequence)
                later = (position + l - 1 - i) % len(sequence)
                sequence[now], sequence[later] = sequence[later], sequence[now]
            position += l + skip
            skip += 1
    return sequence


def get_input(filepath):
    with open(filepath, 'r') as input_file:
        data = input_file.readline().split(',')
        data = [int(n) for n in data]
    return data


def ropehash(lengths, length):
    rope = Rope(length)
    skip_size = 0
    for length in lengths:
        rope.twist(rope.index, length)
        rope.index += skip_size + length 
        skip_size += 1
    return rope[0] * rope[1]


class Rope():
    CENSUS = [] 

    def __init__(self, length):
        self.CENSUS.append(self)
        self.length = length
        self.hash = list(range(self.length))
        self._index = 0

    @property
    def index(self):
        return self._index
    @index.setter
    def index(self, new_index):
        self._index = new_index % self.length
    
    def __getitem__(self, index):
        return self.hash[index]

    def __repr__(self):
        return '-'.join(str(n) for n in self.hash)

    def twist(self, index, length):
        seq = self.get_seq(index, length)
        while seq:
            if index == self.length:
                index = 0
            self.hash[index] = seq.pop()
            index += 1

    def get_seq(self, index, length):
        try:
            return [self.hash[index + i] for i in range(length)]
        except IndexError:
            temp_hash =  self.hash*2
            return [temp_hash[index + i] for i in range(length)]


def test():
    length = 5
    lengths = [3, 4, 1, 5]
    print(ropehash(lengths, length))
    print(Rope.CENSUS[0])



if __name__ == '__main__':
    data = get_input(r"inputs/input_day10.txt")
    part1 = ropehash(data, 256)
    print(f"part 1: {part1}")
