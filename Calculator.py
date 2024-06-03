from tkinter import *
import tkinter as tk
from tkinter import ttk

def button_click(number):
    if number == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
    else:
        current = entry.get()
        entry.delete(0, END)
        entry.insert(END, str(current) + str(number))

window = Tk()
window.title("Calculator")
window.geometry("350x400")
window.configure(bg="lightblue")

style = ttk.Style()
entry = tk.Entry(window, width=54, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

buttons = [
    ("9", 1, 0), ("8", 1, 1), ("7", 1, 2),
    ("6", 2, 0), ("5", 2, 1), ("4", 2, 2),
    ("3", 3, 0), ("2", 3, 1), ("1", 3, 2),
    ("0", 4, 0), ("*", 4, 1), ("/", 4, 2),
    ("C", 1, 3), ("+", 2, 3), ("-", 3, 3), ("=", 4, 3)
]

for (text, row, col) in buttons:
    btn = ttk.Button(window, text=text, padding=5, style='ShadowButton.TButton', command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=2, pady=3)

window.mainloop()
