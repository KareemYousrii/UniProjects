class WhereAreMyParts(SearchProblem):

	def goal_test(self, node):


	def path_cost(self, node):


	# action = {}
	def apply_action(self, node, cmd):
		part = cmd[0]
		i = node.state[part] / dim[1]
		j = node.state[part] % dim[1]

		if cmd[1] == "N":
			node.state[part] =
		
		elif cmd[1] == "S":
			node.state[part] =

		elif cmd[1] = "E":
			node.state[part] =

		elif cmd[1] = "W":
			node.state[part] =