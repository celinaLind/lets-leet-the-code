"""
Medium Problem

DESCRIPTION

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

# Successful V1 - 83ms

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        usedLtrs = {}
        maxCt = 0
        for i in range(len(s)):
            if s[i] in usedLtrs.keys():
                duplicate = usedLtrs[s[i]]
                for key, value in usedLtrs.copy().items():
                    if value < duplicate:
                        print(f'Being Popped {key}')
                        usedLtrs.pop(key)
            usedLtrs[s[i]] = i
            if maxCt < len(usedLtrs):
                maxCt = len(usedLtrs)
        return maxCt
    
# Better Solution - 11ms

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            charSet.add(s[r])
            res = max(res,r-l+1)
        return res