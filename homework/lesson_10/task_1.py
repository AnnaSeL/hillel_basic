"""Create the file and fill it with data from input"""
# first option

# def fill():
#     file_name = input("Enter file name: ")
#     while True:
#         with open(f"{file_name}.txt", "a+") as file:
#             data = input("Enter your text: ")
#             if not data:
#                 break
#             file.write(data+'\n')
#     file.close()
#
#
# fill()

# second option
import sys


def fill(file_name):
    with open(f"{file_name}.txt", "a+") as file:
        data = input("Enter your text: ")
        if not data:
            sys.exit()
        file.write(data+'\n')
    file.close()
    return fill(file_name)


file_name = input("Enter file name: ")
fill(file_name)
