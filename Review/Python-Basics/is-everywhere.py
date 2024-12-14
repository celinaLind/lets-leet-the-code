# Lets say that a value is "everywhere" in an array if for every pair of adjacent elements in the array, at least one of the pair is that value. 
# Return true if the given value is everywhere in the array.

# isEverywhere([1, 2, 1, 3], 1) → true
# isEverywhere([1, 2, 1, 3], 2) → false
# isEverywhere([1, 2, 1, 3, 4], 1) → false

def isEverywhere(nums, val):
    # Ask Interviewer:
    # is it every two values or sliding window where one has to be every other value?
    # Ex. could it be [1,2,2,1] or only [1,2,1,2]

    # start for loop through nums array
    # go for range of len(nums)-1 to avoid index out of range error
    # this is because we are using the current value and the next value
    for i in range(len(nums)-1):
        # create secondary variable for i+1
        k = i + 1
        # if at any point BOTH values are NOT "val" return false
        if nums[i] != val and nums[k] != val:
            return False

    return True

    """
    CODE FEEDBACK:
    1. Enhance Code Quality
        - While your code works correctly, it could benefit from more robust 
        error handling. Consider adding a check for empty input arrays 
    2. Instead of creating a variable k, you can directly use i+1 
    in the if statement
    """