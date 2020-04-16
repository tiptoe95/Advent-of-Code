class ModeError(Exception):
	pass

class Intcode():

	def __init__(self, intcode, phase=None, signal_in=None):
		self.SIG_INT = False
		self.intcode = intcode
		self.cursor = 0
		self.phase = phase
		self.signal_in = signal_in

	def parse_num(self, num):
		command = str(num).zfill(5)
		mode3 = command[0]
		mode2 = command[1]
		mode1 = command[2]
		opcode = command[3:]
		return map(int, (mode3, mode2, mode1, opcode))

	def get_value(self, num, mode):
		if mode == 0:
			val = self.intcode[num]
		elif mode == 1:
			val = num
		else: raise ModeError("invalid mode")
		return val

	def opcode1(self, num1, num2, pos3):
		# adds two inputs and saves to pos3
		self.intcode[pos3] = num1 + num2
		self.cursor += 4

	def opcode2(self, num1, num2, pos3):
		# multiplies 2 inputs and saves to pos3		
		self.intcode[pos3] = num1 * num2
		self.cursor += 4

	def opcode3(self, num):
		# takes an input and saves it to pos1
		pos1 = self.intcode[self.cursor + 1]
		self.intcode[pos1] = num
		self.cursor += 2

	def opcode4(self, mode):
		# outputs value of pos1
		val = self.get_value(self.intcode[self.cursor + 1], mode)
		return val
		self.cursor += 2

	def opcode5(self, a, b):
		# sets instruction pointer to second value if first is non-zero
		if a != 0:
			self.cursor = b
		else:
			self.cursor += 3

	def opcode6(self, a, b):
		# sets instruction pointer to second value if first is zero
		if a == 0:
			self.cursor = b
		else:
			self.cursor += 3

	def opcode7(self, a, b, pos3):
		self.intcode[pos3] = ( 1 if a < b else 0 )
		self.cursor += 4

	def opcode8(self, a, b, pos3):
		self.intcode[pos3] = ( 1 if a == b else 0 )
		self.cursor += 4

	def opcode99(self):
		self.SIG_INT = True
		print("...done")



def test(seq, test_input):
	while not seq.SIG_INT:
		try:
			m3, m2, m1, opc = seq.parse_num(seq.intcode[seq.cursor])
			num1 = seq.get_value(seq.intcode[seq.cursor + 1], m1)
			num2 = seq.get_value(seq.intcode[seq.cursor + 2], m2)
			pos3 = seq.intcode[seq.cursor + 3]
		except IndexError:
			pass
		except ModeError:
			pass

		if opc == 1:
			seq.opcode1(num1, num2, pos3)
		elif opc == 2:
			seq.opcode2(num1, num2, pos3)
		elif opc == 3:
			print(f"giving test value {test_input}...")
			seq.opcode3(test_input)
		elif opc == 4:
			res = seq.opcode4(m1)
			print(res)
		elif opc == 5:
			seq.opcode5(num1, num2)
		elif opc == 6:
			seq.opcode6(num1, num2)
		elif opc == 7:
			seq.opcode7(num1, num2, pos3)
		elif opc == 8:
			seq.opcode8(num1, num2, pos3)
		elif opc == 99:
			seq.opcode99()
		else:
			raise ValueError("invalid opcode")


if __name__ == '__main__':
	from inputs.day5_input import intcode
	seq_ac = Intcode(intcode[:])
	seq_therm = Intcode(intcode[:])
	print("Part 1:")
	test(seq_ac, 1)
	print("\nPart 2:")
	test(seq_therm, 5)