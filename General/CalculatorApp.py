import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x400")
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)
        
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        
        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()
        
        self.create_buttons(btns_frame)
        
    def create_buttons(self, frame):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]
        
        row = 0
        col = 0
        
        for button in buttons:
            if button == 'C':
                btn = tk.Button(frame, text=button, fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=self.clear_input)
            elif button == '=':
                btn = tk.Button(frame, text=button, fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=self.calculate)
            else:
                btn = tk.Button(frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda x=button: self.button_click(x))
            
            btn.grid(row=row, column=col, padx=1, pady=1)
            col += 1
            
            if col > 3:
                col = 0
                row += 1
                
    def button_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)
        
    def clear_input(self):
        self.expression = ""
        self.input_text.set("")
        
    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
