class Part(object):

	def __init__(self, coords):
		self.coords = coords
		self.adj_list = set()