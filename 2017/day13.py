#!/bin/python3


#


def getInput(filepath):
    data = {}
    with open(filepath, 'r') as file:
        for line in file:
            key, val = line.split(":")
            key = int(key)
                # value is a tuple (A, B, C) where:
                    # A -> depth of layer
                    # B -> position of scanner
                    # C -> direction of scanner travel
            val = (int(val.strip()), 1, 1)
            data.update({key : val})
    return data


class Firewall():

    def __init__(self, layers, delay=0):
        self.layers = layers
        self.length = max(self.layers.keys())
        self.time = 0
        self.position = 0 - delay - 1
        self.severity = 0

    def __str__(self):
        print_depth = 20
        print(f"Picosecond {self.time}:\n")
        headerln = ""
                # print header
        for layer in range(print_depth+1):
            if layer < 10:
                headerln += f" {str(layer)}  "
            else:
                headerln += f" {str(layer)} "
        print(headerln)
                # print visualization
        TOP_LAYER = True
        for level in range(max(k[0] for k in self.layers.values())):
            level_str = ""
            for n in range(print_depth):
                if n not in self.layers:
                    if TOP_LAYER and self.position == n:
                        level_str += "( ) "
                        TOP_LAYER = False
                    else:
                        level_str += "    "
                    continue
                if self.layers[n][0] > level:
                    if self.layers[n][1] == level+1:
                        if TOP_LAYER and self.position == n:
                            level_str += "(S) "
                            TOP_LAYER = False
                        else:
                            level_str += "[S] "
                    else:
                        if TOP_LAYER and self.position == n:
                            level_str += "( ) "
                            TOP_LAYER = False
                        else:
                            level_str += "[ ] "
                else:
                    level_str += "    "
            print(level_str)
        return "\n" 

    def tick(self):
        for layer in self.layers:
            depth, pos, direction = self.layers[layer]
            if pos == depth:
                direction = -1
            elif pos == 1:
                direction = 1
            pos += direction
            self.layers[layer] = (depth, pos, direction)
            if layer == self.position:
                # position 2 implies the scanner is moving out of the position
                # while we're still there
                if pos == 2 and direction == 1:
                    print(f"CAUGHT! layer: {layer} depth: {depth}")
                    self.severity += (layer * depth)
        self.position += 1
        self.time += 1


def part1():
    layers = getInput(r'inputs/input_day13.txt')
    firewall = Firewall(layers)
    while firewall.time <= firewall.length:
        firewall.tick()
    print(f"severity: {firewall.severity}")


def part2():
    layers = getInput(r'inputs/input_day13.txt')
    delay = 1
    min_sev = 1000000
    PASSED = False
    while not PASSED:
        print(f"delay: {delay} ps     low severity: {min_sev}{' '*6}", \
              end='\r', flush=True)
        firewall = Firewall(layers)
        while firewall.time <= firewall.length:
            firewall.tick()
        if firewall.severity < min_sev:
            min_sev = firewall.severity
        if firewall.severity == 0:
            PASSED = True
        delay += 1
    print(f"\npassed through with a delay of {delay} picoseconds")
        


def test():
    layers = {0: (3,1,1), 1:(2,1,1), 4:(4,1,1), 6:(4,1,1)}
    firewall = Firewall(layers)
    for t in range(7):
        firewall.tick()
    print(firewall.severity)
    del firewall

    delay = 10
    min_sev = 1000000
    PASSED = False
    while not PASSED:
        print(f"delay: {delay} ps     low severity: {min_sev}{' '*6}", \
              end='\r', flush=True)
        firewall = Firewall(layers, delay)
        while firewall.time - delay <= firewall.length:
            print(firewall)
            firewall.tick()
        if firewall.severity < min_sev:
            min_sev = firewall.severity
        if firewall.severity == 0:
            PASSED = True
        del firewall
        delay += 1
        return
    print(f"\npassed through with a delay of {delay} picoseconds")


if __name__ == "__main__":
    test()
    #part1()
    #part2()
