first_list=[1, 2, 3, 4, 5, 6]
#first_list=[1, 2, 3]
#first_list=[1, 2, 3, 4, 5]
#first_list=[1]
#first_list=[]

x=len(first_list)
if x>3:
    my_list = [first_list[:3], first_list[3:6]]
    print(my_list)
elif x==3:
    my_list = [first_list[:2], first_list[2:3]]
    print(my_list)
else:
    my_list = [first_list[:1], first_list[1:2]]
    print(my_list)
#my_list = [first_list[:3], first_list[3:6]] // так отрабатывало но фейлилось на примере [1, 2, 3]