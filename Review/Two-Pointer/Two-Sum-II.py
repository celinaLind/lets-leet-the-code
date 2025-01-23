# Imagine you're given a list of numbers, called 'numbers', which is sorted in ascending order, and you're asked to find a pair of numbers in this list that together sum up to a specific value, called 'target'.
# Your mission is to discover the positions of these two numbers, acknowledging that the first number's position must be less than the second number's position and you cannot use the same number twice.
# Once found, return the positions of these two numbers as a list, where the positions are adjusted to be one-based (meaning, add 1 to each index for the output).
# Remember, there's guaranteed to be exactly one such pair that sums up to the 'target', and your solution should not utilize extra space beyond constant variables.
 
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 equals the target value of 9.
# The positions of 2 and 7 in the input list are 1 and 2, respectively.
 
# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: 2 plus 4 equals the target value of 6.
# The positions of 2 and 4 in the list are 1 and 3, respectively.
 
# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: -1 added to 0 equals the target value of -1.
# The positions of -1 and 0 in the list are 1 and 2, correspondingly.
 
# Constraints:
# The length of 'numbers' ranges from 2 to 30,000.
# Each element in 'numbers' is between -1000 and 1000.
# The list 'numbers' is sorted in non-decreasing order.
# The 'target' value is between -1000 and 1000.
# There is exactly one unique solution for each input.

def sum_pair_finder(numbers, target):
    l,r = 0, len(numbers) - 1
    while l < r:
        sumN = numbers[l] + numbers[r]
        if target == sumN:
            return [l+1, r+1]
        elif target < sumN:
            r -=1
        else:
            l +=1