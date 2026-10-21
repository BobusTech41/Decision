import tkinter as tk
from tkinter import messagebox

def say_hello():
    name = entry.get()
    if name:
        label.config(text="Hello " + name)
    else:
        messagebox.showerror("Error", "Please enter a name")

root = tk.Tk()
root.title("Menu")
root.geometry("400x300")

label = tk.Label(root, text="Enter your name", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=25)
entry.pack(pady=40)

button = tk.Button(root, text="GREET", command=say_hello)
button.pack(pady=10)

root.mainloop()
