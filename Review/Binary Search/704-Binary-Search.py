"""
Easy Problem

DESCRIPTION:

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""


# Solution 1 - Time Limit Exceeded Error

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        while len(nums) >= 2:
            testIndex = int((len(nums)/2)-1)
            if nums[testIndex] == target : 
                return testIndex
            elif nums[testIndex] < target:
                nums = nums[testIndex:len(nums)]
            else:
                nums = nums[0:testIndex]
        
        return -1
    

# Successful Solution
# Runtime: 0ms

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index, end_index = 0, len(nums)-1
        while start_index <= end_index:
            midIndex = start_index + (end_index - start_index) // 2 # returns an integer value
            midValue = nums[midIndex]
            if midValue == target:
                return midIndex
            elif midValue > target:
                end_index = midIndex - 1
            else: 
                start_index = midIndex + 1

        return -1
    
# Time Complexity O(log base2 n)
# Space Complexity O(1)