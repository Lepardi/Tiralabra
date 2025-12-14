import unittest
import copy
import random
from game import Game

class TestRandom:
    def randint(self, range1, range2):
        return 1

class TestRandom2:
    def randint(self, range1, range2):
        return 3

class TestGame(unittest.TestCase):
    def setUp(self):
        nonrandomRandom = TestRandom()
        nonrandomRandom2 = TestRandom2()
        self.game = Game(random)
        self.game_not_random = Game(nonrandomRandom)
        self.game_not_random2 = Game(nonrandomRandom2)

    def test_addNumToBoard_adds_four_to_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        self.game_not_random.setBoard(test_board)
        self.game_not_random.addNumToBoard()
        self.assertEqual(4, self.game_not_random.getBoard()[1][1])

    def test_addNumToBoard_adds_two_to_board(self):
        test_board =  [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        self.game_not_random2.setBoard(test_board)
        self.game_not_random2.addNumToBoard()
        self.assertEqual(2, self.game_not_random2.getBoard()[3][3])

    def test_addNumToBoard_adds_num_to_random_place(self):
        prev_board = copy.deepcopy(self.game.getBoard())
        self.game.addNumToBoard()
        self.assertNotEqual(prev_board, self.game.getBoard())

    def test_starGame_initiates_game_correctly(self):
        test_board =  [[0,0,0,4],
                       [0,512,0,0],
                       [0,0,2,0],
                       [0,0,0,1024]]
        
        self.game.setBoard(test_board)
        self.game.startGame()
        board_after_start = self.game.getBoard()
        board_after_start_as_one_list = (board_after_start[0]+board_after_start[1]+
                                        board_after_start[2]+board_after_start[3])
        contains_two_or_four = (2 in board_after_start_as_one_list or 
                                4 in board_after_start_as_one_list)
        self.assertEqual(True, contains_two_or_four)
        self.assertEqual(15, board_after_start_as_one_list.count(0))

    def test_copyBoard_returns_copied_board(self):
        test_board =  [[0,0,0,4],
                       [0,512,0,0],
                       [0,0,2,0],
                       [0,0,0,1024]]
        
        copied_board = self.game.copyBoard(test_board)
        self.assertEqual(test_board, copied_board)

    def test_getBoard_gets_board(self):
        board = self.game.getBoard()
        test_board =  [[0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0]]
        self.assertEqual(board, test_board)
    
    def test_getHighestNum_gets_highest_num(self):
        test_board =  [[0,0,0,4],
                       [0,512,0,0],
                       [0,0,2,0],
                       [0,0,0,1024]]
        test_num = self.game.getHighestNum(test_board)
        self.assertEqual(test_num, 1024)

    def test_getZeroPositions_gets_all_zero_positions(self):
        test_board =  [[0,2,2,2],
                        [2,2,2,2],
                        [2,2,2,2],
                        [2,2,0,0]]
        zero_positions = self.game.getZeroPositions(test_board)
        test_zero_positions = [(0,0),(3,2),(3,3)]
        self.assertEqual(test_zero_positions, zero_positions)

    def test_getFirstZeroPosition_gets_first_zero_position(self):
        test_board =  [[2,2,2,2],
                        [2,2,2,2],
                        [2,2,2,2],
                        [2,2,0,0]]
        zero_position = self.game.getFirstZeroPosition(test_board)
        self.assertEqual((3,2), zero_position)

    def test_getFirstZeroPosition_returns_correctly_for_full_board(self):
        test_board =  [[2,2,2,2],
                        [2,2,2,2],
                        [2,2,2,2],
                        [2,2,2,2]]
        zero_position = self.game.getFirstZeroPosition(test_board)
        self.assertEqual((None, None), zero_position)

    def test_setBoard_sets_the_board(self):
        board_to_set =  [[0,2,2,2],
                        [2,2,2,2],
                        [2,2,2,2],
                        [2,2,0,0]]
        self.game.setBoard(board_to_set)
        self.assertEqual(board_to_set, self.game.getBoard())

    def test_setNumToBoard_sets_num_to_board(self):
        test_board =  [[0,0,0,0],
                       [0,0,0,0],
                       [0,0,0,0],
                       [0,0,0,0]]
        
        test_board_modified = self.game.setNumToBoard(2, (3,2), test_board)
        self.assertEqual(test_board_modified[3][2], 2)

    def test_isBoardFull_sees_that_board_is_full(self):
        test_board = [[2,4,8,16],
                     [256,128,64,32],
                     [1024,2,4,8],
                     [2,4,8,2]]
        
        self.assertEqual(True, self.game.isBoardFull(test_board))

    def test_isBoardFull_sees_that_board_is_not_full_when_board_has_zero(self):
        test_board = [[2,4,8,16],
                     [256,128,64,32],
                     [1024,2,4,8],
                     [2,4,0,4]]
        
        self.assertEqual(False, self.game.isBoardFull(test_board))

    def test_isBoardFull_sees_that_board_is_not_full_when_move_is_possbile(self):
        test_board = [[2,4,8,16],
                     [256,128,64,32],
                     [1024,2,4,8],
                     [2,2,2,2]]
        
        self.assertEqual(False, self.game.isBoardFull(test_board))

    def test_isGameWon_sees_that_game_is_won(self):
        test_board = [[2,4,8,16],
                     [256,128,64,32],
                     [1024,2048,4,8],
                     [2,2,2,2]]
        
        self.assertEqual(True, self.game.isGameWon(test_board))

    def test_isGameWon_sees_that_game_is_not_won(self):
        test_board = [[2,4,8,16],
                     [256,128,64,32],
                     [1024,2,4,8],
                     [2,2,2,2]]
        
        self.assertEqual(False, self.game.isGameWon(test_board))

    def test_moveBoardUp_moves_board_up_correctly(self):
        board_to_move =  [[2,0,0,4],
                         [2,0,0,8],
                         [2,0,0,8],
                         [2,0,0,0]]
        
        board_after_move = [[4,0,0,4],
                            [4,0,0,16],
                            [0,0,0,0],
                            [0,0,0,0]]
        
        moved_board = self.game.moveBoardUp(board_to_move)
        self.assertEqual(board_after_move, moved_board)

    def test_moveBoardDown_moves_board_down_correctly(self):
        board_to_move =  [[2,0,0,4],
                         [2,0,0,8],
                         [2,0,0,8],
                         [2,0,0,0]]
        
        board_after_move = [[0,0,0,0],
                            [0,0,0,0],
                            [4,0,0,4],
                            [4,0,0,16]]
        
        moved_board = self.game.moveBoardDown(board_to_move)
        self.assertEqual(board_after_move, moved_board)

    def test_moveBoardLeft_moves_board_Left_correctly(self):
        board_to_move =  [[2,2,2,2],
                         [0,0,0,0],
                         [0,0,0,0],
                         [0,8,8,4]]
        
        board_after_move = [[4,4,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [16,4,0,0]]
        
        moved_board = self.game.moveBoardLeft(board_to_move)
        self.assertEqual(board_after_move, moved_board)

    def test_moveBoardRight_moves_board_Right_correctly(self):
        board_to_move =  [[2,2,2,2],
                         [0,0,0,0],
                         [0,0,0,0],
                         [0,8,8,4]]
        
        board_after_move = [[0,0,4,4],
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,0,16,4]]
        
        moved_board = self.game.moveBoardRight(board_to_move)
        self.assertEqual(board_after_move, moved_board)

    def test_isMovePossible_correctly_sees_move_is_possible_up(self):
        board_to_move =  [[2,0,0,4],
                        [2,0,0,8],
                        [2,0,0,8],
                        [2,0,0,0]]
        
        self.assertEqual(True, self.game.isMovePossible("up", board_to_move))

    def test_isMovePossible_correctly_sees_move_is_not_possible_up(self):
        board_to_move =  [[2,0,0,4],
                        [4,0,0,8],
                        [2,0,0,2],
                        [4,0,0,4]]
        
        self.assertEqual(False, self.game.isMovePossible("up", board_to_move))

    def test_isMovePossible_correctly_sees_move_is_possible_down(self):
        board_to_move =  [[2,0,0,4],
                        [2,0,0,8],
                        [2,0,0,8],
                        [2,0,0,0]]
        
        self.assertEqual(True, self.game.isMovePossible("down", board_to_move))

    def test_isMovePossible_correctly_sees_move_is_not_possible_down(self):
        board_to_move =  [[2,0,0,4],
                        [4,0,0,8],
                        [2,0,0,2],
                        [4,0,0,4]]
        
        self.assertEqual(False, self.game.isMovePossible("down", board_to_move))

    def test_isMovePossible_correctly_sees_move_is_possible_left(self):
        board_to_move =  [[2,0,0,4],
                        [2,0,0,8],
                        [2,0,0,8],
                        [2,0,0,0]]
        
        self.assertEqual(True, self.game.isMovePossible("left", board_to_move))

    def test_isMovePossible_correctly_sees_move_is_not_possible_left(self):
        board_to_move =  [[2,0,0,0],
                        [2,0,0,0],
                        [2,0,0,0],
                        [2,0,0,0]]
        
        self.assertEqual(False, self.game.isMovePossible("left", board_to_move))

    def test_isMovePossible_correctly_sees_move_is_possible_right(self):
        board_to_move =  [[2,0,0,4],
                        [2,0,0,8],
                        [2,0,0,8],
                        [2,0,0,0]]
        
        self.assertEqual(True, self.game.isMovePossible("right", board_to_move))

    def test_isMovePossible_correctly_sees_move_is_not_possible_right(self):
        board_to_move =  [[0,0,0,4],
                        [0,0,0,8],
                        [0,0,0,8],
                        [0,0,0,0]]
        
        self.assertEqual(False, self.game.isMovePossible("right", board_to_move))

    def test_isMovePossible_returns_false_with_wrong_direction_parameter(self):
        board_to_move =  [[0,0,0,4],
                        [0,0,0,8],
                        [0,0,0,8],
                        [0,0,0,0]]
        
        self.assertEqual(False, self.game.isMovePossible("upf", board_to_move))


    def test_move_board_correctly_moves_board_up(self):
        board_to_move =  [[2,0,0,0],
                        [2,0,0,8],
                        [0,0,0,8],
                        [0,0,0,0]]
        
        self.game.setBoard(board_to_move)
        self.game.moveBoard("up")
        board_after_move = self.game.getBoard() 
        board_after_move_as_one_list = (board_after_move[0]+board_after_move[1]+
                                        board_after_move[2]+board_after_move[3])
        
        self.assertEqual(13, board_after_move_as_one_list.count(0))
        self.assertEqual([4, 16], [board_after_move[0][0], board_after_move[0][3]])

    def test_move_board_correctly_moves_board_down(self):
        board_to_move =  [[2,0,0,0],
                        [2,0,0,8],
                        [0,0,0,8],
                        [0,0,0,0]]
        
        self.game.setBoard(board_to_move)
        self.game.moveBoard("down")
        board_after_move = self.game.getBoard() 
        board_after_move_as_one_list = (board_after_move[0]+board_after_move[1]+
                                        board_after_move[2]+board_after_move[3])
        
        self.assertEqual(13, board_after_move_as_one_list.count(0))
        self.assertEqual([4, 16], [board_after_move[3][0], board_after_move[3][3]])

    def test_move_board_correctly_moves_board_left(self):
        board_to_move =  [[2,2,0,0],
                        [0,8,0,8],
                        [0,0,0,0],
                        [0,0,0,0]]
        
        self.game.setBoard(board_to_move)
        self.game.moveBoard("left")
        board_after_move = self.game.getBoard() 
        board_after_move_as_one_list = (board_after_move[0]+board_after_move[1]+
                                        board_after_move[2]+board_after_move[3])
        
        self.assertEqual(13, board_after_move_as_one_list.count(0))
        self.assertEqual([4, 16], [board_after_move[0][0], board_after_move[1][0]])

    def test_move_board_correctly_moves_board_right(self):
        board_to_move =  [[2,2,0,0],
                        [0,8,0,8],
                        [0,0,0,0],
                        [0,0,0,0]]
        
        self.game.setBoard(board_to_move)
        self.game.moveBoard("right")
        board_after_move = self.game.getBoard() 
        board_after_move_as_one_list = (board_after_move[0]+board_after_move[1]+
                                        board_after_move[2]+board_after_move[3])
        
        self.assertEqual(13, board_after_move_as_one_list.count(0))
        self.assertEqual([4, 16], [board_after_move[0][3], board_after_move[1][3]])