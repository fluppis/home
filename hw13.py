import string
y = input('Ввод:')
x = tuple(string.ascii_letters)
y = y.replace('-', '')
i = y[0]
i = x.index(i)
o = y[1]
o = x.index(o) + 1
p = x[i:o]
print(''.join(p))
