class ImageOptions:
	def __init__(self):
		self._tinyMaze = "./Maps/tiny.png"
		self._smallMaze = "./Maps/small.png"
		self._normalMaze = "./Maps/normal.png"
		self._perfect2kMaze = "./Maps/perfect2k.png"
		self._perfect4kMaze = "./Maps/perfect4k.png"
		self._braid200Maze = "./Maps/braid200.png"
		self._braid2k = "./Maps/braid2k.png"
		self._combo400Maze = "./Maps/combo400.png"
		self._solution = "./Maps/solution.png"

	@property
	def tinyMaze(self):
		return self._tinyMaze

	@property
	def smallMaze(self):
		return self._smallMaze

	@property
	def normalMaze(self):
		return self._normalMaze

	@property
	def perfect2kMaze(self):
		return self._perfect2kMaze

	@property
	def perfect4kMaze(self):
		return self._perfect4kMaze

	@property
	def braid200Maze(self):
		return self._braid200Maze

	@property
	def braid2kMaze(self):
		return self._braid2k

	@property
	def combo400Maze(self):
		return self._combo400Maze

	@property
	def solution(self):
		return self._solution


