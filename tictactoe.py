import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe Game")
root.resizable(False, False)

# Game variables
current_player = "X"
board = [""] * 9

# Functions
def check_winner():
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for w in wins:
        a, b, c = w
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def button_click(i):
    global current_player

    if board[i] == "":
        board[i] = current_player
        buttons[i].config(text=current_player, state="disabled")

        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} Wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for b in buttons:
        b.config(text="", state="normal")

# Create buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Run the application
root.mainloop()
