import tkinter as tk

# Function to update the expression in the text entry field
def click_button(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + value)

# Function to clear the expression
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the input field where the user will see the expression
entry = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons and add them to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=evaluate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: click_button(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the Tkinter event loop
root.mainloop()
