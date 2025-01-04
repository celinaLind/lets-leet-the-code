"""
    DESCRIPTION:

    Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
"""

# Version 1 - Time Limit Exceeded
# Time Taken: 20mins

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # define a set where found subsequences are stored
        # use a set so no duplicates can be added
        subset = set()

        # create pointers to process through the sequence
        sLength = len(s)-1
        endPaliLetter = sLength
        for initialPaliLetter in range(sLength - 2):
            # will have to change this while loop since it will o
            while initialPaliLetter < endPaliLetter:
                if s[initialPaliLetter] == s[endPaliLetter]:
                    for middlePaliLetter in range(initialPaliLetter, endPaliLetter):
                        subset.add(f'{s[initialPaliLetter]}{s[middlePaliLetter]}{s[endPaliLetter]}')
                else:
                    endPaliLetter -= 1  
            # after while loop reset the ending value
            endPaliLetter = sLength
        return len(subset)
    
# Time Limit Exceeded because I don't take into account indexes that have already been processed

# Version 2 -Returning wrong results
# Trying to separate the letters into a dictionary and then process the dictionary
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Step 1: Prepare the right character map
        n = len(s)
        right = [set() for _ in range(n)]
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            right[i] = seen.copy()

        # Step 2: Use a left set and count unique palindromes
        left = set()
        palindromes = set()
        
        for i in range(n):
            char = s[i]
            left.add(char)
            for c in left:
                if char in right[i]:
                    palindromes.add((c, char, c))
        
        
# Version 3 - Optimized Solution

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        result = set()

        # Iterate over all lowercase letters as potential outer characters of the palindrome
        for char in set(s):
            # Find the first and last occurrence of the character
            left = s.find(char)
            right = s.rfind(char)
            
            # Ensure there is a range for the middle character
            if right - left > 1:
                # Add all unique palindromes of the form (char, middle, char)
                for middle in set(s[left + 1:right]):
                    result.add((char, middle, char))
        
        return len(result)

"""
    Explanation of the Fix
    Outer Characters:
        Use set(s) to iterate over all distinct characters in the string as potential outer characters for the palindrome.
    First and Last Occurrences:
        Use s.find(char) and s.rfind(char) to identify the range where the middle   characters can appear.
    Middle Characters:
        Iterate over all unique characters between the first and last occurrence and add valid palindromes to the result set.
"""
# Time Complexity: O(N)
# Space Complexity: O(N)