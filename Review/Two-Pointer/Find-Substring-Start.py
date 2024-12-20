# Imagine you have a long piece of text ('haystack') and you are looking for a specific smaller string ('needle') within it.
# Your task is to determine where in the text the smaller string first shows up.
# You should output the starting position of the first occurrence of the 'needle' in the 'haystack'.
# Should the 'needle' not be found within the 'haystack', your program must return -1, indicating its absence.
 
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: The substring "sad" is first found at the start of the "haystack", thus the output is 0.
 
# Example 2:
# Input: haystack = "helloworld", needle = "123"
# Output: -1
# Explanation: Since "123" is not present in "helloworld", we return -1.
 
# Constraints:
# The length of both 'haystack' and 'needle' will be between 1 and 10^4, inclusive.
# Both 'haystack' and 'needle' will contain only lowercase English letters.

# VERSION 1
# Time Complexity: O(n*m)
# where n is the length of the haystack and m is the length of the needle
# Space Complexity: O(1)
def findSubstringStart(haystack, needle):
    # 1. check if haystack or needle is empty
    if needle is None:
        return 0 
    # First, check if the needle string is empty. According to string searching conventions, an empty needle is always found at index 0 in the haystack. If needle is indeed empty, return 0.

    # use lengths of needle and haystack (this will be the iteration range for the loops)

    # loop through haystack
    #This ensures that when checking for the presence of needle, the substring extracted from haystack does not exceed its length.
    for i in range(len(haystack) - len(needle) + 1):
        # Extract substring and compare to needle
        # string[start:end:step]
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1

    # for i in range(len(haystack) + 1 - len(needle)):
    #     for j in range(len(needle)):
    #         if haystack[i + j] != needle[j]:
    #             break
    #         if j == len(needle) -1:
    #             return i

    #  ^ is the same as the substring command we did on line 35

# VERSION 2
def findSubstringStart(haystack, needle):
    # verify if needle is empty
    # if needle is empty return 0 due to string search practices
    if needle is "":
        return 0

    # create a loop going through the haystack range
    # but make the range (haystack - needle) to not exceed and review unnecessary characters
    # you will also need to add the subtracted lengths by one to include the full needle poss.
    for i in range(len(haystack) - len(needle) + 1):
        #compare substring starting at index i that is the same length as len(needle) to the needle string
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1


"""
Recommendations:

1. Consider exploring more optimized algorithms like KMP or Rabin-Karp for improved efficiency.
2. Your edge case handling checks for 'None' instead of an empty string. This could lead to unexpected behavior. Always ensure your edge case checks align precisely with the problem requirements.
"""