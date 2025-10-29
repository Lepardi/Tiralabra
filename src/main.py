from ui import UI
from game import Game


def main():
    game = Game()
    ui = UI(game)
    ui.printUILoop()


if __name__ == "__main__":
    main()