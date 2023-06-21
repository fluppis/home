import keyword
import string
a = input(str())
x = a[0]
sim = string.punctuation + ' '
word = keyword.kwlist
if a == ' ':
    print('False')
elif x.isdigit():
    print('False')
elif a in word:
    print("False")

elif a.isdigit():
    print('False')
else:
    for k in a:
        if k == '_':
            continue
        if k in sim:
            print("False")
            break
    else:
        for g in a:
            if g.isupper():
                print('False')
                break
        else:
            print('True')