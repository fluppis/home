import string

x = input("Введите не больше 139 символов:")
u = string.punctuation + ' '
x = x.title()
for k in u:
    for r in x:
        if k == r:
            x = x.replace(k, "")
print("#"+x[0:139])
