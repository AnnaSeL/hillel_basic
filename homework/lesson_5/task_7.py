from datetime import datetime


def is_date(day, month, year):
    try:
        date = datetime(year, month, day)
        if date.year != year or date.month != month or date.day != day:
            print("False")
            return False
        print("True")
        return True
    except ValueError:
        print("False")
        return False


day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
is_date(day, month, year)
