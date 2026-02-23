def counting_sort(arr, max_val):
    # -------------------------------------------------------------------
    # STEP 1: CREATE COUNT ARRAY
    # We create an array of zeros with size (max_val + 1) . 
    # Why +1? Because we use values as indexes. If we use max_val as size, we can only index from 0 to max_val-1, but we need to index up to max_val.
    # If max_val=8, we need indexes 0-8, which means 9 elements (8+1)
    # Example: max_val=8 → count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #                       index:   0  1  2  3  4  5  6  7  8
    # -------------------------------------------------------------------
    count = [0] * (max_val + 1)

    # -------------------------------------------------------------------
    # STEP 2: COUNT EACH ELEMENT
    # We iterate through arr and for each element x,
    # we increment count[x] by 1
    # This answers: "How many times does value x appear in arr?"
    #
    # arr = [4, 2, 2, 8, 3, 3, 1]
    # x=4 → count[4]++ 
    # x=2 → count[2]++
    # x=2 → count[2]++
    # x=8 → count[8]++
    # x=3 → count[3]++
    # x=3 → count[3]++
    # x=1 → count[1]++
    #
    # Result:
    # index: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # count: [0, 1, 2, 2, 1, 0, 0, 0, 1]
    # -------------------------------------------------------------------
    for x in arr:
        count[x] += 1

    # -------------------------------------------------------------------
    # STEP 3: PREFIX SUM (CUMULATIVE SUM)
    # We add each count[i] with the previous count[i-1]
    # This transforms count array into a "position map"
    # count[v] now means: "total number of elements <= v"
    #
    # i=1 → count[1] += count[0] → 1 + 0 = 1 
    # i=2 → count[2] += count[1] → 2 + 1 = 3 ( 2 + 1 = 3 because there are 2 elements with value 2 and 1 element with value 1, so total 3 elements are <= 2)
    # i=3 → count[3] += count[2] → 2 + 3 = 5 ( 2 + 3 = 5 because there are 2 elements with value 3 and 3 elements that are <= 2, so total 5 elements are <= 3)
    # i=4 → count[4] += count[3] → 1 + 5 = 6 ( 1 + 5 = 6 because there is 1 element with value 4 and 5 elements that are <= 3, so total 6 elements are <= 4)
    # i=5 → count[5] += count[4] → 0 + 6 = 6 ( 0 + 6 = 6 because there are 0 elements with value 5 and 6 elements that are <= 4, so total 6 elements are <= 5)
    # i=6 → count[6] += count[5] → 0 + 6 = 6 ( 0 + 6 = 6 because there are 0 elements with value 6 and 6 elements that are <= 5, so total 6 elements are <= 6)
    # i=7 → count[7] += count[6] → 0 + 6 = 6 ( 0 + 6 = 6 because there are 0 elements with value 7 and 6 elements that are <= 6, so total 6 elements are <= 7)
    # i=8 → count[8] += count[7] → 1 + 6 = 7 ( 1 + 6 = 7 because there is 1 element with value 8 and 6 elements that are <= 7, so total 7 elements are <= 8)
    #
    # Result:
    # index: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # count: [0, 1, 3, 5, 6, 6, 6, 6, 7]
    #
    # How to read this?
    # count[1]=1 → "there are 1 elements that are <= 1"
    # count[2]=3 → "there are 3 elements that are <= 2"
    # count[4]=6 → "there are 6 elements that are <= 4"
    #              so element 4 will go to index 5 (6-1) in result
    # -------------------------------------------------------------------
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # -------------------------------------------------------------------
    # STEP 4: CREATE EMPTY RESULT ARRAY
    # We create an empty array with same length as arr (n=7)
    # result = [0, 0, 0, 0, 0, 0, 0]
    # -------------------------------------------------------------------
    n = len(arr)
    result = [0] * n

    # -------------------------------------------------------------------
    # STEP 5: PLACE ELEMENTS INTO RESULT (ITERATE BACKWARDS)
    # We go from RIGHT TO LEFT through arr → range(6, -1, -1) = [6,5,4,3,2,1,0]
    # Why backwards? To preserve STABLE SORT property:
    # Elements with the same value keep their original relative order.
    #
    # For each element x = arr[i]:
    #   1. Decrement count[x] by 1       → find the correct position
    #   2. new_index = count[x]           → this is where x goes in result
    #   3. result[new_index] = x          → place x there
    #
    # count (prefix sum):
    # index: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # count: [0, 1, 3, 5, 6, 6, 6, 6, 7]
    #
    # i=6 → x=arr[6]=1 → count[1]-=1 → count[1]=0 → result[0]=1 → result=[1,0,0,0,0,0,0]
    # i=5 → x=arr[5]=3 → count[3]-=1 → count[3]=4 → result[4]=3 → result=[1,0,0,0,3,0,0]
    # i=4 → x=arr[4]=3 → count[3]-=1 → count[3]=3 → result[3]=3 → result=[1,0,0,3,3,0,0]
    # i=3 → x=arr[3]=8 → count[8]-=1 → count[8]=6 → result[6]=8 → result=[1,0,0,3,3,0,8]
    # i=2 → x=arr[2]=2 → count[2]-=1 → count[2]=2 → result[2]=2 → result=[1,0,2,3,3,0,8]
    # i=1 → x=arr[1]=2 → count[2]-=1 → count[2]=1 → result[1]=2 → result=[1,2,2,3,3,0,8]
    # i=0 → x=arr[0]=4 → count[4]-=1 → count[4]=5 → result[5]=4 → result=[1,2,2,3,3,4,8]
    # -------------------------------------------------------------------
    for i in range(n - 1, -1, -1):
        x = arr[i]
        count[x] -= 1
        new_index = count[x]
        result[new_index] = x

    # -------------------------------------------------------------------
    # STEP 6: RETURN SORTED ARRAY
    # Final result: [1, 2, 2, 3, 3, 4, 8] 
    # -------------------------------------------------------------------
    return result


unsorted_array = [4, 2, 2, 8, 3, 3, 1]
max_value = max(unsorted_array)  # → 8
sorted_array = counting_sort(unsorted_array, max_value)
print("Original Array:", unsorted_array)  # [4, 2, 2, 8, 3, 3, 1]
print("Sorted Array:  ", sorted_array)    # [1, 2, 2, 3, 3, 4, 8]