import sys
import math
import copy
from queue import Queue, LifoQueue, PriorityQueue

def eval_fun_1(node):
	"""This heuristic function assigns a cost to a state based 
	on the number of disconnected clusters of parts. Returns the
	number of clusters."""

	state = copy.deepcopy(node.state)

	clusters = 0

	for i in xrange(len(state)):
		if state[i] == -1:
			pass
		
		else:
			for adj in state[i].adj_list:
				state[adj] = -1

			clusters +=1

	return clusters - 1

def eval_fun_2(node):
	"""This heuristic function assigns a cost to a state based on the estimated 
	number of steps between all the parts and a reference part, not accounting 
	for the presence of obstacles.This is done through finding the smallest distance
	between two clusters."""
	parts = copy.deepcopy(node.state)
	for part in parts:
		if part != -1:
			for adjacent in part.adj_list:
				parts[adjacent] = -1

	clusters = []

	for i in xrange(parts):
		if parts[i] != -1:
			clusters.add(i)

	reference_cluster = 0
	total_steps = 0
	for i in clusters:
		total_steps += find_least_steps(reference_cluster, i)

	return total_steps

def id_search(problem):
	"""Performs iterative deepening depth first search
	 on a given search problem. Returns the goal node."""

	i = 0
	while depth_limited_search(problem, i) == False:
		i += 1

def depth_limited_search(problem, depth):
	"""Performs depth limited search on a given search problem.
	Returns the goal node if the goal was found, and return False otherwise."""

	nodes = LifoQueue()

	nodes.put(Node(problem.initial_state))
	while not nodes.empty():
		node = nodes.get_nowait()
		if problem.goal_test(node):
			return node

		if node.depth != depth:
			put_all(nodes, expand(node, problem.actions)

	return False

def general_search(problem, strategy):
	"""Implements the general search strategy"""
	
	if strategy == "BF":
		nodes = Queue()

	elif strategy == "DF":
		nodes = LifoQueue()

	elif strategy == "AS1" or "AS2" or "GR1" or "GR2":
		nodes = PriorityQueue()

	elif strategy == "ID":
		id_search(problem)

	nodes.put(Node(problem.initial_state))
	while not nodes.empty():
		node = nodes.get_nowait()
		if problem.goal_test(node):
			return node
		put_all(nodes, expand(node, problem, strategy))

	return False

def put_all(queue, elements):
	"""Enqueues a list of elements in a referenced list."""
	
	for element in elements:
		queue.put(element)

def expand(node, problem, search):
	"""Generates all children nodes by applying each 
	action in the set of all actions to the current node.
	Returns a list of the children of the current node"""

	nodes = []
	actions = problem.actions

	for part in node.state:
		for action in actions:
			new_state = problem.apply_action(node, (part,action))

			if search == 'GR1':
				nodes.put(Node(new_state, node, action, depth = node.depth + 1, cost = eval_fun_1(new_state)))

			elif search == 'GR2':
				nodes.put(Node(new_state, node, action, depth = node.depth + 1, cost = eval_fun_2(new_state)))

			elif search == 'AS1':
				nodes.put(Node(new_state, node, action, depth = node.depth + 1, cost = (node.cost + 1) + eval_fun_1(new_state)))

			elif search == 'AS2':
				nodes.put(Node(new_state, node, action, depth = node.depth + 1, cost = (node.cost + 1) + eval_fun_2(new_state)))

			else:
				nodes.put(Node(new_state, node, action, depth = node.depth + 1, cost = node.cost + 1))

	return nodes

def find_least_steps(cluster_1, cluster_2, state):
	least_parts = [-1,-1]
	least_dist = 9999
	for i in cluster_1.adj_list:
		for j in cluster_2.adj_list:
			new_dist = math.sqrt((state[j].coords[0] - state[i].coords[0]) ** 2 + (state[j].coords[1] - state[i].coords[1]) ** 2)
			if new_dist < least_dist:
				least_dist = new_dist
				least_parts = [i, j]

	least_steps = 0
	if state[i].coords[0] != state[j].coords[0]:
		least_steps += 1

	if state[i].coords[1] != state[j].coords[1]:
		least_steps += 1

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



