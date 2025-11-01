import random
import copy

class Game:
    """Class for the 2048 game

    Attributes:
        board: The game board
    """

    def __init__(self):
        """Constructor for a 2048 game object
        """
        self.board =  [[0,0,0,0],
                       [0,0,0,0],
                       [0,0,0,0],
                       [0,0,0,0]]

    def startGame(self):
        """Initiates the object for a new game with a board 
        that has one initial 2 or 4 on it  
        """
        board =  [[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        self.setBoard(board)
        self.addNumToBoard()

    def getBoard(self):
        """Get the game objects board  
        """
        return self.board

    def getHighestNum(self, board):
        """Get the highest number from a board

        Args: 
            board: The board from which the highest 
                   number is to be get  
        
        Returns: 
            The highest number of a board
        """

        highest = 0
        for i in range(4):
            for j in range(4):
                if board[i][j] > highest:
                    highest = board[i][j]
        return highest

    def getZeroPositions(self, board):
        """Get the free spaces from a board

        Args:
            board: The board to get the free spaces from

        Returns:
            Array of tuples which are the coordinates for the free spaces
        """
        positions = []
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    positions.append((i,j))
        return positions

    def setBoard(self, board):
        """Set the game objects board
        
        Args:
            board: The board to which the game objects board is to be set
        """
        self.board = board

    def setNumToBoard(self, number, coordinates, board):
        """Insert a number to a board into a position
        Function mostly for testing

        Args:
            number: The number which is to be inserted
            coordinates: The position on the board into which the number is to be inserted
            board: The board into which the number is to be inserted
        
        Returns:
            A new board with the number in given position
        """
        modifiedBoard = copy.deepcopy(board)
        modifiedBoard[coordinates[0]][coordinates[1]] = number
        return modifiedBoard

    def isBoardFull(self, board):
        """Check if the board is full and the game is lost
        as new moves cant be made

        Args: 
            board: The board which is to be checked

        Returns: 
            True if the board is full, False if the board is not full
        """
        for i in range(4):
            if 0 in board[i]:
                return False
        moves = ["up","down","left","right"]
        for move in moves:
            if self.isMovePossible(move, board):
                return False
        return True

    def isGameWon(self, board):
        """Check if the game is won by having a 2048 on the board

        Args: 
            board: The board which is be checked for victory

        Returns: 
            True if 2048 on board, False otherwise
        """
        for i in range(4):
            if 2048 in board[i]:
                return True
        return False

    def addNumToBoard(self):
        """Add a 2 or 4 into a random position on the game objects board. 
        2 is added with a propability of 9/10 and 4 with 1/10 propability
        """
        if random.randint(1, 10) < 2:
            num = 4
        else:
            num = 2 
        while True:
            coordinates = (random.randint(0,3),random.randint(0,3))
            if self.board[coordinates[0]][coordinates[1]] == 0:
                self.board[coordinates[0]][coordinates[1]] = num
                break


    def moveBoard(self, move):
        """Move the game objects board in some direction and change the 
        board state accordingly
        Possible moves are up, down, right left

        Args:
            move: The direction in which the board is to be moved 
        """
        prevBoard = copy.deepcopy(self.getBoard())
        if move == "up" and self.isMovePossible(move, prevBoard):
            self.setBoard(self.moveBoardUp(self.getBoard()))
            self.addNumToBoard()

        if move == "down" and self.isMovePossible(move, prevBoard):
            self.setBoard(self.moveBoardDown(self.getBoard()))
            self.addNumToBoard()

        if move == "right" and self.isMovePossible(move, prevBoard):
            self.setBoard(self.moveBoardRight(self.getBoard()))
            self.addNumToBoard()

        if move == "left" and self.isMovePossible(move, prevBoard):
            self.setBoard(self.moveBoardLeft(self.getBoard()))
            self.addNumToBoard()


    def isMovePossible(self, move, board):
        """Check if a move is possible to do on a board
        A move is possible if it can move or combine numbers on the board 
        The check is done by moving a copy of the board and checking whether 
        the board has changed

        Args:
            move: The move which is to be checked
            board: The board on which the move is to be checked

        Returns: 
            True if the move changes the board, False if the move does not
        """
        prevBoard = copy.deepcopy(board)
        if move == "up":
            movedBoard = self.moveBoardUp(prevBoard)
            if movedBoard == prevBoard:
                return False
            else: return True

        if move == "down":
            movedBoard = self.moveBoardDown(prevBoard)
            if movedBoard == prevBoard:
                return False
            else: return True

        if move == "right":
            movedBoard = self.moveBoardRight(prevBoard)
            if movedBoard == prevBoard:
                return False
            else: return True

        if move == "left":
            movedBoard = self.moveBoardLeft(prevBoard)
            if movedBoard == prevBoard:
                return False
            else: return True

        return False
            

    def moveBoardUp(self, board):
        """Moves a board up by moving and compining the numbers on it upward

        Args:
            board: The board to be moved

        Returns:
            A new move board where the numbers have been moved upward
        """
        returnBoard = copy.deepcopy(board)
        for i in range(len(returnBoard)):
            col = [returnBoard[0][i],returnBoard[1][i],returnBoard[2][i],returnBoard[3][i]]
            prevCombinedIdx = None

            j = 1
            while j < len(col):
                if col[j] != 0 and col[j] == col[j-1] and prevCombinedIdx != j-1:
                    col[j-1] = col[j]+col[j-1]
                    col[j] = 0
                    prevCombinedIdx = j-1

                elif col[j] != 0 and col[j-1] == 0:
                    col[j-1] = col[j]
                    col[j] = 0
                    if j-1 != 0:
                        j = j-1

                else:
                    j += 1
                    
            returnBoard[0][i],returnBoard[1][i],returnBoard[2][i],returnBoard[3][i] = col[0],col[1],col[2],col[3]

        return returnBoard

        
    def moveBoardDown(self, board):
        """Moves a board down by moving and compining the numbers on it downward

        Args:
            board: The board to be moved

        Returns:
            A new move board where the numbers have been moved downward
        """
        returnBoard = copy.deepcopy(board)
        for i in range(len(returnBoard)):
            col = [returnBoard[0][i],returnBoard[1][i],returnBoard[2][i],returnBoard[3][i]]
            prevCombinedIdx = None

            j = 2
            while j >= 0:
                if col[j] != 0 and col[j] == col[j+1] and prevCombinedIdx != j+1:
                    col[j+1] = col[j]+col[j+1]
                    col[j] = 0
                    prevCombinedIdx = j+1

                elif col[j] != 0 and col[j+1] == 0:
                    col[j+1] = col[j]
                    col[j] = 0
                    if j+1 != 3:
                        j = j+1

                else:
                    j -= 1
            returnBoard[0][i],returnBoard[1][i],returnBoard[2][i],returnBoard[3][i] = col[0],col[1],col[2],col[3]

        return returnBoard


    def moveBoardLeft(self, board):
        """Moves a board left by moving and compining the numbers on it leftward

        Args:
            board: The board to be moved

        Returns:
            A new move board where the numbers have been moved leftward            
        """
        returnBoard = copy.deepcopy(board)
        for i in range(len(returnBoard)):
            row = returnBoard[i]
            prevCombinedIdx = None

            j = 1
            while j < len(row):
                if row[j] != 0 and row[j] == row[j-1] and prevCombinedIdx != j-1:
                    row[j-1] = row[j]+row[j-1]
                    row[j] = 0
                    prevCombinedIdx = j-1

                elif row[j] != 0 and row[j-1] == 0:
                    row[j-1] = row[j]
                    row[j] = 0
                    if j-1 != 0:
                        j = j-1

                else:
                    j += 1

        return returnBoard
        
    def moveBoardRight(self, board):
        """Moves a board right by moving and compining the numbers on it rightward

        Args:
            board: The board to be moved

        Returns:
            A new move board where the numbers have been moved rightward
        """
        returnBoard = copy.deepcopy(board)
        for i in range(len(returnBoard)):
            row = returnBoard[i]
            prevCombinedIdx = None

            j = 2
            while j >= 0:
                if row[j] != 0 and row[j] == row[j+1] and prevCombinedIdx != j+1:
                    row[j+1] = row[j]+row[j+1]
                    row[j] = 0
                    prevCombinedIdx = j+1

                elif row[j] != 0 and row[j+1] == 0:
                    row[j+1] = row[j]
                    row[j] = 0
                    if j+1 != 3:
                        j = j+1

                else:
                    j -= 1

        return returnBoard

