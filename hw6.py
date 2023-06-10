#list=[12, 3, 4, 10]
#list=[1]
#list=[]
list=[12, 3, 4, 10, 8]
#list=[-12, 3, 4]


x=len(list)
if x==0 :
    print(list)
else:
    t=x-1
    y=list[t]
    list.insert(0,y)
    del(list[x])
    print(list)