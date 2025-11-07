import unittest
import copy
from game import Game
from ai import AI

class TestGame(unittest.TestCase):
    def setUp(self):
        self.ai = AI()

        