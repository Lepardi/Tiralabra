
class UI:
    """Class for the user interface of the program
    """

    def __init__(self, game, ai):
        """Constructor for the UI

        Args:
            game: The game object which handles the game functions 
            ai: The AI to play the game with help of expectiminimax
        """
        self.game = game
        self.ai = ai

    def printUILoop(self):
        """Function for the UI loop
        """
        print()
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
                print()
                self.printAIGameLoop()
            if command == "q":
                print("Hyvästi." + "\n")
                break

    def printGameLoop(self):
        """Function for the game loop for the player to play the game
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
    

    def printAIGameLoop(self):
        """Function for printing the UI loop from which is used to call the AI loop and
          to issue parameters for the AI to play the game.
          Will also print the highest value from the gameboard after each play of the game
        """
        while True:
            print("Syötä hakupuun syvyys (Syötä q palataksesi ohjelmavalikkoon)")
            depth = input("Syvyys: ")
            if depth == "q":
                break
            try:
                depth = int(depth)
                if depth < 0:
                    print("Syvyyden pitää olla positiivinen luku." + "\n")
                    continue
            except ValueError:
                print("Syvyyden pitää olla positiivinen luku." + "\n")
                continue
            print()
            print("Syötä kuinka monta kertaa tekoäly pelaa (Syötä q palataksesi ohjelmavalikkoon)")
            numberOfGames = input("Määrä: ")
            if numberOfGames == "q":
                break
            try:
                numberOfGames = int(numberOfGames)
                if numberOfGames < 1:
                    print("Pelien määrän pitää olla positiivinen luku." + "\n")
                    continue
            except ValueError:
                print("Pelien määrän pitää olla positiivinen luku." + "\n")
                continue
            print()
            print("Syötä kuinka monen liikkeen välein pelilauta näytetään (Syötä q palataksesi ohjelmavalikkoon)")
            numberOfMoves = input("Määrä: ")
            if numberOfMoves == "q":
                break
            try:
                numberOfMoves = int(numberOfMoves)
                if numberOfMoves < 1:
                    print("Liikeiden määrän pitää olla positiivinen luku." + "\n")
                    continue
            except ValueError:
                print("Liikeiden määrän pitää olla positiivinen luku." + "\n")
                continue
            print()
            print("Syötä missä moodissa äly pelaa (Syötä q palataksesi ohjelmavalikkoon)")
            mode = input("Moodi: ")
            if mode == "q":
                break
            try:
                mode = int(mode)
                if mode < 0:
                    print("Moodin pitää olla positiivinen luku." + "\n")
                    continue
            except ValueError:
                print("Moodin pitää olla positiivinen luku." + "\n")
                continue
            print()

            results = []
            for i in range(int(numberOfGames)):
                self.game.startGame()
                results.append(self.ai.aiLoop(depth, numberOfMoves, int(mode)))

            print()
            print(results)
            print()
            

    def printBoardState(self):
        """Print the gameboard
        """
        board = self.game.getBoard()
        for i in range(4):
            print(board[i])
