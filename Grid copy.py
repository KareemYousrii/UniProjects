import random

tiles = {'obstacle' : -1, 'part' : 1, 'empty' : 0}

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
		
		self.grid = [[0 for x in xrange(dimensions[0])] for x in xrange(dimensions[1])]
		for i in xrange(len(self.obstacles)):
			tmp = self.random_cells[i]
			self.grid[tmp] = tiles['obstacle']

		for i in xrange(len(self.robotic_parts), len(random_cells)):
			tmp = self.random_cells[i]
			self.grid[tmp] = tiles['robotic_parts']


grid = Grid()

#+-------+
#|   	 |
#|   P	 |
#|		 |	
#+-------+
