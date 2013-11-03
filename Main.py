import sys

def put_all(queue, elements):
	"""Enqueues a list of elements."""
	
	for element in elements:
		queue.put(element)


def general_search(problem, strategy):
	"""Implements the general search strategy"""
	
	if strategy == "BF":
		nodes = Queue()

	elif strategy == "DF" or strategy == "ID":
		nodes = LifoQueue()

	elif startegy == "ID":
		nodes = PriorityQueue()

	nodes.put(problem.initial_state)
	while not nodes.empty():
		node = nodes.get_nowait()
		if problem.goal_test(node):
			return node
		put_all(nodes, expand(node, problem.actions)

	return False

def expand(node, actions):
	"""Generates all children nodes by applying each 
	action in the set of all actions to the current node."""

	nodes = []
	
	for action in actions:
			problem.transition_model['action']

def visualize(rows, columns):

	# Print the uppermost border
	sys.stdout.write("+")
	for i in xrange(columns):
		sys.stdout.write("-------+")
	sys.stdout.write("\n")

	for i in xrange(rows):
		sys.stdout.write("|")
		for j in xrange(columns):
			sys.stdout.write("       |")		
		sys.stdout.write("\n")
		
		sys.stdout.write("+")
		for j in xrange(columns):
			sys.stdout.write("-------+")
		sys.stdout.write("\n")
