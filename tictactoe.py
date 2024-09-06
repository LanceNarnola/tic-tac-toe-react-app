import tkinter as tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
import random

window = tk.Tk()
window.geometry("200x250")
window.title("Tic Tac Toe")

frame1 = Frame(window)
frame1.pack()

# Title label
titleLabel = Label(frame1, text="Tic Tac Toe")
titleLabel.config(fg="red")
titleLabel.pack()

# Turn label
turnLabel = Label(frame1, text="Player 1's turn")
turnLabel.config(fg="blue")
turnLabel.pack()

# Restarting the game
playAgainButton = Button(frame1, text="Play Again", command=lambda: reset_game())
playAgainButton.pack(pady=10)

frame2 = Frame(window)
frame2.pack()

# User prompt
turn = "x"
buttons = [[None]*3 for _ in range(3)]

def check_winner():
    # Check rows
    if (buttons[0][0]["text"] == buttons[0][1]["text"] == buttons[0][2]["text"] and buttons[0][0]["text"] != ""):
        return buttons[0][0]["text"]
    if (buttons[1][0]["text"] == buttons[1][1]["text"] == buttons[1][2]["text"] and buttons[1][0]["text"] != ""):
        return buttons[1][0]["text"]
    if (buttons[2][0]["text"] == buttons[2][1]["text"] == buttons[2][2]["text"] and buttons[2][0]["text"] != ""):
        return buttons[2][0]["text"]
    
    # Check columns
    if (buttons[0][0]["text"] == buttons[1][0]["text"] == buttons[2][0]["text"] and buttons[0][0]["text"] != ""):
        return buttons[0][0]["text"]
    if (buttons[0][1]["text"] == buttons[1][1]["text"] == buttons[2][1]["text"] and buttons[0][1]["text"] != ""):
        return buttons[0][1]["text"]
    if (buttons[0][2]["text"] == buttons[1][2]["text"] == buttons[2][2]["text"] and buttons[0][2]["text"] != ""):
        return buttons[0][2]["text"]
    
    # Check diagonals
    if (buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] and buttons[0][0]["text"] != ""):
        return buttons[0][0]["text"]
    if (buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] and buttons[0][2]["text"] != ""):
        return buttons[0][2]["text"]
    
    return None

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state="disabled")

def reset_game():
    global turn
    # Reset the game state
    turn = "x"  # Player 1 always starts
    turnLabel.config(text="Player 1's turn")
    titleLabel.config(text="Tic Tac Toe")
    
    for row in buttons:
        for button in row:
            button.config(text="", state="normal")

def play(event):
    global turn
    button = event.widget
    
    if button["text"] == "" and not check_winner():
        button["text"] = "X" if turn == "x" else "O"
        winner = check_winner()
        if winner:
            titleLabel.config(text=f"Player {'1' if winner == 'X' else '2'} wins!")
            disable_buttons()
        else:
            turn = "o" if turn == "x" else "x"
            turnLabel.config(text=f"Player {'2' if turn == 'o' else '1'}'s turn")

# Create buttons and place them in the grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame2, text="", width=4, height=2, font=("Arial", 10))
        buttons[i][j].grid(row=i, column=j)
        buttons[i][j].bind("<Button-1>", play)

reset_game()
window.mainloop()