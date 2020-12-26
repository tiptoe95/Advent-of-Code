from pathlib import Path


# get inputs
input1_file = Path('inputs/day3-1_input.txt')
input2_file = Path('inputs/day3-2_input.txt')
output_file = Path('outputs/day3-1.txt')

with open(input1_file) as input_file:
	moves1 = input_file.readline().split(',')
with open(input2_file) as input_file:
	moves2 = input_file.readline().split(',')


# setup grid
class Grid():

	def __init__(self):
		self.grid = [
			['.', '.', '.'],
			['.', 'o', '.'],
			['.', '.', '.']]
		self.x = 1
		self.y = 1
		self.origin_x = 1
		self.origin_y = 1

	def move_up(self, distance, id_num):
		for i in range(distance):
			if self.y == 0:
				self.grid.insert(0, ['.']*len(self.grid[0]))
				self.origin_y += 1
			else: 
				self.y -= 1
			self.grid[self.y][self.x] = self.check_spot(self.grid[self.y][self.x], id_num)

	def move_down(self, distance, id_num):
		for i in range(distance):
			if self.y == len(self.grid) - 1:
				self.grid.append(['.']*len(self.grid[0]))
			self.y += 1
			self.grid[self.y][self.x] = self.check_spot(self.grid[self.y][self.x], id_num)

	def move_left(self, distance, id_num):
		for i in range(distance):
			if self.x == 0:
				for row in self.grid:
					row.insert(0, '.')
				self.origin_x += 1
			else:
				self.x -= 1
			self.grid[self.y][self.x] = self.check_spot(self.grid[self.y][self.x], id_num)

	def move_right(self, distance, id_num):
		for i in range(distance):
			if self.x == len(self.grid[0]) - 1:
				for row in self.grid:
					row.append('.')
			self.x += 1
			self.grid[self.y][self.x] = self.check_spot(self.grid[self.y][self.x], id_num)

	def new_wire(self):
		self.x, self.y = self.origin_x, self.origin_y

	def check_spot(self, active_spot, id_num):
		if active_spot == '.':
			active_spot = id_num
		elif active_spot == 'o' or active_spot == id_num:
			pass
		elif type(active_spot) == type(id_num):
			active_spot = 'X'
		else:
			print("error found when matching characters")
		return active_spot


# draw lines
grid1 = Grid()

def draw_wire(move_set, id_num):
	for move in move_set:
		direction = move[0]
		distance = int(move[1:])
		if direction == 'U':
			grid1.move_up(distance, id_num)
		elif direction == 'D':
			grid1.move_down(distance, id_num)
		elif direction == 'L':
			grid1.move_left(distance, id_num)
		elif direction == 'R':
			grid1.move_right(distance, id_num)

draw_wire(moves1, 1)
grid1.new_wire()
draw_wire(moves2, 2)
print(f"origin: ", grid1.grid[grid1.origin_y][grid1.origin_x], '\n')

WRITE_OUT_GRID = False
if WRITE_OUT_GRID:
	with open(output_file, 'w+') as file:
		file.write(f"width x height --> {len(grid1.grid[0])} x {len(grid1.grid)}\t")
		for row in grid1.grid:
			for item in row:
				file.write(str(item))
			file.write('\n')

# find all intersections
intersections = []
manhatten_distances = []
for r, row in enumerate(grid1.grid):
	for c, char in enumerate(row):
		if char == 'X':
			intersections.append((r,c))
for k, intersection in enumerate(intersections):
	y, x = intersection
	x_diff, y_diff = abs(grid1.origin_x - x), abs(grid1.origin_y - y)
	manhatten_distances.append(x_diff + y_diff)
print(min(manhatten_distances))

