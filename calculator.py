import tkinter as tk

def on_button_click(char):
    current = display.get()
    display.delete(0, tk.END)  
    display.insert(tk.END, current + char)  


def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)  
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")  

def clear_display():
    display.delete(0, tk.END)  


root = tk.Tk()
root.title("Calculator")


display = tk.Entry(root, width=30, borderwidth=2, font=("Arial", 14), justify="right")
display.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]


for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=evaluate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=clear_display)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda char=text: on_button_click(char))
    button.grid(row=row, column=col, padx=5, pady=5)


root.mainloop()
