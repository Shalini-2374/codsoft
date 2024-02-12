import tkinter as tk

def on_click(event):
    current = result_var.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result_var.set(eval(current))
        except Exception as e:
            result_var.set("Error")
    elif text == "C":
        result_var.set("")
    else:
        result_var.set(current + text)

root = tk.Tk()
root.title("Simple Calculator")

result_var = tk.StringVar()
entry = tk.Entry(root, textvariable=result_var, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14))
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", on_click)  # Attach on_click event handler
    col += 1
    if col > 3:
        col = 0
        row += 1

for widget in root.grid_slaves():
    widget.grid_configure(padx=10, pady=10)

for i in range(1, 4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
