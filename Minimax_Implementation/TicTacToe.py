
# TicTacToe game board class. Contains all game board specific methods. 
class TicTacToe(object):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.board_pieces = ['a','b','c','d','e','f','g','h','i'] # Allows us to mirror the game board with letters.
        self.board = [None for i in range(9)]

    # Places a move on the game board at a specified position.
    def placeMove(self, position, player):
        if self.board[position] != None:
            return
        if position in range(0, 9):
            self.board[position] = player
            self.board_pieces[position] = player

    # Function set the position to None. This function is needed when simulating game moves for the 
    # Minimax algorithm.
    def removeMove(self, position):
        if position in range(0, 9):
            self.board[position] = None
            self.board_pieces[position] = self.getKeyIndex(position)

    # Simple method to display the game board.
    def printGame(self):
        print("\n")
        print (" %s %s %s " % (self.board_pieces[0], self.board_pieces[1], self.board_pieces[2]))
        print (" %s %s %s " % (self.board_pieces[3], self.board_pieces[4], self.board_pieces[5]))
        print (" %s %s %s " % (self.board_pieces[6], self.board_pieces[7], self.board_pieces[8]))
        print("\n")

    # Will test all possible combinations for a win. (3 in a row).
    def testForWin(self, player):
        ttt = self.board
        return (
            (ttt[0] == player and ttt[1] == player and ttt[2] == player) or 
            (ttt[3] == player and ttt[4] == player and ttt[5] == player) or 
            (ttt[6] == player and ttt[7] == player and ttt[8] == player) or 
            (ttt[0] == player and ttt[3] == player and ttt[6] == player) or 
            (ttt[1] == player and ttt[4] == player and ttt[7] == player) or 
            (ttt[2] == player and ttt[5] == player and ttt[8] == player) or 
            (ttt[0] == player and ttt[4] == player and ttt[8] == player) or 
            (ttt[2] == player and ttt[4] == player and ttt[6] == player)) 

    # Checks if a particular move is available or not.
    def isSpaceFree(self, move):
        if move in range(0, 9):
            return self.board[move] == None

    # Checks if the game board is full or not.
    def testBoardFull(self):
        for i in range(0, 9):
            if self.isSpaceFree(i):
                return False
        return True

    # Returns all possible next moves.
    def possibleNextMoves(self):
        possibleMoves = []
        for i in range(0,9):
            if self.isSpaceFree(i):
                possibleMoves.append(i)
        return possibleMoves

    # Convert the key to an int index.
    def getBoardIndex(self, position):
        index = 0
        counter = 0
        for location in ['a','b','c','d','e','f','g','h','i']:
            if position == location:
                index = counter
            counter += 1
        return index

    # Convert the int index to a key.
    def getKeyIndex(self, index):
        counter = 0
        for location in ['a','b','c','d','e','f','g','h','i']:
            if index == counter:
                key = location
            counter += 1
        return key
