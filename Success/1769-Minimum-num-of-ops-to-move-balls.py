"""
DESCRIPTION:

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

 

Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
Example 2:

Input: boxes = "001011"
Output: [11,8,5,4,3,4]
 

Constraints:

n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.
"""

# Version 1 - Success
# Runtime : 1109ms

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # first run through we are going to mark the indexes that have a ball
        haveBall =[]
        for i in range(len(boxes)):
            if boxes[i] == "0":
                continue
            else:
                haveBall.append(i)

        movesPerBox = []
        # second run through we are going to count moves and add to moves list
        for i in range(len(boxes)):
            moves = 0
            for index in haveBall:
                moves += abs(i-index)
            movesPerBox.append(moves)

        return movesPerBox
    
# Time Complexity: Overall, the time complexity is (O(n + n \cdot m)). Since (m) can be at most (n), the worst-case time complexity is (O(n^2)).
# Space Complexity: O(n)
# Overall, the space complexity is (O(n + m)). Since (m) can be at most (n), the worst-case space complexity is (O(n)). 
    

# Better Runtime/Time Complexity Solution:

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        pref = p = s = 0
        for i, el in enumerate(boxes):
            if el == '1':
                pref += i
                p += 1
        for el in boxes:
            answer.append(pref)
            if el == '1':
                p -= 1
                s += 1
            pref = pref - p + s
        return answer
    
# Time Complexity: O(n) => since loops are run sequentially
# Space Complexity: O(n)
"""
Step-by-Step Explanation
Initialization:

answer: An empty list to store the result.
pref: A prefix sum to keep track of the total number of operations needed to move all balls to the current box.
p: The count of '1's (balls) encountered so far.
s: The count of '1's (balls) encountered after the current box.
First Loop (Prefix Calculation):

This loop iterates over the boxes string to calculate the initial prefix sum (pref) and the total number of balls (p).
For each box that contains a ball ('1'), it adds the index i to pref and increments p by 1.
Second Loop (Calculate Operations):

This loop iterates over the boxes string again to calculate the minimum number of operations for each box.
It appends the current pref value to the answer list.
If the current box contains a ball ('1'), it decrements p by 1 (since this ball is now considered to be after the current box) and increments s by 1 (since this ball is now considered to be before the next box).
It updates pref by subtracting p (balls to the right) and adding s (balls to the left).
Return Result:

The function returns the answer list, which contains the minimum number of operations required to move all balls to each box.
"""