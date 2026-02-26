nums = [2, 7, 11, 15]

target = 18

def two_sum(nums, target):
    lenth = len(nums)
    i = 0
    while i < lenth:
        j = i + 1
        while j < lenth:
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1
    return []
result = two_sum(nums, target)
print(result)





# nums = [2, 7, 11, 15]

# target = 9

# def two_sum(nums, target): 
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []
# result = two_sum(nums, target)
# print(result)