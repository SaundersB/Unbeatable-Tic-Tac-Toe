from AI import *
from TicTacToe import TicTacToe

#!/bin/py
# Brandon Saunders
# 4/1/2016
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

# Game Statistics
number_of_game_losses = 0
number_of_game_wins = 0
number_of_ties = 0
total_number_of_games = 0
counter = 0


def switchPlayer(player, p1, p2):
    if (player is p1):
        return p2
    else:
        return p1

def printGameStatistics():
    global number_of_game_losses, number_of_game_wins, number_of_ties, total_number_of_games
    print("------Game Statistics-------")
    print("Wins: ", number_of_game_wins)
    print("Loses: ", number_of_game_losses)
    print("Ties: ", number_of_ties)
    print("Total Games: ", total_number_of_games)
    print("----------------------------")

def main():
    global number_of_game_losses, number_of_game_wins, number_of_ties, total_number_of_games
    print("-----------Game Begin--------------")
    total_number_of_games += 1
    p1 = Player('X')
    p2 = MiniMax('O')
    ttt = TicTacToe(p1, p2)
    player = p1
    while (True):
        ttt.printGame()
        print("Your move, " + player.player)
        move = player.move(ttt)
        print("Playing move: ", move)
        ttt.placeMove(move, player.player)
        if ttt.testForWin(player.player):
            ttt.printGame()
            print(player.player + " won!")
            if(player.player == "X"):
                number_of_game_wins += 1
            elif(player.player == "O"):
                number_of_game_losses += 1
            printGameStatistics()
            print("-----------Game End--------------")
            print("\n")
            main()
        elif ttt.testBoardFull():
            ttt.printGame()
            number_of_ties += 1
            print('The game is a tie!')
            printGameStatistics()
            print("-----------Game End--------------")
            print("\n")
            main()
        else:
            player = switchPlayer(player, p1, p2)


if __name__ == "__main__":
    main()
