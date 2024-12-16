# Consider the challenge of identifying whether a given sequence of characters forms a palindrome, specifically after adjusting its format.
# This involves firstly rendering all capital letters to their lowercase equivalents and secondly, discarding any characters that are neither part of the alphabet nor numerals.
# Should the adjusted sequence mirror itself when reversed, it is recognized as a palindrome.
 
# Given a string `s`, devise a function that determines whether this string qualifies as a palindrome under the conditions mentioned, returning `true` if it does, and `false` if otherwise.
 
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: Following adjustments, "amanaplanacanalpanama" presents a mirrored sequence.
 
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: Post-adjustment, "raceacar" fails to exhibit symmetry.
 
# Example 3:
# Input: s = " "
# Output: true
# Explanation: Once non-alphanumeric characters are removed, `s` becomes an empty string "", which inherently meets the criteria of a palindrome.
 
# Constraints:
# - The string `s` length will range from 1 to 200,000 characters.
# - `s` will only comprise printable ASCII characters.

# VERSION 2
# Time Complexity: O(n)
# Space Complexity: O(1)
def isPalindrome(s):
    # second pointer that will start at the end of the string
    pt2 = -1
    for pt1 in range(len(s) - 1):
        if not s[pt1].isalnum():
            continue
        while not s[pt2].isalnum():
            pt2 -=1

        if s[pt1].lower() != s[pt2].lower():
            return False
        pt2 -= 1

    return True


# VERSION 1
# Time Complexity: O(n)
# Space Complexity: O(1)
def isPalindrome(s: str) -> bool:
    # first change string to lowercase
    # second remove all non alphabetical characters
    cleanText = ''.join(char for char in s if char.isalnum()).lower()

    # finally confirm if it is a palidrome
    # one pointer begins at first character and the other begins at the last character
    # if at any point during the for loop they aren't the same value return false
    pt2 = -1
    for i in range(len(cleanText)-1):
        if cleanText[i] != cleanText[pt2]:
            return False 
        pt2 -= 1

    return True

