import imageio

from Maze import Node

class ImageLoader:
	def __init__(self):
		pass

	def getImageData(self, imagePath: str):
		# Read data from file
		imageData = imageio.imread(imagePath)
		# Prettify().prettyPrintImage(imageData)
		# Build an array of nodes, this is the graph that we can execute the algorithms on
		graph = GraphBuilder().build(imageData)

		return graph

	def saveWithNodeData(self, imageSrc: str, imageDst: str, nodes: [Node]):
		imageData = imageio.imread(imageSrc)
		# colour the path grey cause colours are hard
		previousNode = nodes[0]
		for node in nodes:
			#compare coord x/y position. If x differs = horizontal line, if y differs = vertical line
			if node.xcoord == previousNode.xcoord:
				#vertical line
				for ycoord in range(min(node.ycoord, previousNode.ycoord), max(node.ycoord, previousNode.ycoord) + 1):
					imageData[ycoord][node.xcoord] = 100
			else:
				#horizontal line
				for xcoord in range(min(node.xcoord, previousNode.xcoord), max(node.xcoord, previousNode.xcoord) + 1):
					imageData[node.ycoord][xcoord] = 100

			previousNode = node
		imageio.imwrite(imageDst, imageData)

	def saveWithNodes(self, imageSrc: str, imageDst: str, nodes: [Node]):
		imageData = imageio.imread(imageSrc)
		for node in nodes:
			imageData[node.ycoord][node.xcoord] = 150
		imageio.imwrite(imageDst, imageData)

	def saveWithPath(self, imageSrc: str, imageDst: str, nodes: [Node]):
		imageData = imageio.imread(imageSrc)
		# colour the path grey cause colours are hard
		previousNode = nodes[0]
		for node in nodes:
			# for path in previousNode.pathTo(node):
			# 	imageData[path.y][path.x] = 100
			imageData[previousNode.ycoord][previousNode.xcoord] = 500
			previousNode = node
		imageio.imwrite(imageDst, imageData)


class GraphBuilder:
	def __init__(self):
		pass

	# Returns an array of Nodes
	def build(self, data: [[bool]]):
		graph = []
		topMost = [None] * len(data[0])
		for y in range(len(data)):
			leftMost = None
			for x in range(len(data[y])):
				# Only create node at position if it is a path
				if (data[y][x] > 0):
					isEast = (x < len(data[0]) - 1) and data[y][x + 1] > 0
					isWest = (x > 0) and data[y][x - 1] > 0
					isNorth = (y > 0) and data[y - 1][x] > 0
					isSouth = (y < len(data) - 1) and data[y + 1][x] > 0

					if self._isNode(isEast, isWest, isNorth, isSouth):
						node = Node(y, x)

						if isWest:
							node.addNeighbour(leftMost, 3)
							leftMost.addNeighbour(node, 1)
						leftMost = node if isEast else None

						if isNorth:
							node.addNeighbour(topMost[x], 0)
							topMost[x].addNeighbour(node, 2)
						topMost[x] = node if isSouth else None

						graph.append(node)

		for n in graph:
			for x in range(4):
				b = n.branches[x]


		return graph

	# Returns true if the point on the map is a node (deadend, T or +) and not a path (| or -)
	def _isNode(self, isEast:bool, isWest:bool, isNorth:bool, isSouth:bool):
		return not((isEast == isWest) and (isNorth == isSouth) and (isEast != isNorth))

	# Adds all neighbours to a node, does not return a value
	def _findNeighbours(self, y: int, x: int, data: [[bool]]):
		neighbours = []
		# West neighbour (x - 1)
		if ((x > 0) and data[y][x - 1]):
			neighbours.append(Coord(y, x-1))
		# North neighbour (y - 1)
		if ((y > 0) and data[y - 1][x]):
			neighbours.append(Coord(y-1, x))
		# South neighbour (y + 1)
		if ((y < len(data)-1) and data[y + 1][x]):
			neighbours.append(Coord(y+1, x))
		# East neighbour (x + 1)
		if ((x < len(data[0])-1) and data[y][x + 1]):
			neighbours.append(Coord(y, x+1))
		return neighbours


	def _isItemInList(self, list, coord):
		for i in list:
			if i.equals(coord):
				return True
		return False