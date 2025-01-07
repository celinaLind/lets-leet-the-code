"""
DESCRIPTION:

Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.
"""

# Solution 3 - Success
# Runtime: 3ms
# Total Time Taken: 13 min (correcting errors)

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subWords= set()
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    # REMOVING THESE PRINT STTMENTS 
                    # improved runtime to 0ms from 3ms
                    # print(subWords)
                    # print(words[i])
                    # print(words[j])
                    subWords.add(words[i])
                    break
                elif words[j] in words[i]:
                    subWords.add(words[j])
                    break
            
        return list(subWords)

"""
At first I set subwords as a list which then welcomed duplicate values to be added, so I changed it to a set.

In python you can initialize a set with a function call: variable = set()

To add to a set you use the variable.add(valueToAdd) function

To change back to a list you use the list(variable) function
"""


# Alternative Solution
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        r=' '.join(words)
        s=[i for i in words if r.count(i)>1]
        return s