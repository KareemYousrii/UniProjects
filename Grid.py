import random
from part import Part
from queue import Queue
import sys

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
		
		# Mapping the grid indexes to coordinates for both the parts and obstacles
		i = 0
		while i < len(self.robotic_parts):
			self.robotic_parts[i] = Part([random_cells[i] / self.dimensions[1], random_cells[i] % self.dimensions[1]]) #
			i = i + 1
			
		i = 0
		while i < len(self.obstacles):
			self.obstacles[i] = [random_cells[i + len(self.robotic_parts)] / self.dimensions[1], 
				random_cells[i + len(self.robotic_parts)] % self.dimensions[1]]
			i = i + 1

		# Populating the adjacency lists for each of the robotic parts
		coord_transformations = [[1, 0], [-1, 0], [0, 1], [0, -1]]
		for part in self.robotic_parts:

			# Perform a bfs on each of the robotic parts to create its adjacency list.
			parts = Queue()
			parts.put(part)

			while not parts.empty():
				curr_part = parts.get_nowait()

				# Coordinates of the current part
				x = curr_parts.coords[0]
				y = curr_part .coords[1]

				# Check for parts in the 4 adjacent cells
				for i in xrange(4):

					is_occupied = check_occupation([x + coord_transformations[i][0], y + coord_transformations[i][1]])
					
					if is_occupied != False:
						q.put(self.robotic_parts[is_occupied])
						part.adj_list.add(is_occupied) # Add the index of the part occupying the cell


	def check_occupation(coords):
		"""Checks whether a given cell on the grid is occupied or not.
		Returns the index of the part occuping the cell if it is occupied.
		Returns False otherwise."""

		for i in xrange(len(self.robotic_parts)):
			if coords == self.robotic_parts[i]:
				return i

		return False



grid = Grid()

#+-------+
#|   	 |
#|   P	 |
#|		 |	
#+-------+
