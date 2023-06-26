x = int(input())
y = divmod(x, 86400)
d = y[0]
h = y[1]
h = divmod(h, 3600)
h1 = h[0]
h1 = str(h1)
m = h[1]
m = divmod(m, 60)
m1 = m[0]
m1 = str(m1)
s = m[1]
s = str(s)
d = str(d)
d1 = tuple(d)
d2 = len(d1) - 1
d3 = d1[d2]
d = int(d)
d3 = int(d3)
if d <= 15:
    if d == 1:
        d = str(d) + ' день, '
        print(d + h1.zfill(2), m1.zfill(2), s.zfill(2), sep=':')
    elif d == 2 or d == 3 or d == 4:
        d = str(d) + ' дні, '
        print(d + h1.zfill(2), m1.zfill(2), s.zfill(2), sep=':')
    else:
        d = str(d) + ' днів, '
        print(d + h1.zfill(2), m1.zfill(2), s.zfill(2), sep=':')
elif d > 15:
    if d3 == 1:
        d = str(d) + ' день, '
        print(d + h1.zfill(2), m1.zfill(2), s.zfill(2), sep=':')
    elif d3 == 2 or d3 == 3 or d3 == 4:
        d = str(d) + ' дні, '
        print(d + h1.zfill(2), m1.zfill(2), s.zfill(2), sep=':')
    else:
        d = str(d) + ' днів, '
        print(d + h1.zfill(2), m1.zfill(2), s.zfill(2), sep=':')
