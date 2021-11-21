from QueueItem import QueueItem

class SearchItem:
	def __init__(self, node, path):
		self._node = node;
		self._path = path;

	@property
	def node(self):
		return self._node

	@property
	def path(self):
		return self._path

class DepthFirst:
	def __init__(self, nodes):
		self._explorationQ = [SearchItem(nodes[0], [])]
		self._exploredQ = []
		self._nodes = nodes
		self._finalNode = nodes[-1]

	def name(self):
		return "Depth First"

	def execute(self):
		# This assumes that the final node is in the node list
		while True:
			node = self._explorationQ[-1].node
			path = self._explorationQ[-1].path

			if node.equals(self._finalNode):
				return path + [node]

			self._explorationQ = self._explorationQ[:-1]
			self._exploredQ.append(node)

			for neighbour in node.branches:
				if neighbour is not None and not self._exploredQ.__contains__(neighbour):
					self._explorationQ.append(SearchItem(neighbour, path + [node]))


