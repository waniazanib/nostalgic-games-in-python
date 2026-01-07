import tkinter as tk
import subprocess
import sys

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Hub")
        self.root.attributes("-fullscreen", True)
        self.create_main_menu()

    def create_main_menu(self):
        frame = tk.Frame(self.root, bg="saddle brown")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Game Hub", font=("Cooper Black", 36), fg="lemon chiffon", bg="saddle brown").pack(pady=50)

        button_style = {
            "font": ("Courier New", 20),
            "bg": "lemon chiffon",
            "fg": "saddle brown",
            "activebackground": "sienna2",
            "relief": "raised",
        }

        tk.Button(frame, text="Snake Game", command=self.launch_snake, **button_style).pack(pady=20, ipadx=20, ipady=10)
        tk.Button(frame, text="Tic Tac Toe", command=self.launch_tic, **button_style).pack(pady=20, ipadx=20, ipady=10)
        tk.Button(frame, text="Chess Game", command=self.launch_chess, **button_style).pack(pady=20, ipadx=20, ipady=10)
        tk.Button(frame, text="Quit", command=self.quit_app, **button_style).pack(pady=20, ipadx=20, ipady=10)

    def launch_snake(self):
        self.launch_game("snake.py")

    def launch_tic(self):
        self.launch_game("tic.py")

    def launch_chess(self):
        self.launch_game("ch.py")

    def launch_game(self, script_name):
        self.root.destroy()  # Close the main menu window
        subprocess.run([sys.executable, script_name])  # Launch the game script
        self.restart_menu()  # Restart the menu after exiting the game

    def restart_menu(self):
        new_root = tk.Tk()
        MainMenu(new_root)
        new_root.mainloop()

    def quit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    MainMenu(root)
    root.mainloop()
