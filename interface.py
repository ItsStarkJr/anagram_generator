import tkinter as tk
from tkinter import messagebox
from settings import *


class Interface:
    def __init__(self) -> None:
        self.setup()

    def setup(self):

        # Set the window size and center it
        self.window_width = WINDOW_WIDTH
        self.window_height = WINDOW_HEIGHT
        self.center_window(self.root)

        # Colors
        bg_color = BG_COLOR  # Background color
        fg_color = FG_COLOR  # Text color
        entry_bg_color = ENTRY_BG_COLOR  # Entry background color
        self.root.configure(bg=bg_color)

        # Bind the Escape key to the close_app function
        self.root.bind("<Escape>", self.close_app)

        # Create a frame to hold the widgets and center them vertically
        frame = tk.Frame(self.root, bg=bg_color)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create the "Text to Gram" label and input box
        label_text_to_gram = tk.Label(
            frame, text="Text to Gram:", font=("Arial", 12), bg=bg_color, fg=fg_color
        )
        label_text_to_gram.pack(pady=10)
        self.entry_text_to_gram = tk.Entry(
            frame,
            width=40,
            font=("Arial", 12),
            bg=entry_bg_color,
            fg=fg_color,
            insertbackground=fg_color,
        )
        self.entry_text_to_gram.pack(pady=10)

        # Create the "Number of Words" label and input box
        label_num_words = tk.Label(
            frame,
            text="Number of Words (optional):",
            font=("Arial", 12),
            bg=bg_color,
            fg=fg_color,
        )
        label_num_words.pack(pady=10)
        self.entry_num_words = tk.Entry(
            frame,
            width=40,
            font=("Arial", 12),
            bg=entry_bg_color,
            fg=fg_color,
            insertbackground=fg_color,
        )
        self.entry_num_words.pack(pady=10)

        # Create the "Number of Letters per Word" label and input box
        label_num_letters_per_word = tk.Label(
            frame,
            text="Number of Letters per Word (optional):",
            font=("Arial", 12),
            bg=bg_color,
            fg=fg_color,
        )
        label_num_letters_per_word.pack(pady=10)
        self.entry_num_letters_per_word = tk.Entry(
            frame,
            width=40,
            font=("Arial", 12),
            bg=entry_bg_color,
            fg=fg_color,
            insertbackground=fg_color,
        )
        self.entry_num_letters_per_word.pack(pady=10)

        # Create the submit button
        submit_button = tk.Button(
            frame,
            text="Submit",
            command=self.on_submit,
            font=("Arial", 12),
            bg=entry_bg_color,
            fg=fg_color,
            width=20,
        )
        submit_button.pack(pady=20)


def on_submit(self):
    self.text_to_gram = self.entry_text_to_gram.get().strip()
    num_words = self.entry_num_words.get().strip()
    num_letters_per_word = self.entry_num_letters_per_word.get().strip()

    # Check if "text to gram" is empty
    if not self.text_to_gram:
        messagebox.showerror("Error", "The 'text to gram' field is empty.")
        return

    # If "number of words" and "number of letters per word" are provided
    if num_words.isdigit() and num_letters_per_word.isdigit():
        num_words = int(num_words)
        num_letters_per_word = int(num_letters_per_word)

        # Calculate the total letters required
        total_required_letters = num_words * num_letters_per_word

        # Check if total letters match
        if len(self.text_to_gram) != total_required_letters:
            messagebox.showerror(
                "Error",
                f"The total letters ({len(self.text_to_gram)}) "
                f"do not match the required total ({total_required_letters}).",
            )
            return

    # If checks pass, show success message (or process further as needed)
    messagebox.showinfo("Success", "All inputs are valid.")
