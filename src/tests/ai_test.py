import unittest
import random
from game import Game
from ai import AI
from heuristic import Heuristic

class HeuristicTest:

    def __init__(self):
        self.game = Game(random)

    def heuristic(self, board):

        evaluationMatrix = [[4**15, 4**14, 4**13, 4**12],
                            [4**8, 4**9, 4**10, 4**11],
                            [4**7, 4**6,4**5,4**4],
                            [4**0, 4**1, 4**2, 4**3]]
        
        if (self.game.getHighestNum(board) >= 2048):
            return 100000000000000

        estimate = 0
        for i in range(4):
            for j in range(4):
                estimate += (board[i][j]*evaluationMatrix[i][j])

        return estimate

class TestAi(unittest.TestCase):
    def setUp(self):
        self.game = Game(random)
        heuristic = Heuristic()
        test_heuristic = HeuristicTest()
        self.ai = AI(self.game, heuristic)
        self.ai_with_test_heuristic = AI(self.game, test_heuristic)

    def test_expectiminimax_returns_correct_value_for_empty_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(0, self.ai.expectiminimax(test_board, 0, True, mode=1))

    def test_expectiminimax_returns_correct_value_for_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,2,0,0]]
        
        self.assertEqual(8, self.ai.expectiminimax(test_board, 0, True, mode=1))

    def test_expectiminimax_returns_correct_value_for_full_board(self):
        test_board =  [[2,4,2,4],
                      [4,1024,4,8],
                      [8,2,8,2],
                      [2,4,2,4]]

        self.assertEqual(-99999999999999999, self.ai.expectiminimax(test_board, 2, True, mode=1))

    def test_expectiminimax_returns_correct_value_for_full_board_in_mode_zero(self):
        test_board =  [[2,4,2,4],
                      [4,1024,4,8],
                      [8,2,8,2],
                      [2,4,2,4]]
        
        self.assertEqual(-99999999999999999, self.ai.expectiminimax(test_board, 2, True, mode=0))

    def test_expectiminimax_returns_correct_value_for_winning_board_with_depth_zero(self):
        test_board =  [[0,0,0,0],
                      [0,2048,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(100000000000000, self.ai_with_test_heuristic.expectiminimax(test_board, 0, True, mode=1))

    def test_expectiminimax_returns_correct_value_for_board_with_depth_1(self):
        test_board =  [[1024,1024,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(100000000000000, self.ai_with_test_heuristic.expectiminimax(test_board, 1, True, mode=1))

    def test_expectiminimax_returns_correct_value_for_winning_board_with_depth_3(self):
        test_board =  [[1024,512,256,256],
                      [16,32,64,16],
                      [256,8,0,32],
                      [16,512,128,8]]

        self.assertEqual(100000000000000, self.ai_with_test_heuristic.expectiminimax(test_board, 3, True, mode=1))

    def test_getNextMove_returns_up_when_that_is_next_best_move(self):
        test_board =  [[1024,0,2,4],
                      [1024,0,4,8],
                      [8,2,8,2],
                      [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual("up", self.ai.getNextMove(2, mode=1))

    def test_getNextMove_returns_left_when_that_is_next_best_move(self):
        test_board =  [[1024,2,2,4],
                      [512,512,4,8],
                      [8,2,8,2],
                      [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual("left", self.ai.getNextMove(3, mode=1))

    def test_getNextMove_returns_right_when_that_is_next_best_move(self):
        test_board =  [[2048,1024,512,256],
                      [2,2,128,128],
                      [8,2,8,2],
                      [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual("right", self.ai.getNextMove(1, mode=1))

    def test_aiLoop_loses_the_game_correctly(self):
        test_board =  [[1024,512,2,256],
                        [2,8,16,2],
                        [4,2,8,32],
                        [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual(1024, self.ai.aiLoop(1, 500, mode=1))  

    def test_aiLoop_plays_the_game_as_expected(self):
        test_board =  [[1024,512,256,256],
                        [2,8,16,2],
                        [4,2,8,32],
                        [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertLessEqual(2048, self.ai.aiLoop(1, 500, mode=1))  

    def test_aiLoop_plays_the_game_as_expected_in_mode_zero(self):
        test_board =  [[1024,512,256,256],
                        [2,8,16,2],
                        [4,2,8,32],
                        [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertLess(1024, self.ai.aiLoop(1, 500, mode=0))  
