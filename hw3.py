x=int(input())
one=x // 10000 % 10
two=x // 1000 % 10
three= x // 100 % 10
four= x // 10 % 10
five= x % 10

print(five*10000+four*1000+three*100+two*10+one)