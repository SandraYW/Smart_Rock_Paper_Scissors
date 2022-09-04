import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Sorry, the option "{option}" is invalid. Try again!')


class Player:
    moves = ["rock", "paper", "scissors"]
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    # Always plays rock
    def move(self):
        return "rock"


class RandomPlayer(Player):
    def move(self):
        #  Return any of the options inside moves list randomly
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        #  Plays random choice on first move
        return self.their_move

        # Returns the same move as the other player
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        # chooses a a different move than that previously played
        index = moves.index(self.my_move) + 1
        return moves[index % len(moves)]

    def learn(self, my_move, their_move):
        self.my_move = my_move


class HumanPlayer(Player):
    def move(self):
        # Asks user what move they want to make and returns
        # true if user input matches any of the options
        while True:
            return valid_input("Rock, paper, scissors? Choose! ", moves)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # initial scores for Players
        self.score_p1 = 0
        self.score_p2 = 0

    @staticmethod
    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        #  Prints each players move
        # print(f"Player 1: {move1}  Player 2: {move2}")
        # Determine the winner and store player scores
        if self.beats(move1, move2):
            self.score_p1 += 1
            results = "** PLAYER TWO (Computer) WINS **"
        elif move1 == move2:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            results = "** TIE **"
        else:
            self.score_p2 += 1
            results = "** PLAYER ONE WINS **"

        # Show match results to player
        print(f"You played {move2}\n"
              f"Your opponent played {move1}\n"
              f"{results}\n"
              f"Score: Player one ( {self.score_p2} ), "
              f"Player two ( {self.score_p1} )\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def number_of_rounds(self):
        # Asks user for no. of rounds
        while True:
            self.no_rounds = input("How many rounds would "
                                   "you like to play for? ")
            if self.no_rounds.isdigit():
                return self.no_rounds
            print(f"Sorry, the option '{self.no_rounds}' is "
                  "invalid. Try again!")

    def play_game(self):
        print("Game start!")
        self.number_of_rounds()
        for round in range(int(self.no_rounds)):
            print(f"Round {round + 1}:")
            self.play_round()
        if self.score_p1 == self.score_p2:
            print("** It's a tie! **\n"
                  f"Score: Player one ( {self.score_p2} ), "
                  f"Player two ( {self.score_p1} )")
        elif self.score_p2 > self.score_p1:
            print("** Player ONE has won! **\n"
                  f"Score: Player one ( {self.score_p2} ), "
                  f"Player two ( {self.score_p1} )")
        else:
            print("** Player TWO (Computer) has won! **\n"
                  f"\nScore: Player one ( {self.score_p2} ), "
                  f"Player two ( {self.score_p1} )")


def play_again():
    choice = valid_input("Press 'q' to quit or 'c' to continue: ", ['q', 'c'])
    if choice == 'q':
        print('Thanks for playing! Goodbye!')
        exit(0)


def game():
    while True:
        players = [
            AllRockPlayer(),
            RandomPlayer(),
            ReflectPlayer(),
            CyclePlayer()
            ]
        p1 = random.choice(players)
        p2 = HumanPlayer()
        game = Game(p1, p2)
        game.play_game()

        play_again()


if __name__ == '__main__':
    game()
