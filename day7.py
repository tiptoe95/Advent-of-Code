from helpers import IntcodeMachine
from itertools import permutations
from inputs.day7_input import seq


def run_sim(phase_combo, feedback=False):
	amp_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}
	input_val = 0
	repeat = True
	while repeat:
		for amp in ['A', 'B', 'C', 'D', 'E']:
			# first input is the phase setting, then the input signal
			if amp_dict[amp] == 0:
				amp_dict[amp] = IntcodeMachine(seq, inputs=[input_val, phase_combo.pop(0)])
			else:
				amp_dict[amp].inputs.append(input_val)

			try:
				output = next(amp_dict[amp].run())
			except StopIteration:
				return output
			input_val = output

		if not feedback:
			repeat = False
	return output


if __name__ == '__main__':
	PART1_FLAG = True
	PART2_FLAG = True
	if PART1_FLAG:
		phase_settings = permutations(range(5))
		maxout, best_combo = 0, 0
		for phase_combo in phase_settings:
			output = run_sim(list(phase_combo))
			if output > maxout:
				maxout = output
				best_combo = phase_combo
		print(f"part 1: {best_combo} gives {maxout} thrust")
	if PART2_FLAG:
		phase_settings = permutations(range(5,10))
		maxout, best_combo = 0, 0
		for phase_combo in phase_settings:
			output = run_sim(list(phase_combo), feedback=True)
			if output > maxout:
				maxout = output
				best_combo = phase_combo
		print(f"part 2: {best_combo} gives {maxout} thrust")
		
