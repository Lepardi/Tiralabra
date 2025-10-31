from ui import UI
from game import Game
from ai import AI


def main():
    game = Game()
    ai = AI(game)
    ui = UI(game, ai)
    ui.printUILoop()


if __name__ == "__main__":
    main()