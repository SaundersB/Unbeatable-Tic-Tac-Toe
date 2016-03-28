#!/bin/py
# Brandon Saunders
# 3/9/2016
# Written in Python. This game will be an 'unbeatable' version of the classic Tic-Tac-Toe.
# The human player will face off an 'unbeatable' computer player.
# This is an adversarial, zero sum game. 
# Requirements:
# - allow for a human player
# - play against a computer player
# - have some user interface (text is fine)
# - never lose and win whenever possible
# Human player will play as "X"
# Computer will play as "O"
# Please run this program with Python v2.7. This program does not fully support Python v3. 


import random
import copy

class Game:
	# Initialize with the tic tac toe game board. I use a map for human-readability ease. 
	# ttt stands for Tic-Tac-Toe. Each row, column, and diagonal will be set for easy
	# case testing later.
	def __init__(self):
		self.ttt = {'a': 0, 'b': 0, 'c':0, 'd': 0,'e': 0, 'f':0,'g': 0, 'h': 0, 'i': 0}
		self.row1 = ['a','b','c']
		self.row2 = ['d','e','f']
		self.row3 = ['g','h','i']
		self.col1 = ['a','d','g']
		self.col2 = ['b','e','h']
		self.col3 = ['c','f','i']
		self.dia1 = ['a','e','i']
		self.dia2 = ['c','e','g']
		self.winning_configurations = (self.row1, self.row2, self.row3, self.col1, self.col2, self.col3, self.dia1, self.dia2)

	def __str__(self):
		return " %s %s %s" % (self.rcd_values(self.row1),
							  self.rcd_values(self.row2),
							  self.rcd_values(self.row3))

	# Allows us to reset the game board.
	def reset(self):
		self.ttt = {'a': 0, 'b': 0, 'c':0, 'd': 0,'e': 0, 'f':0,
			   'g': 0, 'h': 0, 'i': 0}

	# Row, column, or diagonal values.
	def rcd_values(self,rcd):
		return [self.ttt[x] for x in rcd]

	# Present the game board to the human player.
	def present(self):
		self.present_row(self.row1)
		self.present_row(self.row2)
		self.present_row(self.row3)
		print("\n")

	# Present only the game rows.
	def present_row(self,row):
		for i in range(3):
			if self.ttt[row[i]] == 0:
				if i < 2:
					print(row[i]),
				else:
					print(row[i])
			else:
				if i < 2:
					print(self.ttt[row[i]]),
				else:
					print(self.ttt[row[i]])


	# Prompt the user for their move. Verify if move is legal.
	def placeX(self):
		self.present()
		while(True):
			pick = raw_input("Choose a place for X: \n")
			
			if self.ttt[pick] == 0:
				self.ttt[pick] = 'X'
				break
			else:
				print ("Can't play there. Choose again:")

	# Computer player goes through a series of checks and then decides the best move.
	# First we always test if we can win. If we cannot we block a possible human player
	# win. Next we play a random corner. After that if we can we play the middle.
	# And finally if none of these options are available we play a random available
	# move.
	def play_O(self):
		self.present()
		print("Playing an O\n")

		NextMoves = self.all_Moves("O")
		decision = []

		# Decision holds keys.
		for item in NextMoves:
			decision.append(item)

		# Checking if player "O" can currently win.
		counter = 0
		for i in self.ttt:
			board_copy = copy.deepcopy(self.ttt)
			if self.is_space_free(board_copy,i):
				self.placeMove(board_copy,i,"O")
				if self.is_winner(board_copy, "O"):
					print("PLaying winning move")
					return i
			counter += 1

		# Blocking a possible human, "X" win
		block = self.two_in_any("X")
		if block:
			print("Blocking human")
			return block			

		# Play a random corner if available.
		move = random.choice([0,2,6,8])
		key_move = self.returnKey(move)
		if move != None and self.is_space_free(self.ttt, key_move):
			print("Picking random corner")
			return key_move

		# Play the middle if it is free
		middle = self.returnKey(4)
		if self.is_space_free(self.ttt,middle):
			print("Playing the middle")
			return middle
				
		# else, take one free space on the sides
		#return self.choose_random_move(self.sides)
		pick = random.choice(NextMoves)
		if self.is_space_free(self.ttt,pick):
			print("Picking a random move")
			return pick
		else:
			self.play_O()
		



	# Return all moves that are the options for the player with symb.
	def next_moves(self, symb):
		moves = []
		for x in ['a','b','c','d','e','f','g','h','i']:
			if(self.ttt[x] == 0):
				# We can place symbol at position x. 
				# Create a game object and duplicate the current game board.
				n = Game() 

				for k in ['a','b','c','d','e','f','g','h','i']:
					n.ttt[k] = self.ttt[k]

				n.ttt[x] = symb
				moves.append(n)
		return moves

	# Returns all possible rows, columns, and diagonals.
	def poss_rcds(self, symb):
			return self.poss_row1(symb) +\
				   self.poss_row2(symb) +\
					self.poss_row3(symb) +\
					self.poss_col1(symb) +\
					self.poss_col2(symb) +\
					self.poss_col3(symb) +\
					self.poss_diag1(symb) +\
					self.poss_diag2(symb)
	
	# Returns 1 for each row, column, and diagonal if it is 
	# still possible for player with symb.
	# Else return 0
	def poss_row1(self, symb):
		r = self.rcd_values(self.row1)

		if (symb == "X" and "O" in r):
			return 0
		else:
			return 1
		if (symb == "O" and "X" in r):
			return 0
		else:
			return 1


	def poss_row2(self, symb):
		r = self.rcd_values(self.row2)

		if (symb == "X" and "O" in r):
			return 0
		else:
			return 1
		if (symb == "O" and "X" in r):
			return 0
		else:
			return 1

	def poss_row3(self, symb):
		r = self.rcd_values(self.row3)

		if (symb == "X" and "O" in r):
			return 0
		else:
			return 1
		if (symb == "O" and "X" in r):
			return 0
		else:
			return 1


	def poss_col1(self, symb):
		r = self.rcd_values(self.col1)

		if (symb == "X" and "O" in r):
			return 0
		else:
			return 1
		if (symb == "O" and "X" in r):
			return 0
		else:
			return 1


	def poss_col2(self, symb):
		r = self.rcd_values(self.col2)

		if (symb == "X" and "O" in r):
			return 0
		else:
			return 1
		if (symb == "O" and "X" in r):
			return 0
		else:
			return 1


	def poss_col3(self, symb):
		r = self.rcd_values(self.col3)

		if (symb == "X" and "O" in r):
			return 0
		else:
			return 1
		if (symb == "O" and "X" in r):
			return 0
		else:
			return 1



	def poss_diag1(self, symb):
		r = self.rcd_values(self.dia1)

		if (symb == "X" and "O" in r):
			return 0
		else:
			return 1
		if (symb == "O" and "X" in r):
			return 0
		else:
			return 1


	def poss_diag2(self, symb):
		r = self.rcd_values(self.dia2)

		if (symb == "X" and "O" in r):
			return 0
		else:
			return 1
		if (symb == "O" and "X" in r):
			return 0
		else:
			return 1

	# Obtain all moves on a game board. 
	def all_Moves(self, symb):
		moves = []
		for x in ['a','b','c','d','e','f','g','h','i']:
			moves.append(x)
		return moves

	# Obtain the key from an index in the map.
	def returnKey(self, index):
		counter = 0
		for x in ['a','b','c','d','e','f','g','h','i']:
			if(index == counter):
				return x
			counter += 1

	# Game board independent move function.
	def placeMove(self,board,index, symb):
		board[index] = symb

	# Checks the board to see if a given key is free on a given board.
	def is_space_free(self, board, key):
		if (board[key] is not None):
			return board[key] == 0
		return "Invalid key or board"
		
	# True if there is a full row of symbol 'symb'    
	def full_row(self,symb):
		rs = list(3*symb)
		return rs==self.rcd_values(self.row1) or\
			   rs==self.rcd_values(self.row2) or\
			   rs==self.rcd_values(self.row3)

	# True if there is a full column of symbol 'symb'
	def full_col(self,symb):
		rs = list(3*symb)
		return rs==self.rcd_values(self.col1) or\
			   rs==self.rcd_values(self.col2) or\
			   rs==self.rcd_values(self.col3)

	# True if there is a full diagonal of symbol 'symb'
	def full_diag(self,symb):
		rs = list(3*symb)
		return rs==self.rcd_values(self.dia1) or\
			   rs==self.rcd_values(self.dia2)

	# True if X wins
	def winX(self):
		return self.full_row('X') or\
			   self.full_col('X') or\
			   self.full_diag('X')

	# True if O wins
	def winO(self):
		return self.full_row('O') or\
			   self.full_col('O') or\
			   self.full_diag('O')

	# True if the board is full.
	def full(self):
		return not 0 in self.rcd_values(self.row1) and\
			   not 0 in self.rcd_values(self.row2) and\
			   not 0 in self.rcd_values(self.row3)

	# Game board independent test if the player has won.
	def is_winner(self, board, marker):	        
	        for combo in self.winning_configurations:
	            if (board[combo[0]] == board[combo[1]] == board[combo[2]] == marker):
	                return True
	        return False


	# Returns key of any row, column, diagonal with
	# two symbols where key needs to be blocked/set with symb.
	# Return False if no two symbols in any row, column, or diagonal.
	# This allows the computer to determine the best place to play for a win.
	def two_in_any(self,symb):
		r1 = self.two_in_row1(symb)
		r2 = self.two_in_row2(symb)
		r3 = self.two_in_row3(symb)
		c1 = self.two_in_col1(symb)
		c2 = self.two_in_col2(symb)
		c3 = self.two_in_col3(symb)
		d1 = self.two_in_dia1(symb)
		d2 = self.two_in_dia2(symb)
		all = [r1,r2,r3,c1,c2,c3,d1,d2]
		while False in all:
			all.remove(False)
		if all == []:
			return False
		return random.choice(all)
		
	# Finds row with two symbs. Return the key to block with opposite symbol.
	def two_in_row1(self, symb):
		vals = self.rcd_values(self.row1)
		if (vals.count(symb) == 2):
			for k in self.row1:
				if self.ttt[k] == 0:
					return k
			return False
		else:
			return False

	def two_in_row2(self, symb):
		vals = self.rcd_values(self.row2)
		if (vals.count(symb) == 2):
			for k in self.row2:
				if self.ttt[k] == 0:
					return k
			return False
		else:
			return False
		
	def two_in_row3(self, symb):
		vals = self.rcd_values(self.row3)
		if (vals.count(symb) == 2):
			for k in self.row3:
				if self.ttt[k] == 0:
					return k
			return False
		else:
			return False

	def two_in_col1(self, symb):
		vals = self.rcd_values(self.col1)
		if (vals.count(symb) == 2):
			for k in self.col1:
				if self.ttt[k] == 0:
					return k
			return False
		else:
			return False
				
	def two_in_col2(self, symb):
		vals = self.rcd_values(self.col2)
		if (vals.count(symb) == 2):
			for k in self.col2:
				if self.ttt[k] == 0:
					return k
			return False
		else:
			return False            

	def two_in_col3(self, symb):
		vals = self.rcd_values(self.col3)
		if (vals.count(symb) == 2):
			for k in self.col3:
				if self.ttt[k] == 0:
					return k
			return False
		else:
			return False
				
	def two_in_dia1(self, symb):
		vals = self.rcd_values(self.dia1)
		if (vals.count(symb) == 2):
			for k in self.dia1:
				if self.ttt[k] == 0:
					return k
			return False
		else:
			return False
				
	def two_in_dia2(self, symb):
		vals = self.rcd_values(self.dia2)
		if (vals.count(symb) == 2):
			for k in self.dia2:
				if self.ttt[k] == 0:
					return k
			return False
		else:
			return False

	# Main() game loop.
	def play(self):
		self.reset()
		print ("\n\n")
		print ("Starting a new game of Tic-Tac-Toe. Human player is X.\n")
		while True:
			self.placeX()

			# Test the game board state.
			if self.winX():
				self.present()
				print("X, you win!\n\n")
				break
			if self.full():
				self.present()
				print("It is a tie!\n\n")
				break
			
			computer_move = self.play_O()
			print(computer_move)
			self.ttt[computer_move] = 'O'

			if self.winO():
				self.present()
				print("O wins, you lose!\n\n")
				break
			if self.full():
				self.present()
				print("Its a tie!\n\n")
				break

		

newGame = Game()
newGame.play()


