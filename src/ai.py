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
        #self.evaluationMatrix = [[4**15, 4**14, 4**13, 4**12],
        #                        [4**8, 4**9, 4**10, 4**11],
        #                        [4**7, 4**6,4**5,4**4],
        #                        [4**0, 4**1, 4**2, 4**3]]

        self.evaluationMatrix = [[2**15, 2**14, 2**13, 2**12],
                                [2**8, 2**9, 2**10, 2**11],
                                [2**7, 2**6,2**5,2**4],
                                [2**0, 2**1, 2**2, 2**3]]

    def getNextMove(self, depth):
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
                self.game.moveBoard(move)
                movedBoard = self.game.getBoard()
                moveScore = self.expectiminimax(movedBoard, depth, True)
                self.game.setBoard(prevBoard)

                if moveScore > bestMoveScore:
                    bestMove = move
                    bestMoveScore = moveScore

        return bestMove

    def expectiminimax(self, board, depth, playerTurn):
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
        if self.game.isBoardFull(board):
            return -9999999999999999
        elif depth == 0:
            return self.heuristic(board)

        alpha = 0
        if playerTurn:
            moves = ["up","down","left","right"]
            for move in moves:
                if self.game.isMovePossible(move, board):

                    if move == "up":
                        tmpBoard = copy.deepcopy(self.game.moveBoardUp(board))
                        tmpAlpha = self.expectiminimax(tmpBoard, depth-1, False)

                    if move == "down":
                        tmpBoard = copy.deepcopy(self.game.moveBoardDown(board))
                        tmpAlpha = self.expectiminimax(tmpBoard, depth-1, False)

                    if move == "left":
                        tmpBoard = copy.deepcopy(self.game.moveBoardLeft(board))
                        tmpAlpha = self.expectiminimax(tmpBoard, depth-1, False)    

                    if move == "right":
                        tmpBoard = copy.deepcopy(self.game.moveBoardRight(board))
                        tmpAlpha = self.expectiminimax(tmpBoard, depth-1, False)    

                    if tmpAlpha > alpha:
                        alpha = tmpAlpha
     
        else:
            freeSpaces = self.game.getZeroPositions(board)
            #board = self.game.setNumToBoard(2, freeSpaces[random.randint(0, len(freeSpaces)-1)], board)
            #alpha += self.expectiminimax(board, depth, True)
            
            for position in freeSpaces:
                board = self.game.setNumToBoard(2, position, board)
                alpha += self.expectiminimax(board, depth, True)/len(freeSpaces)
            #alpha = alpha

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
        freeSpaces = len(self.game.getZeroPositions(board))
        for i in range(4):
            for j in range(4):
                estimate += (board[i][j]*self.evaluationMatrix[i][j])*freeSpaces

        highest = self.game.getHighestNum(board)
        
        if ((board[0][0] == highest) and (board[0][1] == highest/2) 
            and (board[0][2] < board[0][1]) and (board[0][3] < board[0][2])):
            estimate = estimate*100

        return estimate
