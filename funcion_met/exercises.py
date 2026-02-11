# Python Functions Practice: Conditionals, Loops, and Basic Logic


# 1. Sum of List Elements
def sum_list(numbers):
    """Returns the sum of all numbers in a list."""
    total = 0
    for num in numbers:
        total += num
    return total


# 2. Repeated Greeting
def repeat_greeting(name, times):
    """Prints a greeting to name a specified number of times."""
    for _ in range(times):
        print(f"Hello, {name}!")


# 3. Factorial Calculation
def factorial(n):
    """Returns the factorial of a given number n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 4. Fibonacci Sequence Generator
def fibonacci(n):
    """Returns a list containing the first n numbers of the Fibonacci sequence."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_num)
    
    return fib_sequence


# 5. Maximum of Two Numbers
def max_of_two(a, b):
    """Returns the larger of two numbers."""
    if a > b:
        return a
    else:
        return b


# 6. Print a Pattern with Nested Loops
def print_triangle(rows):
    """Prints a right-angled triangle of asterisks (*) with a given number of rows."""
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()  # Move to next line


# Test cases
if __name__ == "__main__":
    print("=" * 50)
    print("1. Sum of List Elements")
    print("=" * 50)
    numbers = [1, 2, 3, 4, 5]
    print(f"List: {numbers}")
    print(f"Sum: {sum_list(numbers)}")
    
    print("\n" + "=" * 50)
    print("2. Repeated Greeting")
    print("=" * 50)
    repeat_greeting("Alice", 3)
    
    print("\n" + "=" * 50)
    print("3. Factorial Calculation")
    print("=" * 50)
    n = 5
    print(f"Factorial of {n}: {factorial(n)}")
    
    print("\n" + "=" * 50)
    print("4. Fibonacci Sequence Generator")
    print("=" * 50)
    n = 10
    print(f"First {n} Fibonacci numbers: {fibonacci(n)}")
    
    print("\n" + "=" * 50)
    print("5. Maximum of Two Numbers")
    print("=" * 50)
    a, b = 15, 23
    print(f"Max of {a} and {b}: {max_of_two(a, b)}")
    
    print("\n" + "=" * 50)
    print("6. Print a Pattern with Nested Loops")
    print("=" * 50)
    print_triangle(5)
