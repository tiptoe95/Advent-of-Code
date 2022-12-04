#!/usr/bin/python3


#


throw_values = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

result_key = {
    "X": 'loss',
    "Y": 'draw',
    "Z": 'win',
}

result_values = {
    "loss": 0,
    "draw": 3,
    "win": 6,
}

matchups = {
    ("A", "X"): 'draw',
    ("A", "Y"): 'win',
    ("A", "Z"): 'loss',
    ("B", "X"): 'loss',
    ("B", "Y"): 'draw',
    ("B", "Z"): 'win',
    ("C", "X"): 'win',
    ("C", "Y"): 'loss',
    ("C", "Z"): 'draw',
}


def get_input(path):
    with open(path, 'r') as file:
        moves = [line.rstrip() for line in file]
    return moves


def score_throw(opp_move, my_move):
    result = matchups[(opp_move, my_move)]
    points = result_values[result] + throw_values[my_move]
    return points


def main():
    input_file = r'inputs/input_day2.txt'
    moves = get_input(input_file)

    # PART 1
    points = []
    for round in moves:
        opp_move, my_move = round.split(" ")
        points.append(score_throw(opp_move, my_move))
    print("Part 1:")
    print(sum(points))

    # PART 2
    points2 = []
    for round in moves:
        opp_move, needed_move = round.split(" ")
        desired_result = result_key[needed_move]
        my_throw = None
        for throw in matchups:
            opp_throw, my_throw = throw
            if opp_throw == opp_move and matchups[throw] == desired_result:
                my_move = my_throw
        if my_throw == None:
            raise ValueError("no match found for desired result")
        points2.append(score_throw(opp_move, my_move))
    print("Part 2:")
    print(sum(points2))


def test():
    moves = ["A Y", "B X", "C Z"]
    points = []
    for move in moves:
        opp_move, my_move = move.split(" ")
        points.append(score_throw(opp_move, my_move))
    print(sum(points))
    print(points)


if __name__ == "__main__":
    main()
