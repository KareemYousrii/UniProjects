import abc

class SearchProblem(object):
	"""Generic Search Problem"""
	__metaclass__ = abc.ABCMeta

	def __init__(self, initial_state, actions):
		self.initial_state = initial_state
		self.actions = actions

	@abc.abstractmethod
	def goal_test(self, node):
		"""Performs the goal test on the given node"""

	@abc.abstractmethod
	def path_cost(self, node):
		"""Assigns the path cost to the sequence of actions 
		resulting in the state in the specified node"""

	@abc.abstractmethod
	def apply_action(self, node, action):
		"""Applies a specific action to a certain node"""

# actions = {'n', 's', 'e', 'w'}
# initial_state = grid.robotic_parts
# state_space = 
# goal test