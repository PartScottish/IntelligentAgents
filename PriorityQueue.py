from QueueItem import QueueItem

from Maze import Node
#from Maze import Coord

class PriorityQueue:
	def __init__(self, nodes):
		self._queueItems = []
		for node in nodes:
			self._queueItems.append(QueueItem(node))
		self._start = self._queueItems[0]
		self._finish = self._queueItems[-1]

	def pos(self, pos: int):
		return self._queueItems[pos]

	def isFinished(self, node: QueueItem):
		return node == self._finish

	def getNext(self):
		# Remove all the nodes we've already visited
		filteredList = [x for x in self._queueItems if not x.isVisited()]
		# Order by the length of their path so we can take the shortest path next
		sortedList = sorted(filteredList, key=lambda x:x.length())
		return sortedList[0]

	def findNode(self, node: Node):
		# Filter out everything except the node we're looking for
		return [x for x in self._queueItems if x.hasCoords(node.xcoord, node.ycoord)][0]
		# Maybe add some error handling here?

	def setAStarFactor(self):
		for queueItem in self._queueItems:
			currentNode = queueItem.node()
			aStarFactor = abs(self._finish.node().xcoord + currentNode.xcoord) + abs(self._finish.node().ycoord + currentNode.ycoord)
			queueItem.setAStarFactor(aStarFactor)