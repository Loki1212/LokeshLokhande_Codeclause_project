import tkinter as tk

class Calculator:
    def _init_(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=25, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+"
        ]
        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(master, text=button_text, width=5, height=2, font=('Arial', 14),
                               command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create equals button
        equals_button = tk.Button(master, text="=", width=5, height=2, font=('Arial', 14),
                                  command=self.calculate)
        equals_button.grid(row=5, column=2, padx=5, pady=5)

    def button_click(self, text):
        # Append button text to display
        current_text = self.display.get()
        if current_text == "0":
            self.display.delete(0, tk.END)
        self.display.insert(tk.END, text)

    def calculate(self):
        # Evaluate the expression in the display and update the display with the result
        expression = self.display.get()
        try:
            result = eval(expression)
        except:
            result = "Error"
        self.display.delete(0, tk.END)
        self.display.insert(0, result)


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()