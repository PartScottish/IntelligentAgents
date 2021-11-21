class Node:
	#Consider adding ID to node for easier searching? 
	def __init__(self, y: int, x: int):
		# self._coord = Coord(y, x)
		self._x = x
		self._y = y
		self._branches = [None, None, None, None]

	def addNeighbour(self, node, position):
		# North = 0
		# East = 1
		# South = 2
		# West = 3
		self._branches[position] = node

	def distanceToNeighbour(self, position):
		#subtracts differences and if even move is vertical, else move is horizontal
		if position % 2:
			return abs(self.xcoord - self._branches[position].xcoord)
		else:
			return abs(self.ycoord - self._branches[position].ycoord)
		# North = 0
		# East = 1
		# South = 2
		# West = 3

	@property
	def xcoord(self):
		return self._x

	@property
	def ycoord(self):
		return self._y

	@property
	def branches(self):
		return self._branches
		
	def equals(self, node):
		return self._x == node.xcoord and self._y == node.ycoord

	def pathTo(self, node):
		for branch in self._branches:
			if branch.path[-1].equals(node):
				return branch.path
		return []