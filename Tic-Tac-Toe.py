#!/bin/py
# Brandon Saunders
# 3/9/2016
# Written in Python. This game will be an 'unbeatable' version of the classic Tic-Tac-Toe.
# The human player will face off an 'unbeatable' computer player.
# This is an adversarial, zero sum game. 

GAME_BOARD = ['A','B','C',\
			  'D','E','F',\
			  'G','H','I']


class Game:
	def __init__(self):
		self.x = None

	def printGameboard(self):
		print(GAME_BOARD[0], GAME_BOARD[1], GAME_BOARD[2])
		print(GAME_BOARD[3], GAME_BOARD[4], GAME_BOARD[5])
		print(GAME_BOARD[6], GAME_BOARD[7], GAME_BOARD[8])

	def placeX(self,x):
		GAME_BOARD[x] = "X"

	def placeO(self,x):
		GAME_BOARD[x] = "O"



def driver():
	myGame = Game()

	myGame.placeO(0)
	myGame.placeX(1)

	myGame.printGameboard()



driver()
