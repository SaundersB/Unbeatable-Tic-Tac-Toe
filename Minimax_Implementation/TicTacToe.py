__author__ = 'bsaunders'


import copy
import time



class TicTacToe:
	def __init__(self, board_pieces = []):
		self.p1 = "X" # Active Player
		self.p2 = "O" # Opposing Player
		self.opponent = "O"
		self.finished = False
		self.winner = None
		self.board_pieces = ['a','b','c','d','e','f','g','h','i'] # Allows us to mirror the game board with letters.
		self.board = [None for i in range(9)]
		self.threes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], \
					   [0, 3, 6], [1, 4, 7], [2, 5, 8], \
					   [0, 4, 8], [2, 4, 6]]

	def printGame(self, ttt):
		print("\n")
		# Print out letters [a-i] for easy viewing and selection.
		print (" %s %s %s " % (self.board_pieces[0], self.board_pieces[1], self.board_pieces[2]))
		print (" %s %s %s " % (self.board_pieces[3], self.board_pieces[4], self.board_pieces[5]))
		print (" %s %s %s " % (self.board_pieces[6], self.board_pieces[7], self.board_pieces[8]))
		print("\n")
		
	# Test for three in a row.
	def inThree(self, player, three):
		count = 0
		for i in three:
			count += (self.board[i] == player)
		return count

	# Make a move in a particular position.
	def move(self, position):
		#print("Moving to position: ", position)
		# Check if move is possible
		if position in range(0, 9):
			if self.finished or self.board[position] != None:
				return

			# Update the game piece for both the game board and the displayed board.
			self.board[position] = self.p1
			self.board_pieces[position] = self.p1

		self.testForWin(self.p1)
		self.testBoardFull()

		#self.switchPlayers()


	def placeMove(self, position, player):
		if self.board[position] != None:
			return

		self.board[position] = player
		self.board_pieces[position] = player

		self.testForWin(player)
		self.testBoardFull()


	def removeMove(self, ttt, position):
		if ttt.board[position] == None:
			return

		ttt.board[position] = None
		ttt.board_pieces[position] = ttt.getBoardIndex(position)


	# Test if there is a win.
	def testForWin(self, player):
		# Check for a Win
		for three in self.threes:
			if self.inThree(player, three) == 3:
				self.winner = player
				return True
		return False


	# Convert the key to an int index.
	def getBoardIndex(self, position):
		index = 0
		counter = 0
		for location in ['a','b','c','d','e','f','g','h','i']:
			if position == location:
				index = counter
			counter += 1
		return index

	def testBoardFull(self):
		# Check if the board is exhausted
		empty_count = 0
		for position in self.board:
			empty_count += (position == None)

		self.finished = (empty_count == 0 or self.winner != None)

		return self.finished

	def switchPlayers(self):
		# Switch to the other player
		self.p1, self.p2 = self.p2, self.p1

	# Returns the number of ways a player can win.
	def evaluateBoard(self):
		number_or_threes = 0
		# Check for a Win
		for three in self.threes:
			if self.inThree(self.p1, three) == 3:
				number_or_threes += 1
		return number_or_threes

	def setOpponent(self):
		if self.p1 == 'X':
			self.opponent = 'O'
		else:
			self.opponent = 'X'


def successor(move):
	successors = []
	for i in range(9):
		if (move.ttt.board[i] == None):
			new_move = copy.deepcopy(move)
			new_move.position = i
			new_move.ttt.move(i)
			successors += [new_move]
	return successors

def evaluate(move):
	if move.ttt.finished:
		if move.ttt.winner == "X":
			return 9
		elif move.ttt.winner == "O":
			return -9

	value = 0
	for three in move.ttt.threes:
		value += (move.ttt.inThree(move.p2, three) == 0) # Threes without an opponent
		value -= (move.ttt.inThree(move.p1, three) == 0) # Threes without the player
	return value

def printGame(ttt):
	for y in range(3):
		for x in range(3):
			char = ttt.board[y * 3 + x]
			if (char == None):
				char = "."
			print(char, " ")
		print("\n", " ")




def getSuccessor(ttt):
	successors = []
	for i in range(9):
		if (ttt.board[i] == None):
			new_move = copy.deepcopy(move)
			new_move.position = i
			new_move.ttt.move(i)
			successors += [new_move]
	return successors



