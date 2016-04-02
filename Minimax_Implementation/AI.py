
from Player import *


class MiniMax(Player):
    def __init__(self, name):
        # Computer is a player as well.
        Player.__init__(self, name)

    def minimax(self, ttt, player):
        if ttt.testForWin(self.name):
            return (1, 1)
        elif ttt.testForWin(self.opponent):
            return (-1, -1)
        elif (ttt.testBoardFull()):
            return (0, 0)
        possibleMoves = ttt.possibleNextMoves()
        if self.name == player:
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
                minimax = self.minimax(ttt, self.name)
                if bestScore > minimax[1]:
                    bestMove = m
                    bestScore = minimax[1]
                ttt.removeMove(m)
        return (bestMove, bestScore)

    def move(self, ttt):
        return self.minimax(ttt, self.name)[0]