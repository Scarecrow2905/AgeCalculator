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
        