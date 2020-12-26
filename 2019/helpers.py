class IntcodeMachine():

	def __init__(self, intcode, inputs=[]):
		self.SIG_TERM = False
		self.SIG_WAIT = False
		self.intcode = intcode[:]
		self.cursor = 0
		self.inputs = inputs
		self.relative_base = 0
		self.memory = [0]

	def parse_num(self, num):
		command = str(num).zfill(5)
		mode3 = command[0]
		mode2 = command[1]
		mode1 = command[2]
		opcode = command[3:]
		return map(int, (mode3, mode2, mode1, opcode))

	def get_value(self, num, mode):
		"""returns the appropriate value for an opcode based upon its parameter mode"""
		# position mode
		if mode == 0:
			val = self.intcode[num]
		# immediate mode
		elif mode == 1:
			val = num
		# relative mode
		elif mode == 2:
			val = self.intcode[self.relative_base + num]
		return val

	def get_pos(self, pos, mode):
		"""returns the address for an opcode's output based upon its parameter mode"""
		if mode == 0:
			pos = pos
		elif mode == 1:
			pos = self.cursor + 3
		elif mode == 2:
			pos = self.relative_base + pos
		return pos

	def opcode1(self, num1, num2, pos3):
		# adds two inputs and saves to pos3
		self.intcode[pos3] = num1 + num2
		self.cursor += 4

	def opcode2(self, num1, num2, pos3):
		# multiplies 2 inputs and saves to pos3		
		self.intcode[pos3] = num1 * num2
		self.cursor += 4

	def opcode3(self, pos, input_val):
		# takes an input and saves it to pos1
		self.intcode[pos] = input_val
		self.cursor += 2

	def opcode4(self, num):
		self.cursor += 2
		return num

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

	def opcode9(self, num):
		self.relative_base += num
		self.cursor += 2

	def opcode99(self):
		self.SIG_TERM = True

	def run(self):
		while not self.SIG_TERM:
			try:
				command = self.intcode[self.cursor]
				mode3, mode2, mode1, opcode = self.parse_num(command)
				if opcode in {1, 2, 4, 5, 6, 7, 8, 9}:
					num1 = self.get_value(self.intcode[self.cursor + 1], mode1)
				if opcode in {1, 2, 5, 6, 7, 8}:
					num2 = self.get_value(self.intcode[self.cursor + 2], mode2)
				if opcode in {1, 2, 7, 8}:
					pos3 = self.get_pos(self.intcode[self.cursor + 3], mode3)
					_ = self.intcode[pos3]
				if opcode in {3}:
					pos1 = self.get_pos(self.intcode[self.cursor + 1], mode1)
					_ = self.intcode[pos1]
			except IndexError:
				self.intcode += [0] * 10
				continue

			if opcode == 1:
				self.opcode1(num1, num2, pos3)
			elif opcode == 2:
				self.opcode2(num1, num2, pos3)
			elif opcode == 3:
				self.opcode3(pos1, self.inputs.pop())
			elif opcode == 4:
				output = self.opcode4(num1)
				yield output
			elif opcode == 5:
				self.opcode5(num1, num2)
			elif opcode == 6:
				self.opcode6(num1, num2)
			elif opcode == 7:
				self.opcode7(num1, num2, pos3)
			elif opcode == 8:
				self.opcode8(num1, num2, pos3)
			elif opcode == 9:
				self.opcode9(num1)
			elif opcode == 99:
				self.opcode99()
			else:
				print(f"cursor: {self.cursor}	command: {command}	opcode: {opcode}")
				print(f"{self.intcode[self.cursor: self.cursor+3]}")
				raise ValueError("invalid opcode")


if __name__ == '__main__':
	pass