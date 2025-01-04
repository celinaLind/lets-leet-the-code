"""
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""
# Overall Time Taken 16mins 32secs for 2 versions
# Version 1: Solution is duplicating string characters from word1 but not adding any characters from word2

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        word1Index, word2Index = 0, 0
        word1Len, word2Len = len(word1), len(word2)
        while word1Index < word1Len or word2Index < word2Len:
            if word1Index == word1Len:
                mergedWord += word2[word2Index:word2Len]
            elif word2Index == word2Index:
                mergedWord += word1[word1Index:word1Len]
            else:
                mergedWord += word1[word1Index] + word2[word2Index]

            word1Index += 1
            word2Index += 1
        
        return mergedWord

# Time complexity: O(n)
# Space complexity: O(n)

# Version 2: Successful solution
# Runtime: 42ms

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        word1Index, word2Index = 0, 0
        word1Len, word2Len = len(word1), len(word2)
        while word1Index < word1Len or word2Index < word2Len:
            if word1Index == word1Len:
                mergedWord += word2[word2Index:word2Len]
                break
            elif word2Index == word2Len:
                mergedWord += word1[word1Index:word1Len]
                break
            else:
                mergedWord += word1[word1Index] + word2[word2Index]
                word1Index += 1
                word2Index += 1
        
        return mergedWord
    
# Time complexity: O(n)
# Space complexity: O(n)


# More optimized solution
# Runtime: 23ms

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
     list = []
     i = 0
     j = 0

     while i<len(word1) and j<len(word2):
        list.append(word1[i])
        list.append(word2[i])
        i = i + 1
        j = j + 1

     list.append(word1[i:])
     list.append(word2[j:])
    
     return  "".join(list)
    
# Time complexity: O(n)
# Space complexity: O(n)