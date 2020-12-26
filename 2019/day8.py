from collections import defaultdict


def part1(layers):
	layer = min(layers, key=lambda x: ''.join(layers[x]).count('0'))
	print(f"layer {layer} has the least instances of '0'")
	ones = ''.join(layers[layer]).count('1')
	twos = ''.join(layers[layer]).count('2')
	return ones * twos


def part2(layers):
	img = [['-' for _ in range(25)] for _ in range(6)]
	for r, row in enumerate(img):
		for c, digit in enumerate(row):
			layer = 0
			while (pixel := layers[layer][r][c]) == '2':
				layer += 1
			if pixel == '1':
				pixel = '\u2588'
			elif pixel == '0':
				pixel = ' '
			else:
				pixel = '?'
			img[r][c] = pixel

	for line in img:
		print(''.join(line))


if __name__ == '__main__':
	im_width = 25
	im_height = 6
	with open('inputs/day8_input.txt') as input_file:
		input_str = input_file.read()
	layers = defaultdict(list)
	count = 0
	while len(input_str) > 24:
		if len(layers[count]) < 6:
			layers[count].append(input_str[:25])
			input_str = input_str[25:]
		else:
			count += 1

	print(f"Part 1: {part1(layers)}")
	print("Part 2:")
	part2(layers)