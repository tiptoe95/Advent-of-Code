#!/usr/bin/python3


#


def main():
    grid = get_data("inputs/input_day8.txt")

    # PART 1
    visible_trees = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            coord = (r, c)
            tree_height = grid[r][c]
            n, s, e, w = list_tree_heights(grid, coord)
            nsew = (n, s, e, w)
            if is_tree_visible(tree_height, nsew):
                visible_trees += 1
    print(f"visible trees: {visible_trees}")

    # PART 2
    scenic_score = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            coord = (r,c)
            scenic_score = max(scenic_score, get_scenic_score(grid, coord))
    print(f"highest scenic score: {scenic_score}")


def is_tree_visible(tree_height, nsew):
    n, s, e, w = nsew
    for direction in (n, s, e, w):
        if len(direction) == 0:
            return True
        if max(direction) < tree_height:
            return True
    return False


def list_tree_heights(grid, coord):
    r, c = coord
    n, s, e, w = [], [], [], []
    # north eval
    for j in range(r):
        n.append(grid[j][c])
    # south eval
    for j in range(len(grid)-r-1):
        s.append(grid[-j-1][c])
    # east eval
    e = grid[r][c+1:]
    # west eval
    w = grid[r][:c]
    return (n[::-1], s[::-1], e, w[::-1])


def get_scenic_score(grid, coord):
    r, c = coord
    tree_height = grid[r][c]
    n, s, e, w = list_tree_heights(grid, coord)
    scores = []
    for direction in (n, s, e, w):
        scores.append(line_of_sight(direction, tree_height))
    return prod_reduce(scores)


def line_of_sight(lst, tree_height):
    visible = 0
    for tree in lst:
        if tree < tree_height:
            visible += 1
        else:
            visible += 1
            break
    return visible


def prod_reduce(lst):
    n = 1
    for x in lst:
        n *= x
    return n


def get_data(input_path):
    with open(input_path, 'r') as file:
        grid = []
        for line in file.readlines():
            row = [int(x) for x in line.strip()]
            grid.append(row)
    return grid


def test(coord):
    grid = [[3,0,3,7,3],
            [2,5,5,1,2],
            [6,5,3,3,2],
            [3,3,5,4,9],
            [3,5,3,9,0]]
    for trees in list_tree_heights(grid, coord):
        print(f"trees for coord {coord}")
        print(trees)
    ss = get_scenic_score(grid, coord)
    print(f"scenic score: {ss}")


if __name__ == "__main__":
    test_run = False
    if not test_run:
        main()
    else:
        test_coord = (1,2)
        test(test_coord)
