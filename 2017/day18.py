#!/usr/bin/python3


#


class Duet:

    def __init__(self, code):
        self.registers = dict((x, 0) for x in "abcdefghijklmnopqrstuvwxyz")
        self.code = code
        self.cmd_dict = {
            "snd": self.cmd_snd,
            "set": self.cmd_set,
            "add": self.cmd_add,
            "mul": self.cmd_mul,
            "mod": self.cmd_mod,
            "rcv": self.cmd_rcv,
            "jgz": self.cmd_jgz,
        }
        self.last_sound = None
        self.index = 0
        self.step = 0
        self.STOP_ITER = False

    def __repr__(self):
        keys = [x for x in self.registers.keys() if not None]
        keys.sort()
        s = ""
        for x in keys:
            s += (f"\t{x} - {self.registers[x]}\n")
        return s

    def run(self):
        while not self.STOP_ITER:
            self.run_step()

    def run_step(self):
        cmd, reg, val = self.code[self.index]
        print(f"{self.step} command <{cmd}, {reg}, {val}>")
        if val is not None:
            self.cmd_dict[cmd](reg, val)
        else:
            self.cmd_dict[cmd](reg)
        print(self)
        self.index += 1
        self.step += 1
#        if self.step > 100:
#            self.STOP_ITER = True

    def cmd_snd(self, x):
        # Plays a sound with frequency equal to the value of x
        freq = self.get_value(x)
        print(f"doot ({freq} hz)")
        self.last_sound = freq

    def cmd_set(self, x, y):
        # sets register x to the value of y
        self.registers[x] = self.get_value(y)

    def cmd_add(self, x, y):
        # increases register x by the value of y
        self.registers[x] += self.get_value(y)

    def cmd_mul(self, x, y):
        # sets register x to the result of multiplying the value contained in register x by the value of y
        self.registers[x] *= self.get_value(y)

    def cmd_mod(self, x, y):
        # sets register x to the remainder of dividing the value contained in register x by the value of y
        self.registers[x] = self.get_value(x) % self.get_value(y)

    def cmd_rcv(self, x):
        # recovers the frequency of the last sound played, but only if x is non-zero
        if self.get_value(x) == 0:
            print("recovery empty")
            pass
        else:
            sound = self.last_sound
            print(sound)
            if sound != 0:
                self.STOP_ITER = True


    def cmd_jgz(self, x, y):
        # jumps with an offset of the value of y, but only if x > 0.
        # An offset of 2 skips the next instruction, while -1 jumps to the previous one
        jump = self.get_value(y)
        if self.get_value(x) < 1:
            pass
        else:
            self.index += jump

    def get_value(self, x):
        # returns the value of x, whether it is an integer or a register

        if type(x) is int:
            return x
        elif type(x) is str:
            return self.registers[x]
        else:
            raise ValueError(f"invalid type {type(x)}")


def get_input(filepath):
    with open(filepath, 'r') as file:
        code = [line.strip() for line in file.readlines()]
    return code


def parse_input(code):
    parsed_code = []
    for instruction in code:
        x = instruction.split(" ")
        if len(x) == 3:
            try:
                # if value is a number, convert it to type int
                value = int(x[2])
            except ValueError:
                # if value can't be an int, leave it as type str to reference register
                value = x[2]
        else:
            value = None

        try:
            reg = int(x[1])
        except ValueError:
            reg = x[1]
        cmd = x[0]
        parsed_code.append((cmd, reg, value))
    return parsed_code


def main():
    code = get_input('inputs/input_day18.txt')
    code = parse_input(code)
    duet = Duet(code)
    duet.run()
    pass


def test():
    code = [
    "set a 1",
    "add a 2",
    "mul a a",
    "mod a 5",
    "snd a",
    "set a 0",
    "rcv a",
    "jgz a -1",
    "set a 1",
    "jgz a -2"]
    duet = Duet(parse_input(code))
    duet.run()


if __name__ == '__main__':
    #test()
    main()
