# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:33:24 2023

@author: KIIT
"""

class CoinFlipGame:
    def __init__(self):
        self.user_guesses = []

    def guess_flips(self):
        print("Please make 10 consecutive guesses (0 for heads, 1 for tails):")
        guesses = []
        for _ in range(10):
            while True:
                guess = input("Guess {}: ".format(len(guesses) + 1))
                try:
                    guess = int(guess)
                    if guess not in [0, 1]:
                        raise ValueError("Invalid input. Please enter 0 for heads or 1 for tails.")
                    guesses.append(guess)
                    break  # Exit the input loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter 0 for heads or 1 for tails.")

        self.user_guesses = guesses
        return "Guesses submitted successfully..."

    def provide_flip_results(self, actual_results):
        if not self.user_guesses:
            return "Please make guesses before providing results."

        if actual_results == self.user_guesses:
            return "Congratulations! You've won a prize."
        else:
            return "Sorry, you didn't win this time. Try again!"

# Example usage:
if __name__ == "__main__":
    game = CoinFlipGame()

    # User makes guesses
    print(game.guess_flips())

    # Admin provides actual results
    actual_results = [1, 0, 0, 0, 1, 1, 1, 0, 0, 1]
    result_message = game.provide_flip_results(actual_results)
    print(result_message)
