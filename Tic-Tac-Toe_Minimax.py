import copy
import time

class Move:
	def __init__(self, ttt, position, p1, p2, quality = 0):
		self.ttt = ttt
		self.position = position										
		self.p1 = p1 											# The player performing the move
		self.p2 = p2 											# The opposing player
		self.quality = quality									

	def __lt__(self, other):
		return self.quality < other.quality

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
		if move.ttt.winner == move.p1:
			return 9
		elif move.ttt.winner == move.p2:
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


def minimax(ttt):
	if ttt.finished:
		return -1

	start = Move(ttt, 0, ttt.p1, ttt.p2)

	# Create a list of possible moves
	moves = successor(start)

	# Determine the mins of each move
	for m in moves:
		if (m.ttt.finished):
			# Return a winning position
			if m.ttt.winner == m.p1:
				return m.position

			m.quality = evaluate(m)
		else:    
			responses = successor(m)

			for r in responses:
				r.quality = evaluate(r)
				

			responses.sort()
			m.quality = responses[0].quality

	# Select the max of mins
	moves.sort()
	moves.reverse()
	print("Max of mins: ", moves[0].position)
	return moves[0].position

class TicTacToe:
	def __init__(self, board_pieces = []):
		self.p1 = "X" # Active Player
		self.p2 = "O" # Opposing Player

		self.finished = False
		self.winner = None
		self.board_pieces = ['a','b','c','d','e','f','g','h','i']

		self.board = [None for i in range(9)]

		self.threes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], \
					   [0, 3, 6], [1, 4, 7], [2, 5, 8], \
					   [0, 4, 8], [2, 4, 6]]


	def printGame(self, ttt):
		

			
		print("\n")
		# Print out either letters or numbers from 0-9 or a-i.
		#if(ttt.board[0] == 'X' or ttt.board[0] == 'O'):
		# Then when the piece is replaced with an "X" or "O" display that instead.

		print " %s %s %s " % (self.board_pieces[0], self.board_pieces[1], self.board_pieces[2])
		print " %s %s %s " % (self.board_pieces[3], self.board_pieces[4], self.board_pieces[5])
		print " %s %s %s " % (self.board_pieces[6], self.board_pieces[7], self.board_pieces[8])
		#print (ttt.board[0], ttt.board[1], ttt.board[2])
		#print (ttt.board[3], ttt.board[4], ttt.board[5])
		#print (ttt.board[6], ttt.board[7], ttt.board[8])
		print("\n")

        

	def inThree(self, player, three):
		count = 0
		for i in three:
			count += (self.board[i] == player)
		return count

	def move(self, position):
		# Check if move is possible
		if self.finished or self.board[position] != None:
			return

		self.board[position] = self.p1
		self.board_pieces[position] = self.p1

		# Check for a Win
		for three in self.threes:
			if self.inThree(self.p1, three) == 3:
				self.winner = self.p1

		# Check if the board is exhausted
		empty_count = 0
		for position in self.board:
			empty_count += (position == None)

		self.finished = (empty_count == 0 or self.winner != None)

		# Switch to the other player
		self.p1, self.p2 = self.p2, self.p1

	def getBoardIndex(self, position):
		index = 0
		counter = 0
		for location in ['a','b','c','d','e','f','g','h','i']:
			if position == location:
				index = counter
			counter += 1
		return index





def gameMain(counter):
	global number_of_game_losses, number_of_game_wons, number_of_ties, total_number_of_games
	counter += 1
	ttt = TicTacToe()
	# Game Loop
	while not ttt.finished:
		ttt.printGame(ttt)

		#board_position = raw_input("Where do you want to play? (a-i): ")
		board_position = minimax(ttt)
		#index = ttt.getBoardIndex(board_position)
		#print(index)
		ttt.move(board_position)

		# Computer move
		print("Computer is making its move...")
		time.sleep(1) # Simulate thinking

		board_position = minimax(ttt)
		ttt.move(board_position)

	# Present Results
	if ttt.winner == "X":
		print("You won!")
		ttt.printGame(ttt)
		number_of_game_losses += 1

	elif ttt.winner == "O":
		print("You Lost!")
		ttt.printGame(ttt)
		number_of_game_wons += 1

	else:
		print("It's a tie!")
		ttt.printGame(ttt)
		number_of_ties += 1

	total_number_of_games += 1

	print("Wins: ", number_of_game_losses)
	print("Loses: ", number_of_game_wons)
	print("Ties: ", number_of_ties)
	print("Total Games: ", total_number_of_games)

	
	gameMain(counter)



number_of_game_losses = 0
number_of_game_wons = 0
number_of_ties = 0
total_number_of_games = 0
counter = 0

gameMain(counter)