# In a sequence of numbers, a pair of elements is considered 'identical' if both elements have the same value and the first element's index is less than the second element's index.
# Your task is to write a program that counts the number of such identical pairs within a given sequence of numbers, represented by an array 'nums'.
 
# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: The identical pairs are (0,3), (0,4), (3,4), and (2,5), using 0-based indexing.
 
# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Every pair in this sequence is identical.
 
# Example 3:
# Input: nums = [1,2,3]
# Output: 0
 
# Constraints:
# The length of the array 'nums' is between 1 and 100, inclusive.
# Each element in 'nums' is an integer between 1 and 100.

# Great Approach
from collections import defaultdict

def countIdenticalPairs(nums):
    valueCount = defaultdict(int)
    pairCount = 0

    for num in nums:
        pairCount += valueCount[num]  # Add existing count (forms pairs)
        valueCount[num] += 1          # Increment count for current num

    return pairCount

# Good Approach
def countIdenticalPairs(nums):
    # use dictionary to store value count
    valueCount = {}
    # use variable to store pair count
    pairCount = 0

    # iterate through values in nums list
    for num in nums:
        # if num is in value count
        if valueCount.get(num):
            # add the current value count to pairCount
            pairCount += valueCount[num]
            # increase current value count by 1
            valueCount[num] += 1
        else:
            # if num is not in valueCount add it
            valueCount[num] = 1

    return pairCount


# Successful but BAD Approach
def countIdenticalPairs(nums):
    # if length of nums is less than 2 there are no pairs
    if len(nums) < 2:
        return 0

    # two pointer method
    left, right = 0, 1
    pairCount = 0
    print(len(nums))
    while left < right:
        # if nums left value is equal to nums right value add 1 to pair count
        if nums[left] == nums[right]:
            pairCount += 1
        # check to see if right value is at the end of the list
        if right == len(nums) - 1:
            # if it is at the end add 1 to left value and reset right value to left + 1
            # as long as left value isn't at the end of the list
            left += 1
            right = left + 1 if left < len(nums) - 1 else left
        else:
            right +=1

    return pairCount 