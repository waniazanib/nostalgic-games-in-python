import tkinter as tk
from tkinter import messagebox
import random

# Colors
BG_COLOR = "saddle brown"
BUTTON_COLOR = "lemon chiffon"
HIGHLIGHT_COLOR = "sienna2"

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.set_fullscreen()

        self.mode = None
        self.board = ["" for _ in range(9)]
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0}

        self.main_menu()

    def set_fullscreen(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.configure(bg=BG_COLOR)

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Tic Tac Toe", font=("Cooper Black", 26), fg=BUTTON_COLOR, bg=BG_COLOR).pack(pady=50)

        tk.Button(frame, text="Play Against Computer", font=("Courier New", 20), bg=BUTTON_COLOR, fg=BG_COLOR, 
                  command=lambda: self.start_game("computer")).pack(pady=20, ipadx=20, ipady=10)

        tk.Button(frame, text="Two Player Game", font=("Courier New", 20), bg=BUTTON_COLOR, fg=BG_COLOR, 
                  command=lambda: self.start_game("two_player")).pack(pady=20, ipadx=20, ipady=10)

        tk.Button(frame, text="Quit", font=("Courier New", 20), bg=BUTTON_COLOR, fg=BG_COLOR, 
                  command=self.root.destroy).pack(pady=20, ipadx=20, ipady=10)

    def start_game(self, mode):
        self.mode = mode
        self.board = ["" for _ in range(9)]
        self.current_player = "X"

        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_board()

    def create_board(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        panel_height = 50
        canvas_height = screen_height - panel_height

        self.canvas = tk.Canvas(self.root, width=screen_width, height=canvas_height, bg="lemon chiffon")
        self.canvas.pack(fill="both", expand=True)

        self.buttons = []
        button_size = min(canvas_height, screen_width) // 3
        x_offset = (screen_width - 3 * button_size) // 2
        y_offset = (canvas_height - 3 * button_size) // 2

        for row in range(3):
            for col in range(3):
                x1 = col * button_size + x_offset
                y1 = row * button_size + y_offset
                x2 = x1 + button_size
                y2 = y1 + button_size

                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="saddle brown", outline="black")
                text = self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text="", font=("Courier New", 36), fill=BUTTON_COLOR)

                self.buttons.append((rect, text))
                self.canvas.tag_bind(rect, "<Button-1>", lambda event, r=row, c=col: self.make_move(r, c))
                self.canvas.tag_bind(text, "<Button-1>", lambda event, r=row, c=col: self.make_move(r, c))

        self.panel_frame = tk.Frame(self.root, bg=BG_COLOR, height=panel_height)
        self.panel_frame.pack(side="bottom", fill="x")

        self.turn_label = tk.Label(self.panel_frame, text=f"Turn: {self.current_player}", font=("Arial", 14), fg=BUTTON_COLOR, bg=BG_COLOR)
        self.turn_label.pack(side="left", padx=10)

        self.score_label = tk.Label(self.panel_frame, text=f"X: {self.scores['X']} | O: {self.scores['O']}", font=("Arial", 14), fg=BUTTON_COLOR, bg=BG_COLOR)
        self.score_label.pack(side="right", padx=10)

        tk.Button(self.panel_frame, text="Restart", command=lambda: self.start_game(self.mode), font=("Arial", 14), bg="green", fg="white").pack(side="right", padx=10)

        tk.Button(self.panel_frame, text="Quit", command=self.main_menu, font=("Arial", 14), bg="red", fg="white").pack(side="right", padx=10)

    def make_move(self, row, col):
        index = row * 3 + col

        if self.board[index] == "":
            self.board[index] = self.current_player
            rect, text = self.buttons[index]
            self.canvas.itemconfig(text, text=self.current_player)

            if self.check_winner():
                self.scores[self.current_player] += 1
                self.highlight_winner()
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.start_game(self.mode)
                return

            if "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.start_game(self.mode)
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.turn_label.config(text=f"Turn: {self.current_player}")

            if self.mode == "computer" and self.current_player == "O":
                self.root.after(500, self.computer_move)

    def computer_move(self):
        best_score = float("-inf")
        best_move = None

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(False)
                self.board[i] = ""

                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            row, col = divmod(best_move, 3)
            self.make_move(row, col)

    def minimax(self, is_maximizing):
        if self.check_winner(True):
            return 1 if self.current_player == "O" else -1

        if "" not in self.board:
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "O"
                    score = self.minimax(False)
                    self.board[i] = ""
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "X"
                    score = self.minimax(True)
                    self.board[i] = ""
                    best_score = min(best_score, score)
            return best_score

    def check_winner(self, simulate=False):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                if not simulate:
                    self.winning_combo = combo
                return True

        return False

    def highlight_winner(self):
        for index in self.winning_combo:
            rect, text = self.buttons[index]
            self.canvas.itemconfig(rect, fill="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
