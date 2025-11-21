import copy
import random

class AI:
    def __init__(self, game):
        """Constructor for the AI object

        Attributes:
            evaluationMatrix: The matrix which is used to calculate 
            the heuristic value of the gameboard

        Args:
            game: The game object which is used for playing 
        """
        self.game = game
        self.evaluationMatrix = [[4**15, 4**14, 4**13, 4**12],
                                [4**8, 4**9, 4**10, 4**11],
                                [4**7, 4**6,4**5,4**4],
                                [4**0, 4**1, 4**2, 4**3]]

        #self.evaluationMatrix = [[2**15, 2**14, 2**13, 2**12],
        #                        [2**8, 2**9, 2**10, 2**11],
        #                        [2**7, 2**6,2**5,2**4],
        #                        [2**0, 2**1, 2**2, 2**3]]

    def printBoardState(self):
        """Print the gameboard
        """
        board = self.game.getBoard()
        for i in range(4):
            print(board[i])
        print()

    def aiLoop(self, depth, numberOfMoves, mode = None):
        movesCounter = 0
        while True:

            if movesCounter % int(numberOfMoves) == 0:
                print("Siirtoja " + str(movesCounter) + ":")
                self.printBoardState()
            movesCounter += 1

            move = self.getNextMove(int(depth), (mode))
            self.game.moveBoard(move)
            board = self.game.getBoard()
            #if self.game.isGameWon(board):
            #    print("Voitit pelin " + str(movesCounter) + " siirron jälkeen:")
            #    self.printBoardState()
            #    return (self.game.getHighestNum(board))
                
            if self.game.isBoardFull(board):
                print("Häviö " + str(movesCounter) + " siirron jälkeen:")
                self.printBoardState()
                return (self.game.getHighestNum(board))

    def getNextMove(self, depth, mode = None):
        """Function for determining the next best move to make. 
           Calls the expectiminimax algorithm function to value the moves

        Args:
            depth: The depth of the search tree for the algorithm

        Returns:
            The direction into which move the board
        """
        moves = ["up","down","left","right"]
        bestMove = None
        bestMoveScore = -999999999999999999
                        
        for move in moves:
            moveScore = -999999999999999999
            prevBoard = copy.deepcopy(self.game.getBoard())
            if self.game.isMovePossible(move, prevBoard):
                #self.game.moveBoard(move)
                #movedBoard = self.game.getBoard()
                #moveScore = self.expectiminimax(movedBoard, depth, True)
                #self.game.setBoard(prevBoard)

                if move == "up":
                    movedBoard = copy.deepcopy(self.game.moveBoardUp(prevBoard))
                    moveScore = self.expectiminimax(movedBoard, depth, False, mode)
                    self.game.setBoard(prevBoard)

                if move == "down":
                    movedBoard = copy.deepcopy(self.game.moveBoardDown(prevBoard))
                    moveScore = self.expectiminimax(movedBoard, depth, False, mode)
                    self.game.setBoard(prevBoard)

                if move == "left":
                    movedBoard = copy.deepcopy(self.game.moveBoardLeft(prevBoard))
                    moveScore = self.expectiminimax(movedBoard, depth, False, mode)
                    self.game.setBoard(prevBoard)

                if move == "right":
                    movedBoard = copy.deepcopy(self.game.moveBoardRight(prevBoard))
                    moveScore = self.expectiminimax(movedBoard, depth, False, mode)
                    self.game.setBoard(prevBoard)

                if moveScore > bestMoveScore:
                    bestMove = move
                    bestMoveScore = moveScore

        return bestMove

    def expectiminimax(self, board, depth, playerTurn, mode = None):
        """The function for the expectiminimax

        Args:
            board: the game board on which the moves are made, an array of arrays of integers
            depth: The depth of the search tree for the algorithm, in other words the recursion depth
            playerTurn: True or False value. True when the recursion node is to make a move made on board
                        False when recursion node is to add a random number on board

        Returns: 
            The heuristic value of the board after the depth number of moves
        """
        #self.printBoardState(board)
        #if self.game.isGameWon(board):
        #    return 99999999999999999
        #if self.game.isBoardFull(board):
        #    return -99999999999999999
        if depth == 0:
            return self.heuristic(board)

        alpha = 0
        if playerTurn:
            isFull = True
            moves = ["up","down","left","right"]
            for move in moves:
                if self.game.isMovePossible(move, board):
                    isFull = False
                    if move == "up":
                        tmpBoard = (self.game.moveBoardUp(board))
                        tmpAlpha = self.expectiminimax(tmpBoard, depth-1, False, mode)

                    if move == "down":
                        tmpBoard = (self.game.moveBoardDown(board))
                        tmpAlpha = self.expectiminimax(tmpBoard, depth-1, False, mode)

                    if move == "left":
                        tmpBoard = (self.game.moveBoardLeft(board))
                        tmpAlpha = self.expectiminimax(tmpBoard, depth-1, False, mode)    

                    if move == "right":
                        tmpBoard = (self.game.moveBoardRight(board))
                        tmpAlpha = self.expectiminimax(tmpBoard, depth-1, False, mode)    

                    if tmpAlpha > alpha:
                        alpha = tmpAlpha
            if isFull:
                return -99999999999999999
        #Muokkaaa lautaa suoraan,älä kutsu setnumtoboard!
        else:
            if mode == 1:
                freeSpaces = self.game.getZeroPositions(board)
                for position in freeSpaces:
                    #board = self.game.setNumToBoard(2, position, board)
                    board[position[0]][position[1]] = 2
                    alpha += (self.expectiminimax(board, depth, True, mode))*0.9
                    #board = self.game.setNumToBoard(4, position, board)
                    board[position[0]][position[1]] = 4
                    alpha += (self.expectiminimax(board, depth, True, mode))*0.1
            else:
                freeSpace = self.game.getFirstZeroPosition(board)
                #board = self.game.setNumToBoard(2, (freeSpace), board)
                board[freeSpace[0]][freeSpace[1]] = 2
                alpha += self.expectiminimax(board, depth, True, mode)
                #board = self.game.setNumToBoard(4, (freeSpace), board)
                #alpha += self.expectiminimax(board, depth, True, mode)*0.1

        return alpha
        
    def heuristic(self, board):
        """The heuristic function for determining  value of given game board
        Uses the evaluation matrix to calculate a value for the board based
        on the numbers on the board. Rewards for having the largest number 
        on upper left corner and other higher values next to this value

        Args: 
            board: The board whiches value is to be estimated

        Returns:
            The heuristic value of the given board
        """

        estimate = 0
        #freeSpaces = len(self.game.getZeroPositions(board))
        for i in range(4):
            for j in range(4):
                estimate += (board[i][j]*self.evaluationMatrix[i][j])#freeSpaces

        #highest = self.game.getHighestNum(board)
        
        #if board[0][0] == highest:
        #    estimate = estimate*2

        #if ((board[0][0] == highest) and (board[0][1] == highest/2) 
        #    and (board[0][2] < (highest/2)/2) and (board[0][3] < ((highest/2)/2)/2)):
        #    #and board[1][3] == board[0][3]):
        #    estimate = estimate*10

        return estimate
