#list=[0, 1, 2, 0, 12]
#list=[1, 0, 3, 0, 0, 0, 5]
#list=[]
list=[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


list2=[]
list3=[]
x=len(list)
t=0
while t<x :
    i=list[t]
    if i==0:
        list2.append(i)
    else:
        list3.append(i)
    t = t +1
list=list3+list2
print(list)