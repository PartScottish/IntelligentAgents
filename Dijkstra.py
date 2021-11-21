from PriorityQueue import PriorityQueue

class Dijkstra:
	def __init__(self, nodes):
		self._queue = PriorityQueue(nodes)

		# for n in nodes:
			# print(f'Node: ({n.coord.x},{n.coord.y}) has neightbours:')
			# for b in n.branches:
			# 	print(f'     [', end='')
			# 	for p in b.path:
			# 		print(f'({p.x},{p.y}) ', end='')
			# 	print(']')

	def name(self):
		return "Dijkstra"

	def execute(self):
		current = self._queue.getNext()
		current.setLength(0)

		while (not self._queue.isFinished(current)):
			# Update the neighbours
			for i in range(4):
				if current.node().branches[i] != None:
					length = current.length() + current.node().distanceToNeighbour(i)
					self.queueItemPathLength(current.node().branches[i], current, length)
			# Go again for the next node
			current.setVisited()
			current = self._queue.getNext()

		return current.path()


	def queueItemPathLength(self, targetNode, currentQI, length):
		#given queue item list find queue item that contains target node
		targetQI = self._queue.findNode(targetNode)
		#given target queue item, we want to set path = the current queue item path + current node
		targetQI.setPathIfShorter(currentQI.path(), currentQI.node(), length)
		#set length of target queue item
