"""
Easy Problem 

Description:

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


# Successful Solution - 15ms

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        listS = list(s)
        locations = [] * len(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                locations.append(i)
        
        start, end = 0, len(locations)-1
        while start < end:
            swapLetter = s[locations[start]]
            listS[locations[start]] = listS[locations[end]]
            listS[locations[end]] = swapLetter
            start +=1
            end -= 1
        
        return "".join(listS)

# Faster Solution - 2ms

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            
            while left < right and s_list[right] not in vowels:
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]

            left += 1
            right -= 1

        return ''.join(s_list)