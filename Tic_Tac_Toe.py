# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:39:09 2023

@author: KIIT
"""

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
            
    def mark_space(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
        else:
            print("Invalid move!")
            
    def play(self):
        self.print_board()
        while True:
            try:
                row = int(input("Enter row number (0-2): "))
                col = int(input("Enter column number (0-2): "))
                self.mark_space(row, col)
                self.print_board()
            except ValueError:
                print("Invalid input, please enter a number.")
            

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
