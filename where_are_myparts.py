from searchproblem import SearchProblem
from node import Node

transform_coords = {'N' : [0, -1], 'S' : [0, 1], 'E' : [1, 0], 'W' : [-1, 0]}

class WhereAreMyParts(SearchProblem):

	def __init__(self, initial_state, actions, grid):
		super().init(initial_state, actions)
		self.grid = grid

	def goal_test(self, node):
		"""Checks if all parts are reachable from a single part.
		Return True or False."""

		# If the adjacency list of one part contains all other parts, 
		#then we have reached the goal state
		if len(self.initial_state[0].adj_list) == len(self.initial_state):
			return True

	def path_cost(self, node):
		int cost = 0
		while node.parent != None:
			cost = cost + 1
			node = node.parent

		return cost

	def check_occupation(coords, state):
		"""Checks whether a given cell on the grid is occupied or not.
		Returns the index of the part occuping the cell if it is occupied.
		Returns False otherwise."""

		for i in xrange(len(state)):
			if coords == state[i].coords:
				return i

		return False

	def share_same_cluster(p1, p2, state): # The indices of the parts in the state
		"""Checks that two parts are not in the same cluster.
		Returns True or False."""

		if p1 in state[p2].adj_list:
			return True

		else:
			return False

	def apply_action(self, node, cmd):
		"""Applies a move action on a robotic part and all its connected parts. 
		Returns a new state."""
		
		new_state = copy.deepcopy(node.state) # State of the newly created node

		# A list of indices of all the robotic parts connected to the current part
		cluster = copy.deepcopy(part.adj_list)
		cluster.add(int(cmd[0])) # Add the current part to the list

		transformation = transform_coords[cmd[1]] # Transformation to be applied to the coordinates

		flag = True
		while flag: # iteratively add units steps to the set of parts until one of the condition no longer holds
			
			for i in cluster: # Add a unit step to each part
				part = new_state[i]
				x = part.coords[0]
				y = part.coords[1]

				if [x + transformation[0], y + transformation[1]] in grid.obstacles:
					flag = False
					break

				# If the cluster hits another part, this part becomes part of the cluster
				is_occupied = check_occupation([x + transformation[0], y + transformation[1]], new_state)
				elif is_occupied != False and not share_same_cluster(is_occupied, i, node.state):  
					flag = False
					break

				# GT was used as opposed to GE to handle the case where a cluster of connected parts is stopped by an obstacle,
				# while having some members against the barbed wire
				elif x + transformation[0] > grid.dimensions[0] - 1 or y + transformation[1] > grid.dimensions[1] - 1:
					return None

				else:
					x = x + transformation[0]
					y = y + transformation[1]

		# Check if any of the parts is connected to a new part. If so, update the adjacency lists
		# of all parts adjacet to thhe connected part
		for i in cluster:
			part = new_state[i]
			x = part.coords[0]
			y = part.coords[1]

			# Check if the border of the cluster contains any unadded parts
			is_occupied = check_occupation([x + transformation[0], y + transformation[1]])
			if is_occupied != False:

				# Add the new part to adj list of all parts in the cluster
				for j in cluster:
					new_state[j].adj_list.add[is_occupied]

				# Add all parts in the cluster to the adj list of the new part
				for j in cluster:
					new_state[is_occupied].adj_list.add(new_state[j])

				# Add all parts in the cluster to each of the parts adjacent to the new part
				for j in new_state[is_occupied].adj_list:
					for k in new_state[i].adj_list:
						new_state[j].adj_list.add(k)

		return new_state








