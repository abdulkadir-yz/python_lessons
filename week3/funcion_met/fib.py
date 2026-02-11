
def max_of_two(a, b):

    if a > b:
        return a
    else:
        return b
    
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


result = max_of_two(a, b)
print(f"The larger number is: {result}")