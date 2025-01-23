# EASY PROBLEM

# In the context of evaluating an inventory list represented by an array of integers, your task is to determine whether any item (number) occurs more than once.
# Your function should return true if at least one item is found in multiple instances, indicating a repeated entry in the inventory.
# Conversely, if each item is unique and no duplicates are present, your function should return false.
 
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
 
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
 
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 
# Constraints:
# The number of items in the inventory (array length) ranges from 1 to 10^5.
# Each item's identifier (integer value) can be between -10^9 and 10^9.

def duplicate_finder(nums):
    for num in nums:
        if nums.count(num) > 1:
            return True
    return False

# Time Complexity : O(n^2)
# Space Complexity: O(1)

# More Efficienct Solution

class Solution:
    def duplicate_finder(nums):
        found = {}
        for num in nums:
            if num in nums:
                return True
            found.append(num)
        
        return False