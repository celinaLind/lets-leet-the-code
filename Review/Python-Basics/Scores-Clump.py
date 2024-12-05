# Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each other by at most 2, such as with [3, 4, 5] or [3, 5, 5]

# scoresClump([3, 4, 5]) → true
# scoresClump([3, 4, 6]) → false
# scoresClump([1, 3, 5, 5]) → true


def scoresClump(scores):
    # Loop through the array, stopping 2 elements before the end to avoid index out of range errors.
    # This is because we're looking at groups of 3 adjacent scores.
    for i in range(len(scores) - 2):
        # Check if the difference between the smallest (scores[i]) and largest (scores[i+2]) in each group of 3 scores
        # is 2 or less. Since the array is sorted in increasing order, scores[i] is the smallest,
        # and scores[i+2] is the largest in the group of three.
        if scores[i+2] - scores[i] <= 2:
            return True  # If we find such a group, return True immediately.
    
    # If we finish looping through the array without finding such a group, return False.
    return False