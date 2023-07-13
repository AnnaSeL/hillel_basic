def remove_none(diction):
    res = {key: value for key, value in diction.items() if value != 'None'}
    return res


dictionary = {}
while True:
    k = input("Введіть ключ (або Enter для завершення вводу): ")
    if not k:
        break
    val = input("Введіть значення: ")
    dictionary[k] = val
result = remove_none(dictionary)
print(result)

# second option
# def remove_none(dictionary):
#     return {key: value for key, value in dictionary.items() if value is not None}
#
#
# my_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
# result = remove_none(my_dict)
# print(result)
