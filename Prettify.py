class Prettify:
	def __init__(self):
		pass

	def _isPath(self, data):
		return data > 0

	def prettyPrintImage(self, im):
		(height, width) = im.shape
		for y in range(height):
			for x in range(width):
				if self._isPath(im[y][x]):
					print("■", end='')
				else:
					print(" ", end='')
			print('')	

	def prettyPrintClean(self, data):
		for y in range(len(data)):
			for x in range(len(data[y])):
				if data[y][x]:
					print("■", end='')
				else:
					print(" ", end='')
			print('')	