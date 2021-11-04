#!/bin/python3


input = 368078


def main():
    ans = part1(input)
    print(ans)


def part1(input):
    # determine how many complete "rings" there are
    rings = 1
    while critical_square(rings) < input:
        rings += 1
    rem = input - critical_square(rings-1)
    # determine which side the remainder ends up on
    side_length = 2*(rings)
    travel = rem % (side_length)
    deviance = abs( travel - (side_length // 2) )
    
    # manhattan distance is distance to the ring plus the deviance from the mid
    distance = rings + deviance
    return distance

def part2():
    pass


def critical_square(ring):
    return (2*ring + 1)**2


def cheat():
    inp = 368078

    def next_coords(x, y):
        if x == y == 0: return (1, 0)
        if y > -x and x > y: return (x, y+1)
        if y > -x and y >= x: return (x-1, y)
        if y <= -x and x < y: return (x, y-1)
        if y <= -x and x >= y: return (x+1, y)

    x, y = 0, 0
    vals = { (0, 0): 1 }
    while vals[(x, y)] <= inp:
        x, y = next_coords(x, y)
        vals[(x, y)] = sum(vals.get((x+i, y+j), 0) for i in [-1, 0, 1] for j in [0, 1, -1])
    print(vals[(x, y)])


if __name__ == "__main__":
    main()
    cheat()
