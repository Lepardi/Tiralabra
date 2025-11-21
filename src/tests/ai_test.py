import unittest
import random
from game import Game
from ai import AI

class TestAi(unittest.TestCase):
    def setUp(self):
        self.game = Game(random)
        self.ai = AI(self.game)

    def test_heuristic_returns_correct_value_for_empty_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(0, self.ai.heuristic(test_board))

    def test_heuristic_returns_correct_value_for_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,2,0,0]]
        
        self.assertEqual(8, self.ai.heuristic(test_board))

    def test_heuristic_returns_correct_value_for_board_where_highest_in_correct_place(self):
        test_board =  [[64,32,16,8],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(78517370880, self.ai.heuristic(test_board))

    def test_expectiminimax_returns_correct_value_for_empty_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(0, self.ai.expectiminimax(test_board, 0, True, mode=0))

    def test_expectiminimax_returns_correct_value_for_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,2,0,0]]
        
        self.assertEqual(8, self.ai.expectiminimax(test_board, 0, True, mode=0))

    #def test_expectiminimax_returns_correct_value_for_winning_board(self):
    #    test_board =  [[0,0,0,0],
    #                  [0,2048,0,0],
    #                  [0,0,0,0],
    #                  [0,0,0,0]]
        
    #    self.assertEqual(99999999999999999, self.ai.expectiminimax(test_board, 2, True, mode=0))

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

    def test_aiLoop_loses_the_game_correctly(self):
        test_board =  [[1024,512,2,256],
                        [2,8,16,2],
                        [4,2,8,32],
                        [2,4,2,4]]
        self.game.setBoard(test_board)
        highest_num = self.ai.aiLoop(1, 500, mode=1)
        self.assertEqual(1024, highest_num)  
