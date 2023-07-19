lis_1 = ['a', 'b', 'c', 'd', 'e']

def create_dict(list1):
    list2 = []
    variab = 0
    for i in list1:
        list2.append(variab)
        variab += 1
    res = dict(zip(list2, list1))
    return res


res = create_dict(lis_1)
print(res)

# second option
# def create_dict(list1):
#     res = {index: value for index, value in enumerate(list1)}
#     print(res)
