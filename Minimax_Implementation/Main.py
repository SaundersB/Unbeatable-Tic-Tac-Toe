__author__ = 'bsaunders'

from TicTacToe import *
from AI import *
from Move import Move


# Either obtain the human players move or play the perfect minimax vs. minimax player.
def enable_AI_vs_AI(enable, ttt):
	if(enable):
		board_position = minimax(ttt)
	else:
		letter = raw_input("Where do you want to play? (a-i): ")
		board_position = ttt.getBoardIndex(letter)
	return board_position


def gameMain(counter):
	global number_of_game_losses, number_of_game_wons, number_of_ties, total_number_of_games
	counter += 1
	ttt = TicTacToe()

	# Game Loop
	while not ttt.finished:
		ttt.printGame(ttt)

		# Change False to True to have the game go on automated.
		board_position = enable_AI_vs_AI(False, ttt)
		print("X is moving to position: ", board_position)

		# Place player X's move on the game board.
		ttt.move(board_position)

		ttt.switchPlayers()

		# Computer move "O"
		print("Computer is making its move...")
		time.sleep(1) # Simulate thinking

		# Calculate the minimax of both players and select the best move for player O.
		board_position = partialMinimax(ttt, "O", 0)[0]
		print("O is moving to position: ", board_position)
		ttt.move(board_position)

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




