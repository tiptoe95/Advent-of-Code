#!/bin/python3


#


class Spinlock():

    def __init__(self, step_size):
        self.buffer = [0] 
        self.buffer_len = 1
        self.position = 0
        self.value = 0
        self.step_size = step_size
        self.val_after_zero = 0

    def  __repr__(self):
        str1 = '  '.join(str(x) for x in self.buffer[:self.position])
        str2 = f"({self.value})"
        str3 = '  '.join(str(x) for x in self.buffer[self.position + 1:])
        return str1 + str2 + str3

    def step(self):
        self.value += 1
        self.position = (self.position + self.step_size) % len(self.buffer)
        self.position += 1
        self.buffer.insert(self.position, self.value)

    def quick_step(self):
        self.value += 1
        self.position = (self.position + self.step_size) % len(self.buffer)
        self.position += 1
        if self.position == 1:
            self.val_after_zero = self.value
        self.buffer.append(0)


def part1():
    spin = Spinlock(349)
    for _ in range(2017):
        spin.step()
    print(f"Part 1:  {spin.buffer[spin.position + 1]}")


def part2():
    spin = Spinlock(349)
    for _ in range(int(5e7)):
        print('{:,}'.format(_), end='\r', flush=True)
        spin.quick_step()
    print(f"Part 2: {spin.val_after_zero}")


def test1():
    test_spin = Spinlock(3)
    for _ in range(9):
        test_spin.step()
        print(test_spin)


if __name__ == "__main__":
    #test1()
    part1()
    part2()
