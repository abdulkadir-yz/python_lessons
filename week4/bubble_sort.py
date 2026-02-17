# Here we gonna explain how to implement bubble sort algorithm in python. 
# And understand how it works. With mahy examples and explain algorithm step by step.
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
#  compares adjacent elements and swaps them if they are in the wrong order. 
# The process is repeated until the list is sorted.

#Over function like this:

def bubble_sort(arr):
    
    n = len(arr) #len function is used to get the number of elements in the list.
                  #here we are getting the length of the input list 'arr' and storing it in variable 'n'.
                  # In our case n = 5 because we have 5 elements in the list [5, 1, 4, 2, 8].
                  #n = len(arr= = [5, 1, 4, 2, 8]) = 5
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

unsorted_list = [5, 1, 4, 2, 8]
sorted_list = bubble_sort(unsorted_list.copy())
print("Original List:", unsorted_list) # Original List: [5, 1, 4, 2, 8]
print("Sorted List:", sorted_list) # Sorted List: [1, 2, 4, 5, 8]