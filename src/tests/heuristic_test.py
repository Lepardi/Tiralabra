import unittest
from heuristic import Heuristic

class TestHeuristic(unittest.TestCase):
    def setUp(self):
        self.heuristic = Heuristic()

    def test_heuristic_returns_correct_value_for_empty_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(0, self.heuristic.heuristic(test_board))

    def test_heuristic_returns_correct_value_for_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,2,0,0]]
        
        self.assertEqual(8, self.heuristic.heuristic(test_board))

    def test_heuristic_returns_correct_value_for_board_where_highest_in_correct_place(self):
        test_board =  [[64,32,16,8],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
        self.assertEqual(78517370880, self.heuristic.heuristic(test_board))