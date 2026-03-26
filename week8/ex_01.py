my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for x in my_list:
    print(x)

for x in my_list:
    new_x =float(x * x)
    print(new_x)

for x in my_list:
    if x % 6 == 0:
        print(x)