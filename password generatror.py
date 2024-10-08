import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_var.get()
    include_upper = upper_var.get()
    include_numbers = numbers_var.get()
    include_special = special_var.get()

    if length < 6:
        messagebox.showwarning("Warning", "Password length should be at least 6 characters.")
        return

    characters = string.ascii_lowercase  # Lowercase letters by default

    if include_upper:
        characters += string.ascii_uppercase  # Add uppercase letters if selected
    if include_numbers:
        characters += string.digits  # Add numbers if selected
    if include_special:
        characters += string.punctuation  # Add special characters if selected

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Variables for user input
length_var = tk.IntVar(value=8)
upper_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()
password_var = tk.StringVar()

# Create and arrange widgets
tk.Label(root, text="Password Length:").pack(pady=5)
tk.Entry(root, textvariable=length_var, width=5).pack()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

tk.Entry(root, textvariable=password_var, state='readonly', width=40).pack(pady=5)

tk.Button
