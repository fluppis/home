def common_elements():
    import random
    lis_1 = []
    lis_2 = []
    ran_1 = random.randint(1, 1000)
    for x in range(3, ran_1, 3):
        lis_1.append(x)
    for k in range(5, ran_1, 5):
        lis_2.append(k)
    lis_1 = set(lis_1)
    lis_2 = set(lis_2)
    return lis_1 & lis_2


print(common_elements())
