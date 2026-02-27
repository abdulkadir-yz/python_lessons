""" 
TWO SUM 
You are given an array of integers, nums, and an integer, target. Your goal is to find indices of two distinct elements in nums whose sum equals target. You can’t use the same element twice, and you may return the indices in any order. You can assume there is exactly one valid solution for each input.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 9, so return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] = 6, so return [1, 2].
Example 3:

Input: nums = [3,3], target = 6
Output: [0, 1]
Explanation: nums[0] + nums[1] = 6, so return [0, 1].
Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Exactly one valid solution exists. 

"""

# nums = [2, 7, 11, 15]

# target = 18

# def two_sum(nums, target):
#     lenth = len(nums)
#     i = 0
#     while i < lenth:
#         j = i + 1
#         while j < lenth:
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#             j += 1
#         i += 1
#     return []
# result = two_sum(nums, target)
# print(result)

#Get help from AI and ask how can i make easy way to solve this problem?

nums = [2, 7, 11, 15]

target = 9

def two_sum(nums, target): 
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

result = two_sum(nums, target)
print(result)

#Solition 2: Using a hash map (dictionary) to store the indices of the numbers we have seen so far. 
# This allows us to check if the complement (target - current number) exists in the hash map in O(1) time.
def two_sum2(nums, target):
    mapping = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in mapping and mapping[diff] != i:
            return [mapping[diff], i]
        mapping[num] = i
    return []
result2 = two_sum2(nums, 26)
print(result2)