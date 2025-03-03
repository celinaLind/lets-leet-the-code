"""
Medium Problem
DESCRIPTION

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

 

Example 1:


Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
 

Constraints:

n == s.length == locked.length
1 <= n <= 105
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.
"""


# Incorrect Solution

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        if n < 2 or n & 1:
            return False
        
        for i in range(len(s)):
            if i & 1:
                print("s[i] odd:", i, s[i])
                if s[i] == ")" or s[i] == "B" or locked[i] == "0":
                    continue
                else:
                    return False
            else:
                print("s[i] even:", i, s[i], "locked", locked[i])
                if s[i] == "(" or s[i] == "A" or locked[i] == "0":
                    continue
                else:
                    return False
        return True

    
# Correct Solution using Stacks

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        if n < 2 or n % 2 == 1:
            return False
        
        # Stack Method
        openB = []
        unlckd = []

        for i in range(n):
            if locked[i] == '0':
                unlckd.append(i)
            elif s[i] == "(":
                openB.append(i)
            elif s[i] == ")":
                if openB:
                    openB.pop()
                elif unlckd:
                    unlckd.pop()
                else:
                    return False
        
        while openB and unlckd and openB[-1] < unlckd[-1]:
            openB.pop()
            unlckd.pop()

        return not openB