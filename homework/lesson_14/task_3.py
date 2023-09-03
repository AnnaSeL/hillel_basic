"""Program checks if the given password correspond to all requirements"""
import re


def check_password(password) -> str:
    if len(password) < 8:
        return "Too short password"
    elif not re.search(r'[a-z]', password):
        return "You should use at least one symbol from a-z"
    elif not re.search(r'[A-Z]', password):
        return "You should use at least one symbol from A-Z"
    elif not re.search(r'[0-9]', password):
        return "You should use at least one symbol from 0-9"
    elif not re.search(r'[$#@+=-]', password):
        return "You should use at least one symbol from $#@+=-"
    else:
        return "Password is correct"

if __name__=="__main__":
    passw = input("Enter your password: ")
    print(check_password(passw))

