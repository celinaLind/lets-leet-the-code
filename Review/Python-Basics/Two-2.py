# Given a list of non-negative integers, return a list of those numbers multiplied by 2, omitting any of the resulting numbers that end in 2.

# two2([1, 2, 3]) → [4, 6]
# two2([2, 6, 11]) → [4]
# two2([0]) → [0]

def two2(nums):
    # initialize empty list to house the doubled values
    doubledNums = []

    # iterate over list and double the values
    for num in nums:
        num *= 2
        # verify if the new value ends in a two
        if num % 10 != 2:
            # Add the doubled value to the list
            doubledNums.append(num)

    return doubledNums


# # Another way to solve without creating a new list
# # range(start, stop, step) --> started at the last number, stopped at the first number, and decremented by 1
# for i in range(len(scores) - 1, -1, -1):
#     doubled = scores[i] * 2
#     print("doubled", doubled)
#     if doubled % 10 != 2:
#         scores[i] = doubled
#     else:
#         scores.pop(i)

## Evaluation
# Your initial implementation had some 
# unnecessary steps, like using pop() to remove elements. 
# Try to simplify your code by using list comprehension or 
# filter() for a more concise and Pythonic solution.