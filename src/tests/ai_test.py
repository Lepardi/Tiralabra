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
        
        self.assertEqual(4*15, self.ai.heuristic(test_board))

    def test_heuristic_returns_correct_value_for_board_where_highest_in_correct_place(self):
        test_board =  [[64,32,16,8],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(3342336000, self.ai.heuristic(test_board))

    def test_expectiminimax_returns_correct_value_for_empty_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(0, self.ai.expectiminimax(test_board, 0, True))

    def test_expectiminimax_returns_correct_value_for_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,2,0,0]]
        
        self.assertEqual(4*15, self.ai.expectiminimax(test_board, 0, True))

    def test_expectiminimax_returns_correct_value_for_winning_board(self):
        test_board =  [[0,0,0,0],
                      [0,2048,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(99999999999999999, self.ai.expectiminimax(test_board, 2, True))

    def test_expectiminimax_returns_correct_value_for_full_board(self):
        test_board =  [[2,4,2,4],
                      [4,1024,4,8],
                      [8,2,8,2],
                      [2,4,2,4]]
        
        self.assertEqual(-999999999999999999, self.ai.expectiminimax(test_board, 2, True))

    