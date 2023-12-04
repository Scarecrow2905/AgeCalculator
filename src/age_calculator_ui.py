from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from datetime import date

class AgeCalculatorGUI:
    def __init__(self, master, age_calculator) -> None:
        self.master = master
        self.master.title('Age Calculator')
        self.age_calculator = age_calculator


        # Widgets
        self.create_widgets()

    
    def create_widgets(self):
        # Label
        self.label = ttk.Label(self.master, text="Enter your birthdate: ")
        self.label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

        # Entry fields

        # Day Entry
        self.day_var = StringVar()
        self.day_entry = ttk.Entry(self.master, textvariable=self.day_var, width=5)
        self.day_entry.grid(row=1, column=0, padx=10)
        self.day_entry.insert(0, 'Day')

        # Month Entry
        self.month_var = StringVar()
        self.month_entry = ttk.Entry(self.master, textvariable=self.month_var, width=5)
        self.month_entry.grid(row=1, column=1)
        self.month_entry.insert(0, 'Month')

        # Year Entry
        self.year_var = StringVar()
        self.year_entry = ttk.Entry(self.master, textvariable=self.year_var, width=8)
        self.year_entry.grid(row=1, column=2, padx=10)
        self.year_entry.insert(0, 'Year')

        # Button
        self.calculate_button = ttk.Button(self.master, text="Calculate Age", command=self.calculate_age)
        self.calculate_button.grid(row=2, column=1, pady=(10, 0))

        # Result label
        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=3, column=0, columnspan=3, pady=(10, 0))


    def calculate_age(self):
        try:
            # Get values from entry fields
            day = int(self.day_entry.get())
            month = int(self.month_entry.get())
            year = int(self.year_entry.get())

            # Calculate age using the AgeCalculator class
            age_result = self.age_calculator.calculate_age(day, month, year)

            # Update result label
            self.result_label.config(text=f'You are {age_result} years old!')
            if(age_result > 30):
                self.result_label.config(text=f'Damn you are old..')

        except ValueError:
            showerror("Invalid Input", "Please enter valid numbers.")