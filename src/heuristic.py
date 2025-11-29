
class Heuristic:
    def __init__(self):
        """ Constructor for the Heuristic object which is used by the expectiminimax
        to determine the goodness of a board

        Attributes:
            evaluationMatrix: The matrix which is used to calculate 
            the heuristic value of the gameboard
        """

        self.evaluationMatrix = [[4**15, 4**14, 4**13, 4**12],
                                 [4**8, 4**9, 4**10, 4**11],
                                 [4**7, 4**6,4**5,4**4],
                                 [4**0, 4**1, 4**2, 4**3]]
        

    def heuristic(self, board):
        """The heuristic function for determining  value of given game board
        Uses the evaluation matrix to calculate a value for the board based
        on the numbers on the board. The snake matrix adapted from Nie et al

        Args: 
            board: The board whiches value is to be estimated

        Returns:
            The heuristic value of the given board
        """

        estimate = 0
        for i in range(4):
            for j in range(4):
                estimate += (board[i][j]*self.evaluationMatrix[i][j])

        return estimate
        
