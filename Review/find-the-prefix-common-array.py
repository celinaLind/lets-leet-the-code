"""
Medium Problem 

DESCRIPTION

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

 

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
Example 2:

Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
 

Constraints:

1 <= A.length == B.length == n <= 50
1 <= A[i], B[i] <= n
It is guaranteed that A and B are both a permutation of n integers.
"""



# Successful Solution - 11ms

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        fini = set()
        C = list()
        for i in range(len(A)):
            common = 0
            if A[i] == B[i] or A[i] in fini or B[i] in fini:
                common = 1 if A[i] == B[i] else (2 if A[i] in fini and B[i] in fini else 1)
            
            fini.add(A[i])
            fini.add(B[i])
            C.append(C[i-1]+common if i>0 else common)
        return C
    
# Better Solution - 0ms

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        
        C = [0] * n
        seta, setb = set(), set()
        for i in range(n):
            C[i] = C[i - 1]
            if A[i] == B[i]:
                C[i] += 1
            else:
                if A[i] in setb:
                    C[i] += 1
                if B[i] in seta:
                    C[i] += 1
                seta.add(A[i])
                setb.add(B[i])
        return C