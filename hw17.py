def correct_sentence(text):
    x=(text)
    y=len(x) - 1
    b=x[y]
    if b == '.':
        return text.capitalize()
    else:
        return text.capitalize() + "."


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings, friends") == "Greetings, friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
