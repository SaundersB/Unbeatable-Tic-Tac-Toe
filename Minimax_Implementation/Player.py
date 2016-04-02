import random

class Player():
    def __init__(self, playerName):
        self.player = playerName
        if playerName == 'X':
            self.opponent = 'O'
        else:
            self.opponent = 'X'

    def move(self, ttt):
        # Enable to input manual user moves.
        move = -1
        key = ""
        key = raw_input("Choose a square: ")
        move = ttt.getBoardIndex(key)
        print("You selected move: ", move)
        return int(move)
        # Uncomment to enable randomized moves for player "X"
        #return self.enable_Random_Move(True, ttt)

    # Convert the key to an int index.
    def getBoardIndex(self, position):
        index = 0
        counter = 0
        for location in ['a','b','c','d','e','f','g','h','i']:
            if position == location:
                index = counter
            counter += 1
        return index

    def enable_Random_Move(self, enable, ttt):
        if(enable):
            possibleMoves = ttt.possibleNextMoves()
            board_position = random.choice(possibleMoves)
        return board_position


