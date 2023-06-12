#list=[1, 3, 5]
#list=[6]
#list=[]
#list=[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


x=len(list)
y=x-1
t= -1
a=0
if x>0 :
   while t<=y :
        if not t%2 :
           w=list[t]
           a=a+w
        t = t + 1
   y = list[y]
   a = a * y
   print(a)

else:
    print(int(0))
