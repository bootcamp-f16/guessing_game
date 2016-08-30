"""A guessing game."""

import random
import sys


class Game():
    """The game object."""

    def __init__(self, tries=10):
        """Initialize game instance."""
        self.tries = tries
        self.secret_number = random.randint(0, 100)

    def guess(self):
        user_guess = input("Guess a number >> ")

        try:
            user_guess = int(user_guess)
            self.tries -= 1
            if user_guess == self.secret_number:
                print("Congratulations, you got it")
                sys.exit()
            elif user_guess < self.secret_number:
                print("Too low. You have {} tries remaining.".format(
                    self.tries
                ))
            else:
                print("Too high. You have {} tries remaining.".format(
                    self.tries)
                )
        except ValueError:
            # Give the user an exit hatch
            if user_guess.lower() == 'x':
                print("Thank you for playing!")
                sys.exit()
            # Warn of invalid input
            else:
                print("Error: you need to enter a number, or x to quit")

    def play_loop(self):
        print("You may hit x to quit at any time.")
        while self.tries > 0:
            self.guess()
        sys.exit()


def main():
    print("In this game, you guess a number between 0 and 100.")
    print("How many tries do you want? Hit enter to default to 10, or hit " +
          "x to cancel.")
    while True:
        user_input = input('>> ')
        if user_input.lower() == 'x':
            sys.exit()
        elif user_input == '':
            game = Game()
            game.play_loop()
            print("Thanks for playing!")
        elif user_input.isdigit():
            game = Game(int(user_input))
            game.play_loop()
            print("Thanks for playing!")
        else:
            print("You have entered invalid input. Please enter the number " +
                  "of tries you want, enter to default to 10, or x to cancel")

if __name__ == "__main__":
    main()
