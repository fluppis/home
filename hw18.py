def second_index(text, some_str):
    for elem in text:
        elem = text.find(some_str)
        elem = text.find(some_str, elem + 1)
        if elem > 0:
            return elem


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
assert second_index("Hillo, hello", "e") is None, 'Test5'
print('ОК')
