from pathlib import Path

# get input
input_file = Path('inputs/day1_input.txt')
with open(input_file) as file:
	modules = [int(line.strip()) for line in file.readlines()]

# part 1
def get_fuel(mass):
	fuel_amt = mass//3 - 2
	return fuel_amt

print("part 1: ", sum(map(get_fuel, modules)))


# part 2
total = 0
count = 0
for mass in modules:
	while (mass := get_fuel(mass)) > 0:
		total += mass
print("part 2: ", total)

