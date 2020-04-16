from pathlib import Path


def get_input():
    file = 'day5input.txt'
    path = Path.cwd() / 'inputs' / file
    with path.open('r') as input:
        polymer = input.read().splitlines()[0]
    return polymer


def main():
    line = get_input()

    oldline = None
    while oldline != line:
        oldline = line
        for i in range(0,26):
            line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
            line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")

    print("Part1:")
    print(len(line))

    original = line
    best = len(line)
    for j in range(0,26):
        line = original
        line = line.replace(chr(ord("a") + j),"")
        line = line.replace(chr(ord("A") + j),"")
        oldline = None
        while oldline != line:
            oldline = line
            for i in range(0,26):
                line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
                line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")

        best = len(line) if len(line) < best else best
    print("Part2:")
    print(best)


if __name__ == '__main__':
    main()



