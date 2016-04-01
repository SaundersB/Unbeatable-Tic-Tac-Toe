__author__ = 'bsaunders'

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

	# Game Loop
	while not ttt.finished:
		# Draw the game board.
		ttt.printGame(ttt)

		print("Current player is: ", current_player)

		board_position = current_player.move(ttt)
		
		ttt.placeMove(board_position, current_player.player)

		ttt.testForWin(current_player)
		ttt.testBoardFull()

		current_player = swapPlayer(current_player, player_1, player_2)

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




