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
		

	# Computer makes move and will grab or block triples; 
	def play_O(self):
		self.present()
		print("Playing an O\n")
		ko = self.two_in_any('O')
		if ko:
			self.ttt[ko] = 'O'  # to win
		else:
			kx = self.two_in_any('X')

			if kx:
				self.ttt[kx] = 'O' # to block
			else:
				rest=[]
				for k in self.ttt.keys():
					if self.ttt[k] == 0:
						rest.append(k)
				pick = random.choice(rest)
				self.ttt[pick] = 'O'

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


	# Returns key of any row, column, diagonal with
	# two symbols where key needs to be blocked/set with O
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
			
			self.play_O()
			if self.winO():
				self.present()
				print("O wins, you loose!\n\n")
				break
			if self.full():
				self.present()
				print("Its a tie!\n\n")
				break

		

newGame = Game()
newGame.play()


