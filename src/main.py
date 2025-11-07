from ui import UI
from game import Game
from ai import AI
import random


def main():
    game = Game(random)
    ai = AI(game)
    ui = UI(game, ai)
    ui.printUILoop()

if __name__ == "__main__":
    main()