__author__ = 'bsaunders'

from Move import Move
from TicTacToe import *

DEPTHLIMIT = 2


def score(game, depth):
    print("Score being called: ")
    if game.testForWin("O"):
        return 10 - depth
    elif game.testForWin("X"):
        return depth - 10
    else:
        return 0

# http://www.progtools.org/games/tutorials/ai_contest/minmax_contest.pdf
def minimax_recursive(ttt):
    # Make a copy of the game board for recursive manipulation.
    new_ttt = TicTacToe()
    new_ttt = copy.deepcopy(ttt)

    return max(new_ttt)

def min(new_ttt, player):
    best_move = []
    moves = getSuccessor(new_ttt)
    for i in moves:
        move = max(new_ttt.applyMove(new_ttt, i))
        if (Value(move) > Value(best_move)):
            best_move = move;
    return best_move;

def max(new_ttt):
    new_ttt = TicTacToe()
    new_ttt = copy.deepcopy(ttt)

    if new_ttt.finished:
        return score(new_ttt)

    #if (GameEnded(ttt)):
    #   return EvalGameState(ttt);
    
    else:
        best_move = []
        #moves = GenerateMoves(ttt)
        moves = successor(new_ttt)
        for i in moves:
            move = min(applyMove(new_ttt))
            if (Value(move) > Value(best_move)):
                best_move = move
        
        return best_move;
    




def minimax(ttt):
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


def fullMinimax(ttt, player):
    new_ttt = copy.deepcopy(ttt)
    start = Move(new_ttt, 0, new_ttt.p1, new_ttt.p2)

    if new_ttt.testForWin(new_ttt.p1):
        return (1,1)

    elif new_ttt.testForWin(new_ttt.p2):
        return (-1,-1)
    
    elif new_ttt.testBoardFull(new_ttt):
        return (0,0)

    # Create a list of possible moves
    moves = successor(start)
    bestMove = -1
    bestScore = -1000

    if player == new_ttt.p1:
       
        for m in moves:
            new_ttt.printGame(new_ttt)
            new_ttt.placeMove(new_ttt, m, player)
            minimax = fullMinimax(new_ttt, new_ttt.p2)
            new_ttt.printGame(new_ttt)


            if bestScore < minimax[1]:
                bestMove = m 
                bestScore = minimax[1] 

            new_ttt.removeMove(new_ttt, m)

    else:

        for m in moves:
            new_ttt.printGame(new_ttt)
            ttt.placeMove(new_ttt, m, player)
            minimax = fullMinimax(new_ttt, new_ttt.p1)
            new_ttt.printGame(new_ttt)

            if bestScore > minimax[1]:
                bestMove = m 
                bestScore = minimax[1]

            new_ttt.removeMove(new_ttt, m)
    print("Best Score is: ", bestScore)
    return (bestMove, bestScore)






def locatedAtTerminalState(ttt, depth):
        global DEPTH_LIMIT
        # Yay, we won!
        if ttt.testForWin(ttt.p1):
            # Return a positive number
            return (True, 100)
        # Darn, we lost!
        elif ttt.testForWin(ttt.p2):
            # Return a negative number
            return (True, -100)
        # if it's a draw,
        elif (ttt.testBoardFull(ttt)):
            # return the value 0
            return (True, 0)
        # if we've hit our depth limit
        elif (depth >= DEPTHLIMIT):
            # use the evaluation function to return a value for this state
            return (True, ttt.evaluateBoard())
        return (False, 0)


def partialMinimax(ttt, player, depth):
        new_ttt = copy.deepcopy(ttt)
        start = Move(new_ttt, 0, new_ttt.p1, new_ttt.p2)

        # check to see if we are at a terminal state - someone won, the ttt is full or we hit our search limit
        terminalTuple = locatedAtTerminalState(new_ttt, depth)
        # if we are at a terminal state
        if terminalTuple[0] == True:
            # return the value of this state
            return (0, terminalTuple[1])
        # get all open spaces
        possibleMoves = successor(start)
        # are we considering our move or our opponent's move
        if new_ttt.p1 == player:
            # if it's our move, we want to find the move with the highest number, so start with low numbers
            bestMove = -1
            bestScore = -1000
            # loop through all possible moves
            for m in possibleMoves:
                # make the move
                new_ttt.placeMove(new_ttt, m.position, player)
                # get the minimax vaue of the resulting state
                minimax = partialMinimax(new_ttt, new_ttt.p2, depth+1)
                # is this move better than any other moves we found?
                if bestScore < minimax[1]:
                    # save the move...
                    bestMove = m
                    # and its score
                    bestScore = minimax[1]
                # undo the move
                new_ttt.removeMove(new_ttt, m)
        else:
        # if it's our opponent's move, we want to find a low number, so start with big numbers
            bestMove = -1
            bestScore = 1000
            # consider all possible moves
            for m in possibleMoves:
                # make the move
                new_ttt.placeMove(new_ttt, m.position, player)
                # get the minimax vaue of the resulting state
                minimax = partialMinimax(new_ttt, new_ttt.p1, depth+1)
                # is this better (for our opponent) than any other moves we found?
                if bestScore > minimax[1]:
                    # save the move...
                    bestMove = m
                    # and its score
                    bestScore = minimax[1]
                # undo the move
                new_ttt.removeMove(new_ttt, m)
        # return the best move and best score we found for this state
        return (bestMove.position, bestScore)
