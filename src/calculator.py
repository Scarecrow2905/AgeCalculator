# Age calculation logic
from datetime import date

class AgeCalculator:
    def __init__(self) -> None:
        pass

    def calculate_age(self, day, month, year):
        today = date.today()
        birthdate = date(year, month, day)
        
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        return age
        
    def get_input(self):
        try:
            day = int(input('Enter day:'))
            month = int(input('Enter month:'))
            year = int(input('Enter year:'))

            age_result = self.calculate_age(day, month, year)
            print(f'You are {age_result} years old')
        except ValueError as ve:
            print(f"Error {ve}")