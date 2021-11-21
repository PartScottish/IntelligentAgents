from PriorityQueue import PriorityQueue

class AStar:
	def __init__(self, nodes):
		self._queue = PriorityQueue(nodes)
		self._queue.setAStarFactor()

	def name(self):
		return "A*"

	def execute(self):
		current = self._queue.getNext()
		current.setLength(0)

		while (not self._queue.isFinished(current)):
			# Update the neighbours
			for i in range(4):
				if current.node().branches[i] != None:
					aStarFactor = self._queue.findNode(current.node().branches[i]).getAStarFactor()
					length = current.length() + current.node().distanceToNeighbour(i) + aStarFactor
					self.queueItemPathLength(current.node().branches[i], current, length)

			# Go again for the next node
			current.setVisited()
			current = self._queue.getNext()

		return current.path() + [current.node()]


	def queueItemPathLength(self, targetNode, currentQI, length):
		#given queue item list find queue item that contains target node
		targetQI = self._queue.findNode(targetNode)
		#given target queue item, we want to set path = the current queue item path + current node
		targetQI.setPathIfShorter(currentQI.path(), currentQI.node(), length)

