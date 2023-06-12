import random
my_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
x=len(my_list)
y=x-1
a1=my_list[0]
a2=my_list[2]
a3=my_list[y-1]
print(my_list) #//первоначальный список
print([a1,a2,a3])