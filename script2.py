# Define some sample variables
x = 10
y = 20
z = 10
a = 5
b = 15

# Equal (==)
print("Is x equal to y?", x == y)       # Expected: False
print("Is x equal to z?", x == z)       # Expected: True

# Not equal (!=)
print("Is x not equal to y?", x != y)   # Expected: True
print("Is x not equal to z?", x != z)   # Expected: False

# Greater than (>)
print("Is y greater than x?", y > x)    # Expected: True
print("Is a greater than b?", a > b)    # Expected: False

# Less than (<)
print("Is x less than y?", x < y)       # Expected: True
print("Is b less than a?", b < a)       # Expected: False

# Greater than or equal to (>=)
print("Is x greater than or equal to z?", x >= z)  # Expected: True
print("Is y greater than or equal to b?", y >= b)  # Expected: True

# Less than or equal to (<=)
print("Is x less than or equal to z?", x <= z)     # Expected: True
print("Is a less than or equal to b?", a <= b)     # Expected: True

# Additional combined comparisons
print("Is x equal to 10 and y greater than 15?", (x == 10) and (y > 15))  # True and True -> True
print("Is a less than 10 or b greater than 100?", (a < 10) or (b > 100))   # True or False -> True
