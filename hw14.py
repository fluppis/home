x = input()
y = tuple()
n = 1
r = 1
while True:
    x = tuple(x)
    for k in x:
        k = int(k)
        r = r*k
    x = str(r)
    u = int(x)
    r = n
    if u <= 9:
        print(u)
        break
