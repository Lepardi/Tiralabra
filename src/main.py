from ui import UI
from game import Game
from ai import AI
from heuristic import Heuristic
import random


def main():
    game = Game(random)
    heuristic = Heuristic()
    ai = AI(game, heuristic)
    ui = UI(game, ai)
    ui.printUILoop()

if __name__ == "__main__":
    main()
