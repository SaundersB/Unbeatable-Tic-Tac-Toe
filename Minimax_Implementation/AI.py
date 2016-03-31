from Move import Move
from TicTacToe import *


def score(game):
    if game.winner == "O":
        return 1
    elif game.winner != "O":
        return -1
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


# http://www.pressibus.org/ataxx/autre/minimax/node2.html
def minimax_v2(ttt, depth, max_depth, the_score, the_move):
    start = Move(ttt, 0, ttt.p1, ttt.p2)

    if (depth == max_depth):
        chosen_score = evaluate(start)
    else:
        moves_list = successor(start)
        if (moves_list == None):
            chosen_score = evaluate(start)
        else:
            for i in moves_list:
                best_score = []
                new_board = copy.deepcopy(start)
                apply_move(new_board, moves_list[i])
                minimax_v2(new_board, depth+1, max_depth, the_score, the_move)
                if (better(the_score, best_score)):
                    best_score = the_score
                    best_move = the_move

            chosen_score = best_score;
            chosen_move = best_move;

    return chosen_score


# http://www3.ntu.edu.sg/home/ehchua/programming/java/javagame_tictactoe_ai.html
def minimax_v3(ttt, level, player):
    start = Move(ttt, 0, ttt.p1, ttt.p2)

    if (ttt.finished or level == 0):
        bestScore = evaluate(start)
        return [bestScore]

    children = successor(start)

    # player is computer, i.e., maximizing player
    if (player == "O"):
        # find max
        bestScore = []
        for child in children:
            score = minimax_v3(ttt, level - 1, "X")
            if (score > bestScore):
                bestScore = score
        return bestScore

    # player is opponent, i.e., minimizing player
    else:
        # find min
        bestScore = []
        for child in children:
            score = minimax_v3(ttt, level - 1, "O")
            if (score < bestScore):
                bestScore = score
    return bestScore

def minimax_v4(player):
    if ttt.finished:
        print("Score(ttt): ", score(ttt))
        return score(ttt)

    start = Move(ttt, 0, ttt.p1, ttt.p2)
    moves = successor(start)
    scores = []
    depth += 1

    for move in moves:
        possible_game = get_new_state(start, move, player)
        #possible_game.printGame(possible_game)
        value = minimax_v4(possible_game, depth, player)
        scores.append(value)
        moves.append(move)

    scores.sort()
    print("Possible moves are: ", moves)
    print("Possible scores are: ", scores)

    if player == start.ttt.p1:
        # Max
        print("Scores are: ", scores)
        #max_score_index = scores[0]
        #decision = moves[max_score_index]
        #return scores[max_score_index]

    else:
        scores.reverse()
        #min_score_index = scores[0]
        #decision = moves[min_score_index]
        #return scores[min_score_index]

def get_new_state(state, move, player):
    copy_state = copy.deepcopy(state)
    new_state = state.ttt.placeMove(copy_state.ttt, move.position, player)
    return new_state


































class FullMinimaxMachine():
    def __init__(self, name):
        # call constructor for parent class
        name = self.name

    def fullMinimax(self, board, player):
        """
        This function implements a minimax search that always goes to the very end
        of the search tree. Only useful for games that don't have big search trees.
        The function always returns a tuple: (<move>, <value>). <move> only matters
        for the top node in the search tree, when the function is sending back which
        move to make to the game.
        """
        # Yay, we won!
        if board.isWinner(self.name):
            # Return a positive number
            return (1, 1)
        # Darn, we lost!
        elif board.isWinner(self.opponent):
            # Return a negative number
            return (-1, -1)
        # if it's a draw,
        elif (board.isBoardFull()):
            # return the value 0
            return (0, 0)
        # get all open spaces
        possibleMoves = board.possibleNextMoves()
        # are we considering our move or our opponent's move
        if self.name == player:
            # if it's our move, we want to find the move with the highest number, so start with low numbers
            bestMove = -1
            bestScore = -1000
            # loop through all possible moves
            for m in possibleMoves:
                # make the move
                board.makeMove(player, m)
                # get the minimax vaue of the resulting state
                minimax = self.fullMinimax(board, self.opponent)
                # is this move better than any other moves we found?
                if bestScore < minimax[1]:
                    # save the move...
                    bestMove = m
                    # and its score
                    bestScore = minimax[1]
                # undo the move
                board.clearSquare(m)
        else:
        # if it's our opponent's move, we want to find a low number, so start with big numbers
            bestMove = -1
            bestScore = 1000
            # consider all possible moves
            for m in possibleMoves:
                # make the move
                board.makeMove(player, m)
                # get the minimax vaue of the resulting state
                minimax = self.fullMinimax(board, self.name)
                # is this better (for our opponent) than any other moves we found?
                if bestScore > minimax[1]:
                    # save the move...
                    bestMove = m
                    # and its score
                    bestScore = minimax[1]
                # undo the move
                board.clearSquare(m)
        # return the best move and best score we found for this state
        return (bestMove, bestScore)

    def move(self, board):
        return self.fullMinimax(board, self.name)[0]