
class UI:
    """Class for the user interface of the program
    """

    def __init__(self, game):
        """Constructor for the UI

        Args:
            game: The game object which handles the game functions 
        """
        self.game = game

    def printUILoop(self):
        """Function for the UI loop
        """
        print("2048 peli")

        while True:
            print("Syötä komennoksi 1 jos haluat pelata 2048 peliä itse")
            print("Syötä komennoksi 2 jos haluat että tekoäly pelaa peliä")
            print("Syötä komennoksi q lopettaaksesi ohjelma")
            command = input("Komento: ")
            if command == "1":
                self.game.startGame()
                print()
                self.printGameLoop()
            if command == "2":
                print("Ei vielä toteutettu!" + "\n")

            if command == "q":
                print("Hyvästi.")
                break


    def printGameLoop(self):
        """Print the loop for the player to play the game himself
        """

        print("Syötä q lopettaaksesi peli")
        print("Syötä w liikuttaaksesi lautaa ylös")
        print("Syötä s liikuttaaksesi lautaa alas")
        print("Syötä a liikuttaaksesi lautaa vasemalle")
        print("Syötä d liikuttaaksesi lautaa oikealla")
        print()
        while True:
            self.printBoardState()
            print()
            command = input("Suunta: ")

            if command == "a":
                self.game.moveBoard("left")
            if command == "d":
                self.game.moveBoard("right")
            if command == "w":
                self.game.moveBoard("up")
            if command == "s":
                self.game.moveBoard("down")
            if command == "q":
                print()
                break

            if  self.game.isBoardFull(self.game.getBoard()):
                print("Hävisit pelin!")
                self.printBoardState()
                print()
                break

            if self.game.isGameWon(self.game.getBoard()):
                print("Voitit pelin!")
                self.printBoardState()
                print()
                break

    def printBoardState(self):
        """Print the gameboard
        """
        board = self.game.getBoard()
        for i in range(4):
            print(board[i])
