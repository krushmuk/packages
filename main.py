import salary
import people
import db.db
from datetime import date


def get_date():
    current_date = date.today()
    return current_date


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(db.db.request)
    print(get_date())
