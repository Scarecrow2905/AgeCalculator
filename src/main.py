from age_calculator import AgeCalculator

try:
    age_calculator = AgeCalculator()
    age_calculator.get_input()

except Exception as e:
    print(f"Something went wrong in main: {e}")

