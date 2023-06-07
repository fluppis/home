first_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#first_list=[1, 2, 3]
#first_list=[1, 2, 3, 4, 5]
#first_list=[1]
#first_list=[]

x=len(first_list)
y=x-(x//2)
my_list = [first_list[0:y], first_list[y:x]]
print(my_list)
