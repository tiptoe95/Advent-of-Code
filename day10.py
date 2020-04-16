def count_sightlines(space_map, pos):
	station_x, station_y = pos
	for y, row in enumerate(space_map):
		row = space_map[y]
		for x, ch in enumerate(row):
			if ch == '.':
				continue


def can_see_astroid():
	# note: multiply coords by 10 then divide to get whole number remainders for checking coord ratios
	pass



if __name__ == '__main__':
	with open('inputs/day10_input.txt', 'r') as file:
		space_map = [[line.strip()] for line in file]

	print("Part 1:")
	best_pos = (0,0)
	max_count = 0

	# PART 1
	# loop through each spot in the map and count up conspicuous asteroids for each asteroid
	for y, row in enumerate(space_map):
		row = space_map[y]
		for x, ch in enumerate(row):
			if ch == '.':
				continue
			station_pos = (x, y)
			count = count_sightlines(space_map[:], station_pos)
			if count > max_count:
				max_count = count
				best_pos = station_pos
	print(f"{best_pos} - {max_count} asteroids in view")	
