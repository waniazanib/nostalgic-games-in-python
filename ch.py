import tkinter as tk
import chess
import chess.engine
from tkinter import messagebox

class ChessApp:

    def __init__(self, root):
        self.root = root
        self.board = chess.Board()
        self.engine = None  # Engine will be initialized only for computer games

        self.captured_white = []
        self.captured_black = []

        # Show the main menu on initialization
        self.create_main_menu()

    def create_main_menu(self):
        self.menu_frame = tk.Frame(self.root, bg="saddle brown")
        self.menu_frame.pack(fill="both", expand=True)

        # Set the root window to fullscreen
        self.root.attributes("-fullscreen", True)

        tk.Label(
            self.menu_frame, text="Chess Game", font=("Cooper Black", 30), fg="lemon chiffon", bg="saddle brown"
        ).pack(pady=50)

        tk.Button(
            self.menu_frame, text="Play Against Computer", font=("Courier New", 20), bg="lemon chiffon", fg="saddle brown",
            command=lambda: self.start_game_menu(True)
        ).pack(pady=20)

        tk.Button(
            self.menu_frame, text="Two Player Game", font=("Courier New", 20), bg="lemon chiffon", fg="saddle brown",
            command=lambda: self.start_game_menu(False)
        ).pack(pady=20)

        tk.Button(
            self.menu_frame, text="Quit", font=("Courier New", 20), bg="lemon chiffon", fg="saddle brown",
            command=self.root.quit
        ).pack(pady=20)

    def start_game_menu(self, against_computer):
        self.against_computer = against_computer

        # Reset the board and captured pieces
        self.board = chess.Board()
        self.captured_white = []
        self.captured_black = []

        # Destroy the main menu frame
        self.menu_frame.destroy()

        # Initialize the chess engine if playing against the computer
        if self.against_computer:
            self.engine = chess.engine.SimpleEngine.popen_uci(
                "D:/downloads/SF/stockfish/stockfish-windows-x86-64-avx2.exe"
            )

        # Set up the game UI
        self.init_ui()

    def init_ui(self):
        self.root.attributes("-fullscreen", True)
        self.root.title("Chess Game")

        self.frame = tk.Frame(self.root, bg="sienna3")
        self.frame.pack(fill="both", expand=True)

        # Left panel for captured black pieces
        self.left_panel = tk.Frame(self.frame, width=360, height=640, bg="sienna3")
        self.left_panel.grid(row=0, column=0, sticky="ns")
        self.left_panel.pack_propagate(False)

        # Canvas for the chessboard
        self.canvas = tk.Canvas(self.frame, width=640, height=640, bg="white")
        self.canvas.grid(row=0, column=1)
        self.canvas.bind("<Button-1>", self.on_click)

        # Right panel for captured white pieces
        self.right_panel = tk.Frame(self.frame, width=360, height=640, bg="sienna3")
        self.right_panel.grid(row=0, column=2, sticky="ns")
        self.right_panel.pack_propagate(False)

        # Quit button
        self.quit_button = tk.Button(
            self.root, text="QUIT", font=("Arial", 16), bg="saddle brown", fg="white", command=self.confirm_quit
        )
        self.quit_button.pack(side="bottom", pady=10)

        self.selected_square = None
        self.square_size = 80  # Default size
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")

        for row in range(8):
            for col in range(8):
                color = "lemon chiffon" if (row + col) % 2 == 0 else "saddle brown"
                x0 = col * self.square_size
                y0 = row * self.square_size
                x1 = x0 + self.square_size
                y1 = y0 + self.square_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        for square, piece in self.board.piece_map().items():
            col, row = chess.square_file(square), chess.square_rank(square)
            x = col * self.square_size + self.square_size // 2
            y = (7 - row) * self.square_size + self.square_size // 2
            piece_color = "black" if piece.color == chess.BLACK else "darkred"
            self.canvas.create_text(x, y, text=piece.symbol(), font=("Arial", self.square_size // 2), fill=piece_color)

        self.update_captured_pieces()

    def on_click(self, event):
        col = event.x // self.square_size
        row = event.y // self.square_size
        square = chess.square(col, 7 - row)

        if self.selected_square is None:
            if self.board.piece_at(square) and self.board.color_at(square) == self.board.turn:
                self.selected_square = square
                self.show_available_moves(square)
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                captured_piece = self.board.piece_at(square)
                if captured_piece:
                    if captured_piece.color == chess.WHITE:
                        self.captured_white.append(captured_piece.symbol())
                    else:
                        self.captured_black.append(captured_piece.symbol())
                self.board.push(move)
                if self.against_computer and not self.board.is_game_over():
                    self.play_computer_move()
            self.selected_square = None
            self.draw_board()

    def show_available_moves(self, square):
        for move in self.board.legal_moves:
            if move.from_square == square:
                col, row = chess.square_file(move.to_square), chess.square_rank(move.to_square)
                x0 = col * self.square_size
                y0 = (7 - row) * self.square_size
                x1 = x0 + self.square_size
                y1 = y0 + self.square_size
                self.canvas.create_oval(
                    x0 + self.square_size // 4, y0 + self.square_size // 4,
                    x1 - self.square_size // 4, y1 - self.square_size // 4,
                    fill="green", outline=""
                )

    def play_computer_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=1))
        captured_piece = self.board.piece_at(result.move.to_square)
        if captured_piece:
            if captured_piece.color == chess.WHITE:
                self.captured_white.append(captured_piece.symbol())
            else:
                self.captured_black.append(captured_piece.symbol())
        self.board.push(result.move)
        self.draw_board()

    def update_captured_pieces(self):
        for widget in self.left_panel.winfo_children():
            widget.destroy()

        for widget in self.right_panel.winfo_children():
            widget.destroy()

        for piece in self.captured_black:
            tk.Label(self.left_panel, text=piece, font=("Arial", 16), bg="sienna3", fg="black").pack()

        for piece in self.captured_white:
            tk.Label(self.right_panel, text=piece, font=("Arial", 16), bg="sienna3", fg="darkred").pack()

    def confirm_quit(self):
        response = messagebox.askyesno("Quit Game", "Do you want to quit the game?")
        if response:
            if self.engine:
                self.engine.quit()
            self.quit_button.destroy()
            self.frame.destroy()
            self.create_main_menu()

    def __del__(self):
        if self.engine:
            self.engine.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    app = ChessApp(root)
    root.mainloop()
