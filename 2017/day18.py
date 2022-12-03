#!/bin/python3


#


class Duet():

    def __init__(self, commands):
        self.commands = commands
        self.register = [(x, 0) for x in "abcdefghijklmnop"]
        self.pos = 0
        self.last_sound = None
    
    def __repr__(self):
        return ' - '.join(f"{let}{num}" for let, num in self.register)

    def parse_command(self, command, *args):
        command_dict = {"snd": self.sound, \
                        "set": self.set, \
                        "add": self.add, \
                        "mul": self.mul, \
                        "mod": self.mod, \
                        "rcv": self.recover, \
                        "jgz": self.jump}
        ans = command_dict[command](*args)
        self.pos += 1
        return ans

    def get_reg(self, reg):
        try:
            reg_idx = int(reg)
        except ValueError:
            filtered_list = [idx for idx, tup in enumerate(self.register) \
                             if tup[0] == reg]
            reg_idx = filtered_list[0]
        return reg_idx

    def get_val(self, reg):
        reg_idx = self.get_reg(reg)
        reg_val = self.register[reg_idx][1]
        return reg_val

    def sound(self, frequency):
        self.last_sound = self.get_val(frequency)
        return

    def set(self, reg, new_val):
        new_val = self.get_val(new_val)
        reg_idx = self.get_reg(reg)
        letter, value = self.register[reg_idx]
        self.register[reg_idx] = (letter, new_val)
        return

    def add(self, reg, add_val):
        add_val = int(add_val)
        reg_idx = self.get_reg(reg)
        letter, value = self.register[reg_idx]
        self.register[reg_idx] = (letter, value + add_val)
        return

    def mul(self, reg, mul_val):
        try:
            mul_val = int(mul_val)
        except ValueError:
            mul_val = self.get_val(mul_val)
        reg_idx = self.get_reg(reg)
        letter, value = self.register[reg_idx]
        self.register[reg_idx] = (letter, value * mul_val)
        return
    
    def mod(self, reg, mod_val):
        mod_val = self.get_val(mod_val)
        reg_idx = self.get_reg(reg)
        letter, value = self.register[reg_idx]
        self.register[reg_idx] = (letter, value % mod_val)
        return

    def recover(self, x):
        try:
            x = int(x)
        except ValueError:
            x = self.get_val(x)
        if x != 0:
            return self.last_sound
        else:
            return None

    def jump(self, x, offset):
        try:
            offset = int(offset)
        except ValueError:
            offset = self.get_val(offset)
        try:
            x = int(x)
        except ValueError:
            x = self.get_val(x)
        if x > 0:
            self.pos += offset - 1


def get_input(file_path):
    with open(file_path, 'r') as file:
        commands = [x.rstrip() for x in file.readlines()]
    return commands

def part1():
    commands = get_input(r"inputs/input_day18.txt")
    duet = Duet(commands)
    RUN_FLAG = True
    ans = None
    while RUN_FLAG:
        try:
            command = commands[duet.pos]
        except IndexError:
            RUN_FLAG = False
        ans = duet.parse_command(*tuple(command.split(' ')))
        if ans is not None:
            RUN_FLAG = False
    print(f"Part 1: {ans}")


def part2():
    pass


def test1():
    commands = ["set a 1", "add a 2", "mul a a", "mod a 5", "snd a", "set a 0", \
                "rcv a", "jgz a -1", "set a 1", "jgz a -2"]
    duet = Duet(commands)
    RUN_FLAG = True
    ans = 0
    while RUN_FLAG:
        print(duet)
        print(duet.pos)
        try:
            command = commands[duet.pos]
            print(f"command: {command}")
        except IndexError:
            raise IndexError
        ans = duet.parse_command(*tuple(command.split(' ')))
        if ans is not None:
            RUN_FLAG = False
    print(ans)

if __name__ == "__main__":
    #test1()
    part1()
