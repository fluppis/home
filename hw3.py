x=int(input())
one=x // 10000 % 10
two=x // 1000 % 10
three= x // 100 % 10
four= x // 10 % 10
five= x % 10
print(five,four,three,two,one,sep='')

