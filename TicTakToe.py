import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - 1 Player")
        
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Player is X
        self.computer_player = "O"  # Computer is O
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        
        self.window.mainloop()

    def create_board(self):
        """Creates the Tic Tac Toe board."""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.window, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        """Handles player moves."""
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            winner = self.check_winner()
            
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = self.computer_player
                self.computer_move()

    def computer_move(self):
        """Makes a move for the computer (randomly selects an empty spot)."""
        empty_spots = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        
        if empty_spots:
            row, col = random.choice(empty_spots)
            self.board[row][col] = self.computer_player
            self.buttons[row][col].config(text=self.computer_player)
            winner = self.check_winner()
            
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "X"  # Switch back to player after computer move

    def check_winner(self):
        """Checks if there's a winner."""
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        
        return None

    def is_draw(self):
        """Checks if the game is a draw."""
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_board(self):
        """Resets the game board."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

# Run the game
TicTacToe()
