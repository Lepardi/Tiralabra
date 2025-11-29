import copy
import random

class AI:
    def __init__(self, game, heuristic):
        """Constructor for the AI object

        Args:
            game: The game object which is used for playing 
            heuristic: The heuristic object used to determine a boards value
        """
        self.game = game
        self.evaluator = heuristic

    def printBoardState(self):
        """Print the gameboard
        """
        board = self.game.getBoard()
        for i in range(4):
            print(board[i])
        print()

    def aiLoop(self, depth, numberOfMoves, mode = None):
        """Function for the AI loop to play the game and call new moves

        Args:
            depth: The depth of the search tree for the algorithm
            numberOfMoves: This number determines after how many moves
            the game board is printed for user to see
            mode: This parameter tells the function which expectiminimax
            form is to be used
            
        Returns:
            The highest num from the board after game is over
        """
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
            mode: This parameter tells the function which expectiminimax
            form is to be used
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
            mode: This parameter tells the function which expectiminimax
            form is to be used

        Returns: 
            The heuristic value of the board after the depth number of moves
        """
        #self.printBoardState(board)
        #if self.game.isGameWon(board):
        #    return 99999999999999999
        #if self.game.isBoardFull(board):
        #    return -99999999999999999
        if depth == 0:
            #print(self.evaluator.heuristic(board))
            return self.evaluator.heuristic(board)

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

        else:
            if mode == 1:
                freeSpaces = self.game.getZeroPositions(board)
                for position in freeSpaces:
                    board[position[0]][position[1]] = 2
                    alpha += round(((self.expectiminimax(board, depth, True, mode))*0.9)/len(freeSpaces))
                    board[position[0]][position[1]] = 4
                    alpha += round((self.expectiminimax(board, depth, True, mode))*0.1)/len(freeSpaces)
            else:
                freeSpace = self.game.getFirstZeroPosition(board)
                board[freeSpace[0]][freeSpace[1]] = 2
                alpha += self.expectiminimax(board, depth, True, mode)
                #board = self.game.setNumToBoard(4, (freeSpace), board)
                #alpha += self.expectiminimax(board, depth, True, mode)*0.1

        return alpha
