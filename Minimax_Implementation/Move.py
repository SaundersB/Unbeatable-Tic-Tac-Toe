


class Move:
	def __init__(self, ttt, position, p1, p2, quality = 0):
		self.ttt = ttt
		self.position = position										
		self.p1 = p1 											# The player performing the move
		self.p2 = p2 											# The opposing player
		self.quality = quality									

	def __lt__(self, other):
		return self.quality < other.quality