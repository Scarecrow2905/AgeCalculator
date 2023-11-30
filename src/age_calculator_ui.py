from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from datetime import date

class AgeCalculatorGUI:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title('Age Calculator')

        # Widgets
        self.create_widgets()

    
    def create_widgets(self):
        # Label
        self.label = ttk.Label(self.master, text="Enter your birthdate: ")
        self.label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

        # Entry fields
        self.day_entry = ttk.Entry(self.master, width=5)
        self.day_entry.grid(row=1, column=0, padx=10)

        self.month_entry = ttk.Entry(self.master, width=5)
        self.month_entry.grid(row=1, column=1)

        self.year_entry = ttk.Entry(self.master, width=8)
        self.year_entry.grid(row=1, column=2, padx=10)

        # Button
        self.calculate_button = ttk.Button(self.master, text="Calculate Age", command=self.calculate_age)
        self.calculate_button.grid(row=2, column=1, pady=(10, 0))

        # Result label
        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=3, column=0, columnspan=3, pady=(10, 0))
    