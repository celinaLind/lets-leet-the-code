"""
DESCRIPTION

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

 

Example 1:

Input: nums = [10,4,-8,7]
Output: 2
Explanation: 
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.
Example 2:

Input: nums = [2,3,1,0]
Output: 2
Explanation: 
There are two valid splits in nums:
- Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split. 
- Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.
 

Constraints:

2 <= nums.length <= 105
-105 <= nums[i] <= 105
"""


# Solution
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        # Calculate prefix sums
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        total_sum = prefix_sum[-1]  # Total sum of the array
        valid_splits = 0

        # Iterate through possible split points
        for i in range(n - 1):
            left_sum = prefix_sum[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                valid_splits += 1

        return valid_splits
    
# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 82ms

"""
    NOTES:
    1. Calculate Prefix Sums: Create an array prefix_sum where each element at index j stores the sum of the first j+1 elements of nums.

    2. Total Sum: Compute the total sum of nums to derive the sum of the right part from the left part's sum.

    3. Iterate and Check Valid Splits: For each split index (from 0 to n-2n-2), check whether the conditions for a valid split are satisfied:

        - prefix_sum[i]≥total_sum-prefix_sum[i]
        - i is within bounds.
    4. Count Valid Splits: Increment a counter whenever a split satisfies the conditions.
"""