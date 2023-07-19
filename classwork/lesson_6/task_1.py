def read_convert_write_data():
    with open('test_data.txt', 'r+') as f:
        result = []
        for row in f:
            result.append(row.replace('\n', '')[::-1] + '\n')
        f.seek(0)
        f.writelines(result)
        return result
print(read_convert_write_data())

# in first task use zip!!!

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,5]
# print(list(zip(list_1, list_2)))
res = {}
for idx, elem in zip(list_1, list_2):
    res[idx] == list_2[idx]
for idx, elem in enumerate(list_1):
    print(elem == list_2[idx])
