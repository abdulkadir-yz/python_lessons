print("Starting program")
a = 5
b = 10
sum_ab = a + b
print("The sum of", a, "and", b, "is", sum_ab)

# Decision Making with if-elif-else
if sum_ab > 10:
    print("The sum is greater than 10.")
elif sum_ab == 10:
    print("The sum is exactly 10.")
else:
    print("The sum is less than 10.")

# Pattern Matching (Python 3.10+)
day = 3
print("\nUsing pattern matching for day number:")
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Another day")

# Repetition: For Loop on list
fruits = ['cherry', 'banana', 'apple']
for fruit in fruits:
    print(f"I really like {fruit}")

# Repetition: While Loop
print("\nWhile loop until count reaches 5:")
count = 0
while count < 5:
    print(count)
    count += 1
print("Program ended")