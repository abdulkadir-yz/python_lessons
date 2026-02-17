
my_list = [1, 2, 3, 4, 5, 5]

def sum_of_list(list):
    sum = 0
    for num in list:
        sum += num
    return sum

def quadratic(list):
    for x , y in list:
        if x==y:
            print(f"{x} and {y} are same.")
        else:
            print(f"{x} and {y} are different.")
print(quadratic(my_list))