#!/bin/python3


#


def main():
    with open("inputs/input_day9.txt", 'r') as file:
        stream = file.readline().strip()

    part = 2
    index = 0
    score_total = 0
    uncanc = 0

    stack = []
    cscore = 0
    garbage = False

    while True:
        if index >= len(stream):
            break
        if stream[index] == '!':
            index += 1
        elif garbage:
            if stream[index] == '>':
                garbage = False
            else:
                uncanc += 1
        elif stream[index] == '{':
            cscore += 1
            stack.append(cscore)
        elif stream[index] == '<':
            garbage = True
        elif stream[index] == '}':
            cscore -= 1
            score_total += stack.pop()
        index += 1

    if part == 1:
        result = score_total
    else:
        result = uncanc

    print(result)
   


if __name__ == "__main__":
    main()
