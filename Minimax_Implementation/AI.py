__author__ = 'bsaunders'

from Move import Move
from TicTacToe import *
import TicTacToe
import random

DEPTHLIMIT = 2


# Original Minimax Algorithm
def original_minimax(ttt):
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
            # Will check all possible moves    
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



class Minimax():
    def __init__(self, ttt, playerName):
        self.ttt = ttt
        self.playerName = playerName

        if self.playerName == 'X':
            self.opponent = 'O'
        else:
            self.opponent = 'X'


    def inARow(self, ttt, le):
        '''
        This function counts the number of two-in-a-row combinations the player has,
        either in a row, column or diagonally
        '''
        # create a tuple for each pair of squares that can be in a row
        combos = [(0, 1), (1, 2), (0, 2),
                  (3, 4), (4, 5), (3, 5),
                  (6, 7), (7, 8), (6, 8),
                  (0, 3), (3, 6), (0, 6),
                  (1, 4), (4, 7), (1, 7),
                  (2, 5), (5, 8), (2, 8),
                  (0, 4), (4, 8), (0, 8),
                  (2, 4), (4, 6), (2, 6)]
        # we start with no squares in a row
        count = 0
        # for each of the pairs above...
        for c in combos:
            # if we have claimed both squares...
            if (ttt[c[0]] == le and ttt[c[1]] == le):
                # increase our count
                count += 1
        # return the total number of two-in-a-row pairs we have
        return count

    def cattyCorner(self, ttt, le):
        '''
        This function returns the number of "catty-corner" pairs the player has
        '''
        # create a tuple for each pair of catty-corner squares
        combos = [(1, 3), (1, 5), (7, 3), (7, 5)]
        # we start with no catty-corner squares
        count = 0
        # for each of the pairs above...
        for c in combos:
            # if we have claimed both squares...
            if (ttt[c[0]] == le and ttt[c[1]] == le):
                # increase our count
                count += 1
        # return the total number of catty-corner squares
        return count

    def haveCenter(self, ttt, le):
        # if we have the center square...
        if (ttt[4] == le):
            # return 1
            return 1
        # otherwise, we don't have the center square...
        else:
            # so return 0
            return 0

    def evaluationFunction(self, ttt):
        """
        This function is used by minimax to evaluate a non-terminal state.
        """
        # start with a value of zero
        score = 0
        # add number of two-in-a-row pairs we have
        score += 3 * self.inARow(ttt, self.playerName)
        # subtract number of two-in-a-row pairs opponent has
        score -= 3 * self.inARow(ttt, self.opponent)
        # add number of catty-corner pairs we have
        score += 2 * self.cattyCorner(ttt, self.playerName)
        # subtract number of catty-corner pairs opponent has
        score -= 2 * self.cattyCorner(ttt, self.opponent)
        # add one if we have the center square
        score += self.haveCenter(ttt, self.playerName)
        # subtract one if opponent has center square
        score -= self.haveCenter(ttt, self.opponent)
        # return the evaluation score
        return score



    def move(self, ttt):
         # Computer move "O"
        print("Computer is making its move...")
        print("Please be patient...")
        #time.sleep(1) # Simulate thinking

        #Alpha Beta Pruning
        #board_position = self.alphaBeta(ttt, self.playerName, 0, 2, -2)[0]
        #score = self.alphaBeta(ttt, self.playerName, 0, 2, -2)[1]

        # Partial Minimax
        # Calculate the minimax of both players and select the best move for player O.
        board_position = self.partialMinimax(ttt, self.playerName, 0)[0]
        score = self.partialMinimax(ttt, self.playerName, 0)[1]

        # Full Minimax
        # print("Player O using the full minimax algorithm...")
        #board_position = self.fullMinimax(ttt, self.playerName)[0]
        #score = self.fullMinimax(ttt, self.playerName)[1]

        if(isinstance(board_position, int)):
            print("(int) Move is: ", str(board_position))
            return board_position
        else: 
            print("(obj) Move is: ", str(board_position.position))
            return board_position.position




    def partialMinimax(self, ttt, player, depth):
        new_ttt = copy.deepcopy(ttt)
        start = Move(new_ttt, 0, new_ttt.p1, new_ttt.p2)

        # check to see if we are at a terminal state - someone won, the ttt is full or we hit our search limit
        terminalTuple = self.locatedAtTerminalState(new_ttt, depth)
        # if we are at a terminal state
        if terminalTuple[0] == True:
            # return the value of this state
            return (0, terminalTuple[1])
        # get all open spaces
        possibleMoves = successor(start)
        # are we considering our move or our opponent's move
        if self.playerName == player:
            # if it's our move, we want to find the move with the highest number, so start with low numbers
            bestMove = -1
            bestScore = -1000
            # loop through all possible moves
            for m in possibleMoves:
                # make the move
                new_ttt.placeMove(m.position, player)
                # get the minimax vaue of the resulting state
                minimax = self.partialMinimax(new_ttt, self.opponent, depth+1)
                # is this move better than any other moves we found?
                if bestScore < minimax[1]:
                    # save the move...
                    bestMove = m
                    # and its score
                    bestScore = minimax[1]
                # undo the move
                new_ttt.removeMove(m.position)
        else:
        # if it's our opponent's move, we want to find a low number, so start with big numbers
            bestMove = -1
            bestScore = 1000
            # consider all possible moves
            for m in possibleMoves:
                # make the move
                new_ttt.placeMove(m.position, player)
                # get the minimax vaue of the resulting state
                minimax = self.partialMinimax(new_ttt, self.playerName, depth+1)
                # is this better (for our opponent) than any other moves we found?
                if bestScore > minimax[1]:
                    # save the move...
                    bestMove = m
                    # and its score
                    bestScore = minimax[1]
                # undo the move
                new_ttt.removeMove(m.position)
        # return the best move and best score we found for this state
        return (bestMove, bestScore)



    def locatedAtTerminalState(self, ttt, depth):
        global DEPTH_LIMIT
        # Yay, we won!
        if ttt.testForWin(self.playerName):
            # Return a positive number
            return (True, 100)
        # Darn, we lost!
        elif ttt.testForWin(self.opponent):
            # Return a negative number
            return (True, -100)
        # if it's a draw,
        elif (ttt.testBoardFull()):
            # return the value 0
            return (True, 0)
        # if we've hit our depth limit
        elif (depth >= DEPTHLIMIT):
            # use the evaluation function to return a value for this state
            return (True, self.evaluationFunction(ttt.board))
        return (False, 0)


    def fullMinimax(self, ttt, player):
        new_ttt = copy.deepcopy(ttt)
        start = Move(new_ttt, 0, self.playerName, self.opponent)

        if new_ttt.testForWin(self.playerName):
            return (1,1)

        elif new_ttt.testForWin(self.opponent):
            return (-1,-1)
        
        elif new_ttt.testBoardFull():
            return (0,0)

        # Create a list of possible moves
        moves = successor(start)
        bestMove = -1
        bestScore = -1000

        if self.playerName == player:
            for m in moves:
                #new_ttt.printGame(new_ttt)
                new_ttt.placeMove(m.position, player)
                minimax = self.fullMinimax(new_ttt, self.opponent)
                #new_ttt.printGame(new_ttt)

                if bestScore < minimax[1]:
                    bestMove = m 
                    bestScore = minimax[1] 

                new_ttt.removeMove(new_ttt, m.position)
        else:
            for m in moves:
                #new_ttt.printGame(new_ttt)
                new_ttt.placeMove(m.position, player)
                minimax = self.fullMinimax(new_ttt, self.playerName)
                #new_ttt.printGame(new_ttt)

                if bestScore > minimax[1]:
                    bestMove = m 
                    bestScore = minimax[1]

                new_ttt.removeMove(new_ttt, m.position)

        #print("Best Score is: ", bestScore)

        return (bestMove, bestScore)


    def alphaBeta(self, ttt, player, depth, alpha, beta):
        new_ttt = copy.deepcopy(ttt)
        # check to see if we are at a terminal state - someone won, the board is full or we hit our search limit
        terminalTuple = self.locatedAtTerminalState(new_ttt, depth)
        # if we are at a terminal state
        if terminalTuple[0] == True:
            # return the value of this state
            return (0, terminalTuple[1])
        # get all open spaces
        moves = Move(new_ttt, 0, self.playerName, self.opponent)
        possibleMoves = successor(moves)
        # are we considering our move or our opponent's move
        if self.playerName == player:
            # if it's our move (MAX), we want to find the move with the highest number, so start with low numbers
            bestMove = -1
            bestScore = beta
            # loop through all possible moves
            for m in possibleMoves:
                # make the move
                #print("Before move-----")
                #new_ttt.printGame()
                new_ttt.placeMove(m.position, player)

                #print("After move ---------")
                #new_ttt.printGame()
                # get the minimax vaue of the resulting state
                minimax = self.alphaBeta(new_ttt, self.opponent, depth+1, alpha, beta)
                # is this move better than any other moves we found?
                if bestScore < minimax[1]:
                    # save the move...
                    bestMove = m
                    # and its score
                    bestScore = minimax[1]
                # undo the move
                new_ttt.removeMove(m.position)
                # alpha-beta pruning: compare the returned value with of the previous path with the
                # beta value...
                if bestScore > alpha:
                    # If the value is greater than alpha abort the search for the current node;
                    return (bestMove, bestScore)
        else:
        # if it's our opponent's move (MIN), we want to find a low number, so start with big numbers
            bestMove = -1
            bestScore = alpha
            # consider all possible moves
            for m in possibleMoves:
                # make the move
                new_ttt.placeMove(m.position, player)
                # get the minimax vaue of the resulting state
                minimax = self.alphaBeta(new_ttt, self.playerName, depth+1, alpha, beta)
                # is this better (for our opponent) than any other moves we found?
                if bestScore > minimax[1]:
                    # save the move...
                    bestMove = m
                    # and its score
                    bestScore = minimax[1]
                # undo the move
                new_ttt.removeMove(m.position)
                # compare the returned value with of the previous path with the alpha value...
                if bestScore < beta:
                    # If the value is less than beta abort the search for the current node
                    return (bestMove, bestScore)
        # return the best move and best score we found for this state

        return (bestMove, bestScore)






class Player():
    def __init__(self, playerName):
        # name of this player - either X or O
        self.playerName = playerName
        # name of player's opponent
        if playerName == 'X':
            self.opponent = 'O'
        else:
            self.opponent = 'X'

    def move(self, ttt):        
        '''
        # Enable to allow user input.
        letter = raw_input("Where do you want to play? (a-i): ")
        board_position = ttt.getBoardIndex(letter)
        '''
        print("Player X is taking their turn...")
        board_position = enable_Random_Move(True, ttt)
        print("X is moving to position: ", board_position.position)            
       
        return board_position.position

# Either obtain the human players move or play the perfect minimax vs. minimax player.
def enable_AI_vs_AI(enable, ttt):
    if(enable):
        board_position = original_minimax(ttt)
    return int(board_position)

def enable_Random_Move(enable, ttt):
    if(enable):
        moves = Move(ttt, 0, ttt.p1, ttt.p2)
        possible_moves = successor(moves)
        board_position = random.choice(possible_moves)
    return board_position







# Heurisitic minimax. Searches for the best of all possible moves each turn.
def minimax_v2(ttt):
    if ttt.finished:
        return -1

    start = Move(ttt, 0, ttt.p1, ttt.p2)

    # Create a list of possible moves
    moves = successor(start)

    # Determine the mins of each move
    for m in moves:
        print("Available move: ", m.position)
        if (m.ttt.finished):
            # Return a winning position
            if m.ttt.winner == m.p1:
                return m.position

            m.quality = evaluate(m)
        else:
            # Will check all possible moves    
            responses = successor(m)

            for r in responses:
                r.quality = evaluate(r)
                
            responses.sort()
            print("Responses: ", responses)
            m.quality = responses[0].quality


    # Select the max of mins
    moves.sort()
    moves.reverse()
    #print("Max of mins: ", moves[0].position)
    return moves[0].position







def score(game, depth):
    print("Score being called: ")
    if game.testForWin("O"):
        return 10 - depth
    elif game.testForWin("X"):
        return depth - 10
    else:
        return 0
