__author__ = 'bsaunders'

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

from TicTacToe import *
from Move import Move
import random
from AI import Player
from AI import Minimax

def swapPlayer(current_player, player_1, player_2):
	if (current_player is player_1):
		return player_2
	else:
		return player_1


def gameMain(counter):
	global number_of_game_losses, number_of_game_wons, number_of_ties, total_number_of_games
	counter += 1
	ttt = TicTacToe()
	player_1 = Player("X")
	player_2 = Minimax(ttt, "O")
	current_player = player_1

	print("-----------Starting game------------")

	# Game Loop
	while not ttt.finished:
		# Draw the game board.
		ttt.printGame()

		print("Current player is: ", current_player.playerName)

		board_position = current_player.move(ttt)
		position = int(board_position)
		
		ttt.placeMove(position, current_player.playerName)

		ttt.testForWin(current_player.playerName)
		ttt.testBoardFull()

		current_player = swapPlayer(current_player, player_1, player_2)

	# Present Results, increment the game statistics
	if ttt.winner == "X":
		print("You won!")
		ttt.printGame()
		number_of_game_losses += 1

	elif ttt.winner == "O":
		print("You Lost!")
		ttt.printGame()
		number_of_game_wons += 1

	else:
		print("It's a tie!")
		ttt.printGame()
		number_of_ties += 1

	total_number_of_games += 1

	print("Wins: ", number_of_game_losses)
	print("Loses: ", number_of_game_wons)
	print("Ties: ", number_of_ties)
	print("Total Games: ", total_number_of_games)

	print("------------Ending game-------------\n")

	# Recursively restart the game
	gameMain(counter)

# Game Statistics
number_of_game_losses = 0
number_of_game_wons = 0
number_of_ties = 0
total_number_of_games = 0
counter = 0

gameMain(counter)




