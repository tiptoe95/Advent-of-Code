# PART 1
def get_passwd(minim, maxim):
	possibilities = set()
	for num in range(minim, maxim+1):
		if test_num(num):
			possibilities.add(num)
	return possibilities

def test_num(num):
	strnum = str(num)
	HAS_DOUBLE = False
	for i, digit in enumerate(strnum):
		try:
			if int(strnum[i+1]) < int(digit):
				return False

			if not HAS_DOUBLE:
				if strnum[i+1] == digit:
					HAS_DOUBLE = True
		except IndexError:
			continue
	return True if HAS_DOUBLE else False


# PART 2
def bad_double(num):
	num = list(str(num))
	for digit in num:
		if num.count(digit) == 2:
			return True
	return False


if __name__ == '__main__':
	input_min, input_max = 231832, 767346
	res = get_passwd(input_min, input_max)
	print(f"part 1: {len(res)}")

	res2 = set(filter(bad_double, res))
	print(f"part 2: {len(res2)}")