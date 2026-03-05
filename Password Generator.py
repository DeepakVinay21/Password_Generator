#!/usr/bin/env python
# coding: utf-8

"""
TASK 3: Password Generator GUI using Tkinter
This application generates a secure password based on the length
entered by the user.
"""

import tkinter as tk
import string
import secrets


def show_message(message, color):
    status_label.config(text=message, fg=color)


def generate_password():
    username = username_entry.get().strip()
    length_str = length_entry.get().strip()

    if not username:
        show_message("Please enter the user name first", "red")
        return

    if not length_str.isdigit():
        show_message("Password length must be a number", "red")
        return

    length = int(length_str)

    if length < 4:
        show_message("Password length must be at least 4", "red")
        return

    characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

    password_chars = [secrets.choice(characters) for _ in range(length)]
    generated_password = "".join(password_chars)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

    show_message("Password generated successfully!", "green")


def clear_all():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    show_message("", "black")


def reset_password():
    password_entry.delete(0, tk.END)
    show_message("", "black")


# GUI Window
window = tk.Tk()
window.title("Password Generator")

# Title
tk.Label(
    window,
    text="Password Generator",
    font=("Times", 20, "underline"),
    fg="Green"
).grid(row=0, column=0, columnspan=2)

# Username
tk.Label(window, text="Enter user name:", font=("Times", 20)).grid(row=1, column=0, pady=20)
username_entry = tk.Entry(window, width=20, font=("Times", 20))
username_entry.grid(row=1, column=1, pady=20)

# Password Length
tk.Label(window, text="Enter Password length:", font=("Times", 20)).grid(row=2, column=0, pady=15)
length_entry = tk.Entry(window, width=20, font=("Times", 20))
length_entry.grid(row=2, column=1, pady=15)

# Generated Password
tk.Label(window, text="Generated Password:", font=("Times", 20)).grid(row=3, column=0, pady=15)
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
status_label = tk.Label(window, text="", font=("Times", 10))
status_label.grid(row=7, column=0, columnspan=2)

window.mainloop()
