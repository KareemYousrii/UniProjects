import random

class Grid(object):
	"""Generates a random grid."""

	def __init__(self):
		# The robotic parts are seperated from the obstacles so that the state could comprise of only the robotic_parts, 
		# since these are the only entities that are affected by change, unlike the obstacles which are stationery.
		self.dimensions = [random.randint(1,100), random.randint(1,100)]
		self.obstacles = [0] * random.randint(1, self.dimensions[0] * self.dimensions[1])
		self.robotic_parts = [0] * random.randint(1, self.dimensions[0] * self.dimensions[1] - len(self.obstacles))
	
		# Generate a list of random nums used to allocate positions of robotic parts and obstacles	
		random_cells = random.sample(xrange(self.dimensions[0] * self.dimensions[1]), len(self.robotic_parts) + len(self.obstacles))
		
		i = 0
		while i < len(self.robotic_parts):
			self.robotic_parts[i] = random_cells[i]
			i = i + 1
			
		i = 0
		while i < len(self.obstacles):
			self.obstacles[i] = random_cells[i + len(self.robotic_parts)]
			i = i + 1

grid = Grid()

#+-------+
#|   	 |
#|   P	 |
#|		 |	
#+-------+
