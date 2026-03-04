def is_valid(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in mapping:
            # if stack:
            #     top_element = stack.pop()
            # else:
            #     top_element = None

            top_element = stack.pop() if stack else None

            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return True


# Test cases
print(is_valid(")"))  # False
print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True