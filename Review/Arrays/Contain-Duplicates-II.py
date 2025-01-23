"""
Easy Problem

Description:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


# Successful Solution - 17ms

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distinct = {}
        for i, num in enumerate(nums):
            if num in distinct and abs(distinct.get(num) - i) <= k:
                return True
            distinct[num] = i
        return False
    
# Faster Solution - 0ms

class Solution:
    def containsNearbyDuplicate(self, n: List[int], k: int) -> bool:
        d = {}
        for i in range(len(n)):
            if n[i] in d and i - d[n[i]] <= k:
                return True
            d[n[i]] = i
        return False