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
        
        self.assertEqual(33423360, self.ai.heuristic(test_board))

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
        
        self.assertEqual(-99999999999999999, self.ai.expectiminimax(test_board, 2, True))

    def test_getNextMove_returns_up_when_that_is_next_best_move(self):
        test_board =  [[1024,0,2,4],
                      [4,1024,4,8],
                      [8,2,8,2],
                      [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual("up", self.ai.getNextMove(1))

    def test_getNextMove_returns_left_when_that_is_next_best_move(self):
        test_board =  [[1024,2,2,4],
                      [512,512,4,8],
                      [8,2,8,2],
                      [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual("left", self.ai.getNextMove(2))

    def test_getNextMove_returns_down_when_that_is_next_best_move2(self):
        test_board =  [[1024,4,2,4],
                      [0,0,0,0],
                      [0,512,256,256],
                      [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual("down", self.ai.getNextMove(3))

    def test_getNextMove_returns_up_when_that_is_next_best_move2(self):
        test_board =  [[1024,256,256,256],
                        [0,4,2,256],
                        [8,2,8,2],
                        [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual("up", self.ai.getNextMove(3))

    def test_getNextMove_returns_up_when_that_is_next_best_move3(self):
        test_board =  [[1024,256,128,64],
                        [0,8,16,0],
                        [4,2,8,32],
                        [4,4,4,4]]
        self.game.setBoard(test_board)
        self.assertEqual("up", self.ai.getNextMove(2))

    def test_aiLoop_loses_the_game_correctly(self):
        test_board =  [[1024,512,2,256],
                        [2,8,16,2],
                        [4,2,8,32],
                        [2,4,2,4]]
        self.game.setBoard(test_board)
        self.assertEqual(1024, self.ai.aiLoop(3, 500))  

    def test_aiLoop_wins_the_game_when_possible(self):
        test_board =  [[1024,512,256,256],
                        [0,8,16,0],
                        [4,2,8,32],
                        [4,4,4,4]]
        self.game.setBoard(test_board)
        self.assertEqual(2048, self.ai.aiLoop(3, 500))  
         
    def test_aiLoop_wins_the_game_when_possible2(self):
        test_board =  [[1024,512,256,128],
                        [0,8,16,128],
                        [4,2,8,32],
                        [4,4,4,4]]
        self.game.setBoard(test_board)
        self.assertEqual(2048, self.ai.aiLoop(4, 500)) 

    def test_aiLoop_wins_the_game_when_possible3(self):
        test_board =  [[1024,512,256,128],
                        [0,8,128,0],
                        [4,2,8,32],
                        [4,4,4,4]]
        self.game.setBoard(test_board)
        self.assertEqual(2048, self.ai.aiLoop(5, 500)) 