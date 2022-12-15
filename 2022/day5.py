#!/usr/bin/python3


import copy


def main():
    input_file = r"inputs/input_day5.txt"
    raw_data = [x for x in  get_input(input_file).split("\n")]
    stack_rows, moves = parse_input(raw_data)

    # transform stacks for easier management
    stack = transform(stack_rows)
    # remove empty spaces so gravity can do its thing when a crate is moved to the stack
    stack = remove_empties(stack)

    # part 1
    # move the crates
    new_stack = copy.deepcopy(stack)
    for move in moves:
        new_stack = move9000(new_stack, move)
    print(f"Part 1:\n{''.join(col[-1] for col in new_stack)}")

    # part 2
    new_stack = copy.deepcopy(stack)
    for move in moves:
        new_stack = move9001(new_stack, move)
    print(f"Part 2:\n{''.join(col[-1] for col in new_stack)}")


def get_input(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()


def parse_input(raw_data: str) -> list:
    rows = []
    moves = []
    parsing_rows = True
    for line in raw_data:
        # Once we hit an empty line we know each subsequent line will be a movement
        if line == "":
            parsing_rows= False
            continue
        if parsing_rows:
            row_line = parse_row_line(line)
            rows.append(row_line)
        else:
            move = parse_move(line)
            moves.append(move)

    # remove bottom line with index labels
    rows = rows[:-1]
    return rows, moves

        
def parse_row_line(line: str) -> list[str]:
    slots = line[1:][::4]
    slots = [x for x in slots]
    return slots


def parse_move(move: str) -> tuple[int]:
    move = move.split(" ")
    move_nums = (move[1], move[3], move[5])
    move_nums = tuple(int(x) for x in move_nums)
    return move_nums


def transform(stack_rows: list[list]) -> list[list]:
    stack = []
    for i in range(len(stack_rows[0])):
        stack.append([])
        for row in stack_rows[::-1]:
            stack[i].append(row[i])
    return stack


def remove_empties(stack: list) -> list:
    for i, column in enumerate(stack):
        stack[i] = [x for x in column if x != " "]
    return stack


def move9000(stack: list[list], move: tuple[int]) -> list[list]:
    amount, source, dest = move
    source -= 1
    dest -= 1
    for _ in range(amount):
        stack[dest].append(stack[source].pop())
    return stack


def move9001(stack: list[list], move: tuple[int]) -> list[list]:
    amount, source, dest = move
    source -= 1
    dest -= 1
    cluster = []
    for _ in range(amount):
        if len(stack[source]) == 0:
            continue
        cluster.append(stack[source].pop())
    stack[dest].extend(cluster[::-1])
    return stack


def test():
    test_file = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
    test_file = test_file.split("\n")[1:]
    [print(x) for x in test_file]
    stack_rows, moves = parse_input([x for x in test_file])
    stack = transform(stack_rows)
    stack = remove_empties(stack)
    # part 1
    # move the crates
    new_stack = copy.deepcopy(stack)
    for move in moves:
        new_stack = move9000(new_stack, move)
    print(f"Part 1:\n{''.join(col[-1] for col in new_stack)}")
    print()
    print(stack)
    print()
    # part 2
    new_stack2 = copy.deepcopy(stack)
    for move in moves:
        print(new_stack2)
        new_stack2 = move9001(new_stack2, move)
    print(f"Part 2:\n{''.join(col[-1] for col in new_stack2)}")


if __name__ == "__main__":
    main()
