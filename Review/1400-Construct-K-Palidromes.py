"""
MEDIUM QUESTION

DESCRIPTION:
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= 105
"""


# Successful Solution
# Runtime: 35 ms

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        #1. count the amount of each letter
        count_letters = Counter(s)
        print(count_letters)
        # odd letter count <= k
        # for each k there has to be 
        odd_ct, even_ct = 0,0
        for ct in count_letters.values():
            if ct % 2 != 0:
                odd_ct += 1
                if odd_ct > k:
                    print("Bigger odd_ct:", odd_ct)
                    return False
                if ct > 1:
                    print("Getting even from odd ct:", ct, "added to even_ct value:", (ct-1)/2)
                    even_ct += (ct-1)//2
                    print("New even_ct:", even_ct)
            else:
                even_ct += ct//2
        print("Final value:", even_ct, odd_ct)
        
        return (even_ct > k or odd_ct == k or even_ct + odd_ct == k or  even_ct * 2 > k or even_ct * 2 + odd_ct > k)


# Better Solution - The even_ct and all of its comparisons are unnecessary
# Runtime: 32ms

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False # means there aren't enough letters
        #1. count the amount of each letter
        count_letters = Counter(s)
        print(count_letters)
        # odd letter count <= k
        odd_ct= 0
        for ct in count_letters.values():
            if ct % 2 != 0:
                odd_ct += 1
                if odd_ct > k:
                    print("Bigger odd_ct:", odd_ct)
                    return False
        
        return odd_ct <= k
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)


# Another Version - w/o using the Counter()

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Handle edge cases
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        # Initialize frequency dictionary and odd_count
        freq = [0] * 26
        odd_count = 0

        # Increment the value of the index corresponding to the current character
        for char in s:
            freq[ord(char) - ord("a")] += 1
        # Count the number of characters that appear an odd number of times in s
        for count in freq:
            if count % 2 == 1:
                odd_count += 1
        # Return if the number of odd frequencies is less than or equal to k
        return odd_count <= k