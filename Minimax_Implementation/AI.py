
from Player import *

# Minimax class that inherits the Player class.
# Will go through all possible moves on the board for each player depending on
# whether they're the maximizing player or the minimizing player.
class MiniMax(Player):
    def __init__(self, player):
        Player.__init__(self, player)

    def minimax(self, ttt, player):
        if ttt.testForWin(self.player):
            return (1, 1)
        elif ttt.testForWin(self.opponent):
            return (-1, -1)
        elif (ttt.testBoardFull()):
            return (0, 0)
        possibleMoves = ttt.possibleNextMoves()
        if self.player == player:
            bestMove = -1
            bestScore = -1000
            for m in possibleMoves:
                ttt.placeMove(m, player)
                minimax = self.minimax(ttt, self.opponent)
                if bestScore < minimax[1]:
                    bestMove = m
                    bestScore = minimax[1]
                ttt.removeMove(m)
        else:
            bestMove = -1
            bestScore = 1000
            for m in possibleMoves:
                ttt.placeMove(m, player)
                minimax = self.minimax(ttt, self.player)
                if bestScore > minimax[1]:
                    bestMove = m
                    bestScore = minimax[1]
                ttt.removeMove(m)
        return (bestMove, bestScore)

    def move(self, ttt):
        return self.minimax(ttt, self.player)[0]