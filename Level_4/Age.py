from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year

print(calculate_age(2003))