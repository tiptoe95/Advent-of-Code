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


if __name__ == "__main__":
    main()
