from pathlib import Path
from collections import defaultdict
import time
import threading
import multiprocessing


def new_grid(coords):
    # create an empty grid
    max_x = max(coord[0] for coord in coords)
    max_y = max(coord[1] for coord in coords)
    max_vals = max_x, max_y
    print(f"max x:{max_x}\nmax y:{max_y}")
    grid = []
    for y in range(max_y):
        grid.append([])
        for x in range(max_x):
            grid[y].append('-')
    return grid, max_vals


def get_input():
    input_file = 'day6input.txt'
    input_path = Path.cwd() / 'inputs' / input_file
    with input_path.open('r') as coord_file:
        coords = [line.strip() for line in coord_file]
    for i, coord in enumerate(coords):
        coords[i] = list(map(int, coord.split(',')))
    return coords


def writeout(grid):
    writepath = Path.cwd() / 'visual.txt'
    with writepath.open('w') as visual:
        for row in grid:
            visual.write(''.join(row) + '\n')


def add_coords(grid, coords):
    for x, y in coords:
        grid[len(grid) - y][x-1] = 'X'
    return grid


def find_coord(cell, coords, max_vals):
    cell_row, cell_col = cell
    step = 1
    LOST_FLAG = True
    closest = False
    out_of_bounds = False

    # this loop was a bitch to write
    while LOST_FLAG:
        for row in range(-step, step+1):
            stride = step - abs(row)
            for direction in [-1, 1]:
                spot = [cell_col + stride*direction, cell_row + row]
                x, y = spot[0], spot[1]
                if (x < 0 or x > max_vals[0]) \
                        or (y < 0 or y > max_vals[1]):
                    out_of_bounds = True

                if spot in coords:
                    if LOST_FLAG:
                        closest = f'{spot}'
                        LOST_FLAG = False
                    else:
                        closest = '.'
                        return closest
                if stride == 0:
                    break
        step += 1
    return closest, out_of_bounds


def analyze_cell(grid, row, cell, coords, coord_ids, max_vals, oob_coords):
    if cell == '-':
        cell_location = (grid.index(row), row.index(cell))
        closest_coord, oob = find_coord(
                             cell_location, coords, max_vals)
        if not oob:
            coord_ids[closest_coord] += 1
            print(f"space belongs to {closest_coord}, "
                  f"it's tally is {coord_ids[closest_coord]}")
        else:
            oob_coords.update(closest_coord)
    return coord_ids, oob_coords


def tally_areas(grid, coords, max_vals):
    coord_ids = defaultdict(int)
    total_cells = max_vals[0] * max_vals[1]
    cell_num = 1
    oob_coords = {}

    for row in grid:
        for cell in row:

            # todo: perhaps add threads here for multiprocessing
            # todo: create 4 threads
            print(f"analyzing cell {cell_num}/{total_cells}")
            cell_num += 1

            analyze_cell()

            # todo: join threads here before continuing

    return coord_ids, oob_coords


def main():
    coords = get_input()
    grid, max_vals = new_grid(coords)
    grid = add_coords(grid, coords)
    coord_talleys, oob_coords = tally_areas(grid, coords, max_vals)

    # todo: remove oob coords from top entries

    top_coord = max(coord_talleys, key=coord_talleys.get) # todo: fix 'max() arg is an empty sequence'
    print(f"{top_coord} is the top coordinate")
    print(f"coordinate talleys: ")
    print(coord for coord in coord_talleys)
    print(f"out of bounds coordinates: ")
    print(oob for oob in oob_coords)
    # writeout(grid)

    return


if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    delta_t = t2 - t1
    print(f"elapsed time: {delta_t}")
