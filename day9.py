from inputs.day9_input import program
from helpers import IntcodeMachine




if __name__ == '__main__':
	test = IntcodeMachine(program, input_val=1)
	print(f"Part 1: {next(test.run())}")

	boost = IntcodeMachine(program, input_val=2)
	print(f"Part 2: {next(boost.run())}")