# Consider two textual sequences represented by strings 's' and 't'.
# Your task is to ascertain whether 's' can be derived from 't' through the omission of some characters, without altering the sequential order of the remaining characters.
# In other words, determine if 's' stands as a subsequence of 't'.
# The term 'subsequence' signifies a sequence that can be derived from another sequence by deleting certain elements without changing the order of the remaining elements.
 
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Explanation: By removing 'h', 'b', 'g', and 'd' from "ahbgdc", the string "abc" is obtained, which maintains the relative positioning, hence 's' is a subsequence of 't'.
 
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
# Explanation: There's no way to obtain "axc" from "ahbgdc" while preserving the original order, indicating 's' is not a subsequence of 't'.
 
# Constraints:
# The length of 's' falls within the range of 0 to 100.
# The length of 't' is at most 10^4.
# Both 's' and 't' contain only lowercase English letters.

def checkSubsequence(s, t):
    checkedIndex=0
    checked = set()
    if len(s) > len(t):
        return False
    
    if len(s) == 0:
        return True
    
    for char in t:
        if s[checkedIndex] == char and s[checkedIndex] not in checked:
            checked.add(char)
            checkedIndex += 1

    return len(s) < checkedIndex + 1
