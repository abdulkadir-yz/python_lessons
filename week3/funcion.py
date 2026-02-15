
#what is function in python?
#A function is a reusable block of code that performs a specific task. 
#Functions allow you to break down your code into smaller, more manageable pieces, making it easier to read, maintain, and debug.
#Functions can take input in the form of parameters, perform operations on that input, and return a result. They can also be called multiple times throughout your code, which helps to avoid repetition and
#improves code organization.
# return statement is used to exit a function and return a value to the caller. It can be used to return any type of data, including numbers, strings, lists, or even other functions. If a function does not have a return statement, it will return None by default.
#Functions can be defined using the def keyword, followed by the function name and parentheses. The code block within the function is indented, and you can include parameters within the parentheses to allow for input when the function is called.
#Here is an example of a simple function that takes two numbers as input and returns their sum:
def add_numbers(a, b):
    return a + b    
result = add_numbers(3, 5)
print(result)  # Output: 8  



#Karesini al Fonksionu
def kare(x):
    print(x * x)
kare(5)  # Output: 25
A = kare(5)  # Output: 25
print(A)  # Output: None


#Karesini Al ve Return Et Fonksionu
def kare(x):
    return x * x
A = kare(5)
print(A)  # Output: 25 

#The return statement terminates the function and specifies the value returned by the function. When the return statement is used within a function, the function stops executing and returns the specified value to the calling code. If the return statement is not used, the function returns the None value.
 
 