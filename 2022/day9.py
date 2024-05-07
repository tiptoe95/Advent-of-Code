#!/usr/bin/python3


import matplotlib.pyplot as plt
import numpy as np


def main():
    data = get_input("inputs/input_day9.txt")
    part1 = Grid(data)
    move_count = 0
    for move in part1.moves:
        direction, steps = move
        for step in range(steps):
            part1.update_head_pos(direction)
            part1.update_tail_pos()
            part1.print_coords()
            move_count += 1
    print(len(part1.visited))
    part1.draw()
    return


def test():
    x = get_input("inputs/input_day9.txt")
    print(x)


def get_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    moves = []
    for line in lines:
        x, y = line.split(" ")
        direction = x
        distance =  int(y)
        moves.append((direction, distance))
    return moves


class Grid():

    def __init__(self, moves):
        self.moves = moves
        self.h_x = 0
        self.h_y = 0
        self.t_x = 0
        self.t_y = 0
        self.visited = set((0,0))
        self.h_coords = [(0,0)]
        self.t_coords = [(0,0)]

    def update_head_pos(self, step_direction):
        match step_direction:
            case "U":
                self.h_y += 1
            case "D":
                self.h_y -= 1
            case "L":
                self.h_x -= 1
            case "R":
                self.h_x += 1
        self.h_coords.append((self.h_x, self.h_y))

    def update_tail_pos(self):
        vert_dist = self.h_y - self.t_y
        horz_dist = self.h_x - self.t_x
        # check for vertical separation
        if abs(vert_dist) > 1:
            if vert_dist < 0:
                self.t_y -= 1
            else:
                self.t_y += 1
            # add diagonal component
            self.t_x += horz_dist
        # check for horizontal separation
        elif abs(horz_dist) > 1:
            if horz_dist < 0:
                self.t_x -= 1
            else:
                self.t_x += 1
            # add diagonoal component
            self.t_y += vert_dist
        # update visited coordinates
        tail_pos = (self.t_x, self.t_y)
        self.visited.add(tail_pos)
        self.t_coords.append(tail_pos)

    def print_coords(self):
        print(f"head: ({self.h_x}, {self.h_y})")
        print(f"tail: ({self.t_x}, {self.t_y})")
        print()

    def draw(self):
        hx = [c[0] for c in self.h_coords]
        hy = [c[1] for c in self.h_coords]
        tx = [c[0] for c in self.t_coords]
        ty = [c[1] for c in self.t_coords]

        x_min, y_min = -10, -10
        x_max, y_max = 10, 10

        fig, ax = plt.subplots()

        for t in range(len(hx)):
            ax.set_xlim(-10,10)
            ax.set_ylim(-10,10)
            head, = ax.plot(hx[t], hy[t], marker="H", linestyle="None")
            plt.pause(0.5)
            tail, = ax.plot(tx[t], ty[t], marker="H", linestyle="None")
            plt.pause(1)



if __name__ == '__main__':
    main()
