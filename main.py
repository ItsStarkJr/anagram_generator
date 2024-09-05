import tkinter as tk
from tkinter import scrolledtext
import random
import string


# Function to perform ROT13 encoding/decoding
def rot13(text):
    rot13_translation = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:]
        + string.ascii_lowercase[:13]
        + string.ascii_uppercase[13:]
        + string.ascii_uppercase[:13],
    )
    return text.translate(rot13_translation)


# Function to create an anagram from the input words
def create_anagram(word1, word2, word3):
    combined = word1 + word2 + word3
    anagram = "".join(random.sample(combined, len(combined)))
    return anagram


# Function to center a window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    window.geometry(f"{width}x{height}+{position_right}+{position_top}")


# Function to show ROT13 result in a scrollable popup
def show_rot13_result():
    text = rot13_input.get()
    result = rot13(text)

    result_popup = tk.Toplevel(root)
    result_popup.title("ROT13 Result")
    result_popup.configure(bg=bg_color)
    center_window(result_popup, 900, 600)

    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()

    copy_button_top = tk.Button(
        result_popup,
        text="Copy to Clipboard",
        command=copy_to_clipboard,
        bg=button_color,
        fg=text_color,
    )
    copy_button_top.pack(pady=(10, 5))

    # Create a scrollable text area
    text_area = scrolledtext.ScrolledText(
        result_popup,
        wrap=tk.WORD,
        bg=bg_color,
        fg=text_color,
        insertbackground=text_color,
        width=80,
        height=20,
    )
    text_area.insert(tk.END, result)
    text_area.config(state=tk.DISABLED)
    text_area.pack(padx=10, pady=(5, 5))

    copy_button_bottom = tk.Button(
        result_popup,
        text="Copy to Clipboard",
        command=copy_to_clipboard,
        bg=button_color,
        fg=text_color,
    )
    copy_button_bottom.pack(pady=(5, 10))

    close_button = tk.Button(
        result_popup,
        text="Close",
        command=result_popup.destroy,
        bg=button_color,
        fg=text_color,
    )
    close_button.pack(pady=10)


# Function to show Anagram result in a scrollable popup
def show_anagram_result():
    word1 = anagram_input1.get()
    word2 = anagram_input2.get()
    word3 = anagram_input3.get()
    result = create_anagram(word1, word2, word3)

    result_popup = tk.Toplevel(root)
    result_popup.title("Anagram Result")
    result_popup.configure(bg=bg_color)
    center_window(result_popup, 900, 600)

    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()

    copy_button_top = tk.Button(
        result_popup,
        text="Copy to Clipboard",
        command=copy_to_clipboard,
        bg=button_color,
        fg=text_color,
    )
    copy_button_top.pack(pady=(10, 5))

    # Create a scrollable text area
    text_area = scrolledtext.ScrolledText(
        result_popup,
        wrap=tk.WORD,
        bg=bg_color,
        fg=text_color,
        insertbackground=text_color,
        width=80,
        height=20,
    )
    text_area.insert(tk.END, result)
    text_area.config(state=tk.DISABLED)
    text_area.pack(padx=10, pady=(5, 5))

    copy_button_bottom = tk.Button(
        result_popup,
        text="Copy to Clipboard",
        command=copy_to_clipboard,
        bg=button_color,
        fg=text_color,
    )
    copy_button_bottom.pack(pady=(5, 10))

    close_button = tk.Button(
        result_popup,
        text="Close",
        command=result_popup.destroy,
        bg=button_color,
        fg=text_color,
    )
    close_button.pack(pady=10)


# Function to navigate to the ROT13 page
def go_to_rot13():
    menu_frame.pack_forget()
    anagram_frame.pack_forget()
    rot13_frame.pack(fill=tk.BOTH, expand=True)


# Function to navigate to the Anagram page
def go_to_anagram():
    menu_frame.pack_forget()
    rot13_frame.pack_forget()
    anagram_frame.pack(fill=tk.BOTH, expand=True)


# Function to return to the main menu
def back_to_menu():
    rot13_frame.pack_forget()
    anagram_frame.pack_forget()
    menu_frame.pack(pady=20)


# Initialize main window
root = tk.Tk()
root.title("Text Transformer")

# Set the window size and center it on the screen
window_width = 1000
window_height = 700
center_window(root, window_width, window_height)

# Colors for the dark theme
bg_color = "#2e2e2e"
text_color = "#ffffff"
button_color = "#555555"

# Apply the dark theme
root.configure(bg=bg_color)

# Main Menu Frame
menu_frame = tk.Frame(root, bg=bg_color)
menu_label = tk.Label(
    menu_frame, text="Main Menu", font=("Arial", 16), fg=text_color, bg=bg_color
)
menu_label.pack(pady=10)

rot13_button = tk.Button(
    menu_frame,
    text="ROT13",
    command=go_to_rot13,
    width=20,
    bg=button_color,
    fg=text_color,
)
rot13_button.pack(pady=5)

anagram_button = tk.Button(
    menu_frame,
    text="Anagram",
    command=go_to_anagram,
    width=20,
    bg=button_color,
    fg=text_color,
)
anagram_button.pack(pady=5)

menu_frame.pack(pady=20)

# ROT13 Frame
rot13_frame = tk.Frame(root, bg=bg_color)

rot13_label = tk.Label(
    rot13_frame,
    text="Enter text for ROT13 encoding/decoding:",
    font=("Arial", 12),
    fg=text_color,
    bg=bg_color,
)
rot13_label.pack(pady=10)

rot13_input = tk.Entry(
    rot13_frame,
    width=int(window_width * 0.9 / 10),
    bg=button_color,
    fg=text_color,
    insertbackground=text_color,
)
rot13_input.pack(pady=5)

rot13_submit = tk.Button(
    rot13_frame,
    text="Submit",
    command=show_rot13_result,
    bg=button_color,
    fg=text_color,
)
rot13_submit.pack(pady=5)

rot13_back = tk.Button(
    rot13_frame,
    text="Back to Menu",
    command=back_to_menu,
    bg=button_color,
    fg=text_color,
)
rot13_back.pack(pady=5)

# Anagram Frame
anagram_frame = tk.Frame(root, bg=bg_color)

anagram_label = tk.Label(
    anagram_frame,
    text="Enter three words to create an anagram:",
    font=("Arial", 12),
    fg=text_color,
    bg=bg_color,
)
anagram_label.pack(pady=10)

anagram_input1 = tk.Entry(
    anagram_frame,
    width=int(window_width * 0.9 / 10),
    bg=button_color,
    fg=text_color,
    insertbackground=text_color,
)
anagram_input1.pack(pady=5)

anagram_input2 = tk.Entry(
    anagram_frame,
    width=int(window_width * 0.9 / 10),
    bg=button_color,
    fg=text_color,
    insertbackground=text_color,
)
anagram_input2.pack(pady=5)

anagram_input3 = tk.Entry(
    anagram_frame,
    width=int(window_width * 0.9 / 10),
    bg=button_color,
    fg=text_color,
    insertbackground=text_color,
)
anagram_input3.pack(pady=5)

anagram_submit = tk.Button(
    anagram_frame,
    text="Submit",
    command=show_anagram_result,
    bg=button_color,
    fg=text_color,
)
anagram_submit.pack(pady=5)

anagram_back = tk.Button(
    anagram_frame,
    text="Back to Menu",
    command=back_to_menu,
    bg=button_color,
    fg=text_color,
)
anagram_back.pack(pady=5)

# Start the main loop
root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# from settings import *


# class Interface:
#     def __init__(self) -> None:
#         self.setup()

#     def on_submit(self):
#         self.text_to_gram = self.entry_text_to_gram.get().strip()
#         num_words = self.entry_num_words.get().strip()
#         num_letters_per_word = self.entry_num_letters_per_word.get().strip()

#         # Check if "text to gram" is empty
#         if not self.text_to_gram:
#             messagebox.showerror("Error", "The 'text to gram' field is empty.")
#             return

#         # If "number of words" and "number of letters per word" are provided
#         if num_words.isdigit() and num_letters_per_word.isdigit():
#             num_words = int(num_words)
#             num_letters_per_word = int(num_letters_per_word)

#             # Calculate the total letters required
#             total_required_letters = num_words * num_letters_per_word

#             # Check if total letters match
#             if len(self.text_to_gram) != total_required_letters:
#                 messagebox.showerror(
#                     "Error",
#                     f"The total letters ({len(self.text_to_gram)}) "
#                     f"do not match the required total ({total_required_letters}).",
#                 )
#                 return

#         # If checks pass, show success message (or process further as needed)
#         messagebox.showinfo("Success", "All inputs are valid.")

#     def setup(self):

#         # Create the main window
#         self.root = tk.Tk()
#         self.root.title("Gram Checker")

#         # Set the window size and center it
#         self.window_width = WINDOW_WIDTH
#         self.window_height = WINDOW_HEIGHT
#         self.center_window(self.root)

#         # Colors
#         bg_color = BG_COLOR  # Background color
#         fg_color = FG_COLOR  # Text color
#         entry_bg_color = ENTRY_BG_COLOR  # Entry background color
#         self.root.configure(bg=bg_color)

#         # Bind the Escape key to the close_app function
#         self.root.bind("<Escape>", self.close_app)

#         # Create a frame to hold the widgets and center them vertically
#         frame = tk.Frame(self.root, bg=bg_color)
#         frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#         # Create the "Text to Gram" label and input box
#         label_text_to_gram = tk.Label(
#             frame, text="Text to Gram:", font=("Arial", 12), bg=bg_color, fg=fg_color
#         )
#         label_text_to_gram.pack(pady=10)
#         self.entry_text_to_gram = tk.Entry(
#             frame,
#             width=40,
#             font=("Arial", 12),
#             bg=entry_bg_color,
#             fg=fg_color,
#             insertbackground=fg_color,
#         )
#         self.entry_text_to_gram.pack(pady=10)

#         # Create the "Number of Words" label and input box
#         label_num_words = tk.Label(
#             frame,
#             text="Number of Words (optional):",
#             font=("Arial", 12),
#             bg=bg_color,
#             fg=fg_color,
#         )
#         label_num_words.pack(pady=10)
#         self.entry_num_words = tk.Entry(
#             frame,
#             width=40,
#             font=("Arial", 12),
#             bg=entry_bg_color,
#             fg=fg_color,
#             insertbackground=fg_color,
#         )
#         self.entry_num_words.pack(pady=10)

#         # Create the "Number of Letters per Word" label and input box
#         label_num_letters_per_word = tk.Label(
#             frame,
#             text="Number of Letters per Word (optional):",
#             font=("Arial", 12),
#             bg=bg_color,
#             fg=fg_color,
#         )
#         label_num_letters_per_word.pack(pady=10)
#         self.entry_num_letters_per_word = tk.Entry(
#             frame,
#             width=40,
#             font=("Arial", 12),
#             bg=entry_bg_color,
#             fg=fg_color,
#             insertbackground=fg_color,
#         )
#         self.entry_num_letters_per_word.pack(pady=10)

#         # Create the submit button
#         submit_button = tk.Button(
#             frame,
#             text="Submit",
#             command=self.on_submit,
#             font=("Arial", 12),
#             bg=entry_bg_color,
#             fg=fg_color,
#             width=20,
#         )
#         submit_button.pack(pady=20)

#     def run(self):
#         self.root.mainloop()

#     def close_app(self, event=None):
#         self.root.destroy()  # Closes the Tkinter window


# interface = Interface()
# interface.run()
