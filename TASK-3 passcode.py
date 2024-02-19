import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return
    
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label and entry to display generated password
password_label = tk.Label(root, text="Generated Password:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Start the application
root.mainloop()
