# Determine if two provided words are anagrams of each other.
# An anagram is defined as a word obtained by rearranging the letters of another word, using all the original letters exactly once.
# For this verification, input consists of two strings: 's' representing the first word, and 't' for the second word.
# The goal is to return true if 't' is an anagram of 's', otherwise, return false.
 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
 
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
 
# Constraints:
# - The length of both strings 's' and 't' will be in the range of 1 to 50,000.
# - Both strings will contain only lowercase English letters.

# Version 1 - Successful
from collections import Counter
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    ctS, ctT = Counter(s), Counter(t)
    return ctS == ctT

# Version 2 - Successful
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z'}

    for ltr in alpha:
        if s.count(ltr) != t.count(ltr):
            return False

    return True

# Faster Solution - 0 ms

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
    
        for x in set(s):
            if(s.count(x)!=t.count(x)):
                return False
        return True
    
# created a set for one string and then compared the counts for each letter to the other string
# if at any point the counts for the character aren't equal return false

# More efficient solution - O(1) => some interviewers don't considered sorting as taking up much time

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
# for this solution, if the strings are anagrams once sorted the letters will be in order a-z and will be the same string once sorted