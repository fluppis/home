def add_one(some_list):
    string_1 = (''.join(map(str, some_list)))
    string_1 = int(string_1) + 1
    result = []
    while string_1 > 0:
        result.append(string_1 % 10)
        string_1 //= 10
    result.reverse()
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
