def is_palindrome(text):
    import string
    a = string.punctuation + ' '
    x = text.lower()
    for k in x:
        for o in a:
            if k == o:
                x = x.replace(k, '')
    rev_1 = x[::-1]
    if x == rev_1:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")