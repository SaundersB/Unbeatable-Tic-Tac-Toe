#!/bin/py
# Brandon Saunders
# 3/18/2016
# Written in Python. This game will be an 'unbeatable' version of the classic Tic-Tac-Toe.
# The human player will face off an 'unbeatable' computer player or alternatively the computer
# can play the computer.
# This is an adversarial, zero sum game. 
# Requirements:
# - allow for a human player
# - play against a computer player
# - have some user interface (text is fine)
# - never lose and win whenever possible
# Human player will play as "X"
# Computer will play as "O"
# Please run this program with Python v2.7. This program does not fully support Python v3. 

import copy
import time



class TicTacToe:
	def __init__(self, board_pieces = []):
		self.p1 = "X" # Active Player
		self.p2 = "O" # Opposing Player
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
		# Check if move is possible
		if self.finished or self.board[position] != None:
			return

		# Update the game piece for both the game board and the displayed board.
		self.board[position] = self.p1
		self.board_pieces[position] = self.p1

		self.testForWin()
		self.testBoardFull(self.board)

		self.switchPlayers()

	# Test if there is a win.
	def testForWin(self):
		# Check for a Win
		for three in self.threes:
			if self.inThree(self.p1, three) == 3:
				self.winner = self.p1


	# Convert the key to an int index.
	def getBoardIndex(self, position):
		index = 0
		counter = 0
		for location in ['a','b','c','d','e','f','g','h','i']:
			if position == location:
				index = counter
			counter += 1
		return index

	def testBoardFull(self, board):
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
	def evaluateBoard(self, ttt):
		number_or_threes = 0
		# Check for a Win
		for three in self.threes:
			if self.inThree(self.p1, three) == 3:
				number_or_threes += 1

		return number_or_threes



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
	#print("Max of mins: ", moves[0].position)
	return moves[0].position


# http://www.pressibus.org/ataxx/autre/minimax/node2.html
def minimax_v2(ttt, depth, max_depth, the_score, the_move):
	start = Move(ttt, 0, ttt.p1, ttt.p2)

	if (depth == max_depth):
		chosen_score = evaluate(start)
	else:
		moves_list = successor(start)
		if (moves_list == None):
			chosen_score = evaluate(start)
		else:
			for i in moves_list:
				best_score = []
				new_board = copy.deepcopy(start)
				apply_move(new_board, moves_list[i])
				minimax_v2(new_board, depth+1, max_depth, the_score, the_move)
				if (better(the_score, best_score)):
					best_score = the_score
					best_move = the_move

			chosen_score = best_score;
			chosen_move = best_move;

	return chosen_score


# http://www3.ntu.edu.sg/home/ehchua/programming/java/javagame_tictactoe_ai.html
def minimax_v3(ttt, level, player):
	start = Move(ttt, 0, ttt.p1, ttt.p2)

	if (ttt.finished or level == 0):
		bestScore = evaluate(start)
		return [bestScore]


	children = successor(start)

	# player is computer, i.e., maximizing player
	if (player == "O"):
		# find max
		bestScore = []
		for child in children:
			score = minimax_v3(ttt, level - 1, "X")
			if (score > bestScore):
				bestScore = score
		return bestScore

	# player is opponent, i.e., minimizing player
	else:
		# find min
		bestScore = []
		for child in children:
			score = minimax_v3(ttt, level - 1, "O")
			if (score < bestScore):
				bestScore = score
	print(bestScore)
	return bestScore


def evaluate(move):
	value = 0
	for three in move.ttt.threes:
		value += (move.ttt.inThree(move.p2, three) == 0) # Threes without an opponent
		value -= (move.ttt.inThree(move.p1, three) == 0) # Threes without the player
	return value


def getSuccessor(ttt):
	successors = []
	for i in range(9):
		if (ttt.board[i] == None):
			new_move = copy.deepcopy(move)
			new_move.position = i
			new_move.ttt.move(i)
			successors += [new_move]
	return successors


# http://www.progtools.org/games/tutorials/ai_contest/minmax_contest.pdf
def minimax_recursive(ttt):
	# Make a copy of the game board for recursive manipulation.
	new_ttt = TicTacToe()
	new_ttt = copy.deepcopy(ttt)

	return max(new_ttt)

def min(new_ttt, player):
	best_move = []
	moves = getSuccessor(new_ttt)
	for i in moves:
		move = max(new_ttt.applyMove(new_ttt, i))
		if (Value(move) > Value(best_move)):
			best_move = move;
	return best_move;

def max(new_ttt):
	new_ttt = TicTacToe()
	new_ttt = copy.deepcopy(ttt)

	if new_ttt.finished:
		return evaluate(new_ttt)

	#if (GameEnded(ttt)):
	#	return EvalGameState(ttt);
	
	else:
		best_move = []
		#moves = GenerateMoves(ttt)
		moves = successor(new_ttt)
		for i in moves:
			move = min(applyMove(new_ttt))
			if (Value(move) > Value(best_move)):
				best_move = move
		
		return best_move;
	


# Either obtain the human players move or play the perfect minimax vs. minimax player.
def enable_AI_vs_AI(enable, ttt):
	if(enable):
		board_position = minimax(ttt)
	else:
		letter = raw_input("Where do you want to play? (a-i): ")
		board_position = ttt.getBoardIndex(letter)
	return board_position


# Game main.
def gameMain(counter):
	global number_of_game_losses, number_of_game_wons, number_of_ties, total_number_of_games
	counter += 1
	ttt = TicTacToe()

	# Game Loop
	while not ttt.finished:
		ttt.printGame(ttt)

		# Change False to True to have the game go on automated.
		board_position = enable_AI_vs_AI(True, ttt)

		# Place player X's move on the game board.
		ttt.move(board_position)

		# Computer move "O"
		print("Computer is making its move...")
		time.sleep(1) # Simulate thinking

		# Calculate the minimax of both players and select the best move for player O.
		board_position = minimax_v3(ttt, 2, "O")
		#ttt.move(board_position)

	# Present Results, increment the game statistics
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

	# Recursively restart the game
	gameMain(counter)

# Game Statistics
number_of_game_losses = 0
number_of_game_wons = 0
number_of_ties = 0
total_number_of_games = 0
counter = 0

gameMain(counter)