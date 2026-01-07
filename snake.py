import tkinter as tk
import random
from tkinter import messagebox

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        self.mode = "Medium"
        self.game_running = False

        # Main menu
        self.show_main_menu()

    def show_main_menu(self):
        # Main menu
        self.menu_frame = tk.Frame(self.master, bg="saddle brown")
        self.menu_frame.pack(fill="both", expand=True)

        # Title
        title_label = tk.Label(self.menu_frame, text="Snake Game", font=("Cooper Black", 26), fg="lemon chiffon", bg="saddle brown")
        title_label.pack(pady=20)

        # Create a frame for the difficulty buttons to align them horizontally
        difficulty_frame = tk.Frame(self.menu_frame, bg="saddle brown")
        difficulty_frame.pack(pady=10)

        # Difficulty buttons (on the same line)
        button_style = {"font": ("Courier New", 20), "bg": "lemon chiffon", "fg": "saddle brown", "relief": "raised", "bd": 2}
        tk.Button(difficulty_frame, text="Easy", command=lambda: self.set_mode("Easy"), **button_style).pack(side="left", padx=10)
        tk.Button(difficulty_frame, text="Medium", command=lambda: self.set_mode("Medium"), **button_style).pack(side="left", padx=10)
        tk.Button(difficulty_frame, text="Hard", command=lambda: self.set_mode("Hard"), **button_style).pack(side="left", padx=10)

        # Start button
        tk.Button(self.menu_frame, text="Start Game", command=self.start_game, **button_style).pack(pady=20)

        # Quit button
        tk.Button(self.menu_frame, text="Return", command=self.master.quit, **button_style).pack(pady=10)

    def set_mode(self, mode):
        self.mode = mode

    def start_game(self):
        self.menu_frame.destroy()
        self.init_game()

    def init_game(self):
        # Make canvas cover the screen except the bottom panel
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Define the panel height and available canvas height
        panel_height = 40
        canvas_height = screen_height - panel_height

        self.canvas = tk.Canvas(self.master, width=screen_width, height=canvas_height, bg='lemon chiffon')
        self.canvas.pack(fill="both", expand=True)

        self.snake = [[screen_width // 2, canvas_height // 2]]  # Initial snake position
        self.food = []
        self.direction = "Right"
        self.running = True
        self.score = 0  # Initialize the score

        self.speed = {"Easy": 150, "Medium": 100, "Hard": 50}[self.mode]

        self.create_food()
        self.update_snake()
        self.master.bind("<KeyPress>", self.change_direction)

        # Panel at the bottom with score and quit button
        self.panel_frame = tk.Frame(self.master, bg="saddle brown", height=panel_height)
        self.panel_frame.pack(side="bottom", fill="x")

        # Score label
        self.score_label = tk.Label(self.panel_frame, text=f"Score: {self.score}", font=("Arial", 14), fg="lemon chiffon", bg="saddle brown")
        self.score_label.pack(side="left", padx=10)

        # Quit button with confirmation
        tk.Button(self.panel_frame, text="Quit", command=self.confirm_quit, font=("Arial", 14), bg="red", fg="white").pack(side="right", padx=10)

    def create_food(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        if not self.food:
            while True:
                x = random.randint(0, (screen_width // 20) - 1) * 15
                y = random.randint(0, (screen_height // 20) - 1) * 15
                if [x, y] not in self.snake:  # Ensure food doesn't spawn on the snake
                    self.food = [x, y]
                    self.canvas.create_oval(x, y, x + 20, y + 20, fill="sienna2", tag="food")
                    break

    def update_snake(self):
        if not self.running:
            return

        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= 20
        elif self.direction == "Down":
            head_y += 20
        elif self.direction == "Left":
            head_x -= 20
        elif self.direction == "Right":
            head_x += 20

        # Wrap the snake around the edges of the screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        head_x %= screen_width
        head_y %= screen_height

        new_head = [head_x, head_y]

        if new_head in self.snake:  # Collides with itself
            self.game_over()
            return

        self.snake.insert(0, new_head)

        food_x, food_y = self.food
        if abs(new_head[0] - food_x) < 20 and abs(new_head[1] - food_y) < 20:  # Check proximity to food
            self.food = []
            self.canvas.delete("food")
            self.create_food()
            self.score += 1  # Increase score when food is eaten
            self.score_label.config(text=f"Score: {self.score}")  # Update score label
        else:
            self.snake.pop()

        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="saddle brown", tag="snake")

        self.master.after(self.speed, self.update_snake)

    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = {"Up", "Down", "Left", "Right"}
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}

        if new_direction in all_directions and new_direction != opposites[self.direction]:
            self.direction = new_direction

    def game_over(self):
        self.running = False
        self.canvas.delete("all")
        self.canvas.create_text(
            self.master.winfo_screenwidth() // 2,
            self.master.winfo_screenheight() // 2 - 50,
            text="Game Over", fill="white", font=("Arial", 36)
        )
        self.canvas.create_text(
            self.master.winfo_screenwidth() // 2,
            self.master.winfo_screenheight() // 2 + 50,
            text=f"Final Score: {self.score}", fill="black", font=("Arial", 24)
        )
        

    def confirm_quit(self):
        # Show a confirmation dialog before quitting
        if messagebox.askyesno("Quit Game", f"Are you sure you want to quit? \nYour current score is {self.score}."):
            self.panel_frame.destroy()  # Remove the current game panel
            self.canvas.destroy()  # Remove the game canvas
            self.show_main_menu()


def main():
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Make the window fullscreen
    SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
