import tkinter as tk
from utils import on_screen_close
from settings import *


class ScreenSwitcherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("damn")
        self.set_window_parameters()
        self.set_colors_and_fonts()
        self.root.bind("<Escape>", self.close_app)

        self.setup_menu_window()

        # Instance variables to hold references to the windows
        self.screen1_window = None
        self.screen2_window = None

    def setup_menu_window(self):

        # Main Menu Label
        self.main_label = tk.Label(
            self.root, text="Main Menu", font=("Arial", 16), fg=FG_COLOR, bg=BG_COLOR
        )
        self.main_label.pack(pady=20)

        # Buttons to open screens
        self.button_screen1 = tk.Button(
            self.root,
            text="Anagrams",
            command=self.open_screen1,
            width=BUTTON_WIDTH,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            font=BUTTON_FONT,
        )
        self.button_screen1.pack(pady=4)

        self.button_screen2 = tk.Button(
            self.root,
            text="Rot13",
            width=BUTTON_WIDTH,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            font=BUTTON_FONT,
            command=self.open_screen2,
        )
        self.button_screen2.pack(pady=4)

    def set_window_parameters(self):
        # Fixed positions and sizes
        self.main_window_position = APP_POS
        self.window_size = MENU_WINDOW_SIZE  # Size for the main window

        self.screen1_position = MAIN_WINDOW_POS
        self.screen2_position = MAIN_WINDOW_POS
        self.screen_size = MAIN_WINDOW_SIZE  # Size for additional screens

        # Set the main window size and position
        self.set_window_geometry(self.root, self.main_window_position, self.window_size)

    def set_colors_and_fonts(self):
        self.bg_color = BG_COLOR  # Background color
        fg_color = FG_COLOR  # Text color
        entry_bg_color = ENTRY_BG_COLOR  # Entry background color
        self.root.configure(bg=self.bg_color)

    # Utility method to set window geometry
    def set_window_geometry(self, window, position, size):
        x, y = position
        width, height = size
        window.geometry(f"{width}x{height}+{x}+{y}")

    # Method to open Screen 1 and close Screen 2 if it's open
    def open_screen1(self):
        if self.screen2_window is not None:
            self.screen2_window.destroy()
            self.screen2_window = None

        if self.screen1_window is None:
            self.screen1_window = tk.Toplevel(self.root)
            self.screen1_window.title("Screen 1")
            self.screen1_window.configure(bg=self.bg_color)

            self.set_window_geometry(
                self.screen1_window, self.screen1_position, self.screen_size
            )

            label = tk.Label(
                self.screen1_window, text="This is Screen 1", font=("Arial", 18)
            )
            label.pack(pady=20)

            close_button = tk.Button(
                self.screen1_window, text="Close", command=self.screen1_window.destroy
            )
            close_button.pack(pady=10)

            # Handle window close event
            self.screen1_window.protocol(
                "WM_DELETE_WINDOW", lambda: on_screen_close(self.screen1_window)
            )

    # Method to open Screen 2 and close Screen 1 if it's open
    def open_screen2(self):
        if self.screen1_window is not None:
            self.screen1_window.destroy()
            self.screen1_window = None

        if self.screen2_window is None:
            self.screen2_window = tk.Toplevel(self.root)
            self.screen2_window.title("Screen 2")
            self.screen2_window.configure(bg=self.bg_color)
            self.set_window_geometry(
                self.screen2_window, self.screen2_position, self.screen_size
            )

            label = tk.Label(
                self.screen2_window, text="This is Screen 2", font=("Arial", 18)
            )
            label.pack(pady=20)

            close_button = tk.Button(
                self.screen2_window, text="Close", command=self.screen2_window.destroy
            )
            close_button.pack(pady=10)

            # Handle window close event
            self.screen2_window.protocol(
                "WM_DELETE_WINDOW", lambda: on_screen_close(self.screen2_window)
            )

    def close_app(self, event=None):
        """Closes windows if open, closes app if not."""
        if self.screen2_window is not None:
            self.screen2_window.destroy()
            self.screen2_window = None
        elif self.screen1_window is not None:
            self.screen1_window.destroy()
            self.screen1_window = None
        else:
            self.root.destroy()

    def run(self):
        self.root.mainloop()


# Main application loop
if __name__ == "__main__":

    app = ScreenSwitcherApp()
    app.run()
