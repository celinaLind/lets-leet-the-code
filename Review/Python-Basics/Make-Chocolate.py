# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
    """
    ask interviewer: 
    1. will any of the variables be zero?
    2. what should be done if goal zero?
    3. do I need to check for negative values? 
    (don't believe so considering we are working in terms of chocolate
     and you can't have negative choco.
     but if context is user input there may be a user error)

    """

    """
    NOTE:
    Do NOT use the following code:
    max_big = goal / 5

    This is because the division operator will return a float value
    and the problem is asking for an integer value.

    Instead, use the integer division operator:
    max_big = goal // 5
    """
    # get the max # of big bars
    max_big = goal // 5
    # Recommended to make variable names more descriptive
    # EX. max_big_bars

    # set max_big to the smllst amt
    # either big or current max_big value
    if max_big > big:
        max_big = big

    # find the remainder
    remainder = goal - (5 * max_big)

    # use small bars for the remainder
    if remainder <= small :
        return remainder  
        # you would return the remainder since the small bars 
        # would fulfill the remaining order or package amt
    
    return -1
