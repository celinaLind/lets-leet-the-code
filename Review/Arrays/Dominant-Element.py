# Imagine you have a list of numbers, referred to as 'nums', with a total length of 'n'.
# Your task is to identify the dominant element in this list.
# The dominant element is defined as the one that appears more than half the time (n / 2) in the list.
# It is guaranteed that such an element exists in the list.
 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
 
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# - The length of 'nums' is equal to 'n'.
# - 'n' ranges from 1 to 50,000.
# - Each element in 'nums' can be any integer between -1,000,000,000 and 1,000,000,000.
 
from collections import Counter

def majorityElement(nums):
    counted = Counter(nums)
    dominantCt = 0
    dominantIndex = 0
    for key, val in counted.items():
        if val > dominantCt:
            dominantCt = val
            dominantIndex = key
    return dominantIndex