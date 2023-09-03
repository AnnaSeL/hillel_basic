"""Program format the given phone number to the standard (+38) 000 000-00-00"""
import re


def format_phone_number(number):
    numbers = re.findall(r'[0-9]', number)
    if len(numbers) == 10:
        return "(+38) {}{}{} {}{}{}-{}{}-{}{}".format(*numbers)
    elif len(numbers) == 12:
        return "(+{}{}) {}{}{} {}{}{}-{}{}-{}{}".format(*numbers)
    else:
        return "Failed to recognize number"


if __name__ == "__main__":
    num = input("Enter the phone number: ")
    print(f"Formatted phone number: {format_phone_number(num)}")
