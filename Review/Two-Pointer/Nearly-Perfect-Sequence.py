# In this problem, you are given a lowercase English letter string 's'.
# The task is to determine whether it is possible to form a palindrome by eliminating no more than one character from 's'.
# A palindrome is a word that reads the same backward as forward.
# The input 's' consists only of lowercase English letters.
# Your solution should return a boolean value, where 'true' indicates that the given string can be rearranged into a palindrome by deleting at most one character, and 'false' otherwise.
 
# Example 1:
# Input: s = "aba"
# Output: true
 
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: By removing the character 'c', the string becomes a palindrome.
 
# Example 3:
# Input: s = "abc"
# Output: false
# Explanation: There is no way to delete a single character to make 'abc' a palindrome.
 
# Constraints:
# The length of the string 's' is at least 1 and at most 10^5.
# Each character in the string 's' is a lowercase English letter.

# VERSION 1
# Time Complexity: O(n)
# O(n) time complexity is due to the loop that iterates through the string.
# Space Complexity: O(1)
# O(1) space complexity is due to the use of a constant number of variables.
def nearlyPerfect(s):
    # set variable for have_rmvd_char
    # this will be used to tell program if we have already "removed" a character from the string
    have_rmvd_char = False

    # set pointer for start and end of string
    start_pt, end_pt = 0, len(s) - 1

    # loop through string and verify that each character from start to end match accordingly
    while start_pt < end_pt:
        if s[start_pt] != s[end_pt]:
            if not have_rmvd_char:
                if s[start_pt+1] == s[end_pt]:
                    start_pt += 1
                elif s[start_pt] == s[end_pt - 1]:
                    end_pt -= 1
                else:
                    return False
                # change boolean since only one character can be "removed"
                have_rmvd_char = True
            else:
                return False
        # increment and decrement values
        start_pt += 1
        end_pt -= 1

    return True

"""
    Recommendations:

    1. Your solution uses a while loop to compare characters, which is O(n) time complexity. However, you could improve efficiency by avoiding the need to check both s[start+1] == s[end] and s[start] == s[end-1] in each iteration.
    2. The code could benefit from more concise logic. For example, you could combine the conditions for checking if a character can be removed into a single if statement, reducing redundancy and improving readability.
"""
        

# VERSION 2
# Time Complexity: O(n)
# Space Complexity: O(n)
# O(n) space complexity is due to the creation of the two substrings.
def nearlyPerfect(s):
    left = 0  # Initialize a pointer at the start of the string.
    right = len(s) - 1  # Initialize another pointer at the end of the string.
    
    # Loop until the left pointer is less than the right pointer.
    # This ensures we're comparing characters moving inwards from both ends of the string.
    while left < right:
        # Check if the characters at the left and right pointers are the same.
        if s[left] == s[right]:
        # If the characters are the same, move the left pointer rightward and the right pointer leftward
        # to continue comparing the next set of characters.
            left += 1
            right -= 1
        else:
        # If the characters at the current pointers do not match, we try to check if removing one character
        # makes the string a palindrome. We check two scenarios:
        # 1. Removing the character at the left pointer (s[left:right]).
        # 2. Removing the character at the right pointer (s[left+1:right+1]).
        # For each substring created by removing a character, we compare it to its reverse.
        # If either reversed substring matches the original substring, it means the string can become
        # a palindrome by removing that character.
            return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]
    
    # If we exit the loop without returning False, it means the string is a palindrome
    # or can become a palindrome by removing one character. Hence, return True.
    return True