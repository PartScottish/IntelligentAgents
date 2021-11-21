from Maze import Node
import sys


class QueueItem:
    def __init__(self, node: Node):
        self._node = node
        self._length = sys.maxsize
        self._path = []
        self._isVisited = False
        self._aStarFactor = None

    def node(self):
        return self._node

    def length(self):
        return self._length

    def setLength(self, len: int):
        self._length = len

    def isVisited(self):
        return self._isVisited

    def path(self):
        return self._path

    def setPath(self, path, node):
        self._path = path[:]
        self._path.append(node)
        self._length = len(self._path)

    def setPathIfShorter(self, path, node, length):
        if self._path == [] or self._length > length:
            self._path = path[:]
            self._path.append(node)
            self._length = length

    def setVisited(self):
        self._isVisited = True

    def hasCoords(self, x, y):
        return self._node.xcoord == x and self._node.ycoord == y

    def setAStarFactor(self, distanceToEnd):
        # setter
        self._aStarFactor = distanceToEnd

    def getAStarFactor(self):
        # getter
        return self._aStarFactor
