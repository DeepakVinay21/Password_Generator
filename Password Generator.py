# 💡 [RYFT REVIEW - SUGGESTION] Shebang line is not necessary for Python scripts, consider removing it.
#!/usr/bin/env python
# coding: utf-8

# 💡 [RYFT REVIEW - SUGGESTION] Docstring is missing a period at the end.
"""
TASK 3: Password Generator GUI using Tkinter
This application generates a secure password based on the length
entered by the user.
"""

# 💡 [RYFT REVIEW - SUGGESTION] Consider using `import tkinter as tk` instead of `import tkinter`.
import tkinter as tk
import string
import secrets


# 💡 [RYFT REVIEW - SUGGESTION] Function name `show_message` is not descriptive, consider renaming it.
def show_message(message, color):
    status_label.config(text=message, fg=color)


def generate_password():
# ⚠️ [RYFT REVIEW - WARNING] Consider adding a check for `username_entry` being `None` before calling `get()`.
    username = username_entry.get().strip()
# ⚠️ [RYFT REVIEW - WARNING] Consider adding a check for `length_entry` being `None` before calling `get()`.
    length_str = length_entry.get().strip()

    if not username:
        show_message("Please enter the user name first", "red")
        return

# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more specific error message instead of just 'red'.
    if not length_str.isdigit():
        show_message("Password length must be a number", "red")
        return

# 💡 [RYFT REVIEW - SUGGESTION] Consider adding a check for `length` being less than 1 instead of just 4.
    length = int(length_str)

    if length < 4:
        show_message("Password length must be at least 4", "red")
        return

# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more descriptive variable name instead of `characters`.
    characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more descriptive variable name instead of `password_chars`.
    password_chars = [secrets.choice(characters) for _ in range(length)]
    generated_password = "".join(password_chars)

# 💡 [RYFT REVIEW - SUGGESTION] Consider using `password_entry.delete(0, tk.END)` instead of just `password_entry.delete(0, tk.END)`.
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

    show_message("Password generated successfully!", "green")


# 💡 [RYFT REVIEW - SUGGESTION] Function name `clear_all` is not descriptive, consider renaming it.
def clear_all():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    show_message("", "black")


# 💡 [RYFT REVIEW - SUGGESTION] Function name `reset_password` is not descriptive, consider renaming it.
def reset_password():
    password_entry.delete(0, tk.END)
    show_message("", "black")


# GUI Window
# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more descriptive variable name instead of `window`.
window = tk.Tk()
window.title("Password Generator")

# Title
# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more descriptive variable name instead of `title`.
tk.Label(
    window,
    text="Password Generator",
    font=("Times", 20, "underline"),
    fg="Green"
).grid(row=0, column=0, columnspan=2)

# Username
tk.Label(window, text="Enter user name:", font=("Times", 20)).grid(row=1, column=0, pady=20)
# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more descriptive variable name instead of `username_entry`.
username_entry = tk.Entry(window, width=20, font=("Times", 20))
username_entry.grid(row=1, column=1, pady=20)

# Password Length
tk.Label(window, text="Enter Password length:", font=("Times", 20)).grid(row=2, column=0, pady=15)
length_entry = tk.Entry(window, width=20, font=("Times", 20))
# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more descriptive variable name instead of `length_entry`.
length_entry.grid(row=2, column=1, pady=15)

# Generated Password
tk.Label(window, text="Generated Password:", font=("Times", 20)).grid(row=3, column=0, pady=15)
# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more descriptive variable name instead of `password_entry`.
password_entry = tk.Entry(window, width=20, font=("Times", 20))
password_entry.grid(row=3, column=1, pady=15)

# Buttons
tk.Button(
    window,
    text="GENERATE PASSWORD",
    bg="Blue",
    fg="white",
    command=generate_password
).grid(row=4, column=1, pady=15)

tk.Button(
    window,
    text="ACCEPT",
    fg="Blue",
    command=clear_all
).grid(row=5, column=1, pady=5)

tk.Button(
    window,
    text="RESET",
    fg="Blue",
    command=reset_password
).grid(row=6, column=1, pady=5)

# Status Label
# 💡 [RYFT REVIEW - SUGGESTION] Consider using a more descriptive variable name instead of `status_label`.
status_label = tk.Label(window, text="", font=("Times", 10))
status_label.grid(row=7, column=0, columnspan=2)

window.mainloop()
