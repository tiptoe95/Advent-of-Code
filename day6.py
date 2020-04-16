class SolarSys():


	def __init__(self, orbit_list):
		self.census = []
		self.untethered = []
		self.census.append(Satellite('COM'))

		for item in orbit_list:
			orbitee_name, orbiter_name = self.parse_orbit(item)
			orbiter_list = [x for x in self.census if x.name == orbiter_name]
			orbitee_list = [x for x in self.census if x.name == orbitee_name]

			if len(orbiter_list) == 0:
				orbiter = Satellite(orbiter_name)
				self.census.append(orbiter)
			elif len(orbiter_list) > 1:
				print(f"ORBITER LIST: {orbiter_list}")
				raise ValueError("name conflict in census")
			else:
				orbiter = orbiter_list[0]
				if orbiter in self.untethered:
					self.untethered.remove(orbiter)
			
			if len(orbitee_list) == 0:
				orbitee = Satellite(orbitee_name, orbiter)
				self.census.append(orbitee)
				self.untethered.append(orbitee)
			elif len(orbitee_list) > 1:
				print(f"ORBITEE LIST: {orbitee_list}")
				raise ValueError("name conflict in census")
			else:
				orbitee = orbitee_list[0]
				orbitee + orbiter
						# adds orbiter to orbitee's list of orbiters
			orbiter.parent = orbitee

	def parse_orbit(self, line):
		orbitee, orbiter = line.split(')')
		return orbitee, orbiter

	def checksum(self):
		COM = self.census[0]
		self.orbit_count = 0
		self.count_orbits(COM, 0)
		print(f"checksum: {self.orbit_count} orbits")

	def count_orbits(self, satt, depth):
		"""Recursively determines depth of each planet and adds it to total orbits"""
		satt.depth = depth
		for orbiter in satt.orbiters:
			self.orbit_count += depth + 1
			self.count_orbits(orbiter, depth + 1)

	def find_santa(self):
		"""Creates a branch from COM to YOU and SAN and compares at the point at which the branches diverge"""
		YOU = next(planet for planet in self.census if planet.name == "YOU")
		SAN = next(planet for planet in self.census if planet.name == "SAN")
		YOU_path, SAN_path = [], []
		curr_body = YOU
		for i in range(YOU.depth):
			YOU_path.append(curr_body.parent)
			curr_body = curr_body.parent
		curr_body = SAN
		for i in range(SAN.depth):
			SAN_path.append(curr_body.parent)
			curr_body = curr_body.parent
		YOU_path.reverse()
		SAN_path.reverse()
		print(YOU_path)
		print(SAN_path)
		for i in range(min(len(YOU_path), len(SAN_path))):
			if YOU_path[i] != SAN_path[i]:
				merge_depth = i - 1
				break
		num_jumps = (SAN.depth - merge_depth) + (YOU.depth - merge_depth) - 2
				# subtract 2 because no orbit transfer is necessary at merge point as well as from final planet to santa
		print(num_jumps, " jumps")



class Satellite():

	def __init__(self, name, orbiter=None):
		self.name = name
		self.parent = None
		self.orbiters = []
		self.depth = None
		if orbiter:
			self.orbiters.append(orbiter)

	def __add__(self, other):
		self.orbiters.append(other)

	def __repr__(self):
		return self.name



if __name__ == '__main__':
	with open('inputs/day6_input.txt', 'r') as input_file:
		orbit_list = [line.strip() for line in input_file.readlines()]

	test = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']
	ptest = SolarSys(test)
	ptest.checksum()
	ptest.find_santa()
	p1 = SolarSys(orbit_list)
	p1.checksum()
	p1.find_santa()