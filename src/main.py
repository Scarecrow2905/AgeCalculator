from age_calculator import AgeCalculator
from age_calculator_ui import *

try:
    root = Tk()
    age_calculator = AgeCalculator()
    app = AgeCalculatorGUI(root, age_calculator)
    root.mainloop()

except Exception as e:
    print(f"Something went wrong in main: {e}")

