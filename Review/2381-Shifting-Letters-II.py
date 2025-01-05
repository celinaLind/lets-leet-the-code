"""
DESCRIPTION:

You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
 

Constraints:

1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters
"""

# Successful Solution:

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Create a list of all the letters in the alphabet
        import string
        alphabet = string.ascii_lowercase
        
        # Convert the string into a mutable list
        s = list(s)
        
        # Create a list to store the cumulative shift for each character
        n = len(s)
        cumulative_shifts = [0] * (n + 1)

        # Apply the shifts
        for start, end, direction in shifts:
            # Increment or decrement the shift range
            if direction == 1:
                cumulative_shifts[start] += 1
                if end + 1 < n:
                    cumulative_shifts[end + 1] -= 1
            else:
                cumulative_shifts[start] -= 1
                if end + 1 < n:
                    cumulative_shifts[end + 1] += 1

        # Compute the prefix sum to get the final shift for each character
        current_shift = 0
        for i in range(n):
            current_shift += cumulative_shifts[i]
            current_shift %= 26  # Ensure shift is within bounds
            
            # Calculate the new character
            alpha_index = alphabet.index(s[i])
            new_index = (alpha_index + current_shift) % 26
            s[i] = alphabet[new_index]

        return ''.join(s)

"""
Key Improvements:
Cumulative Shifts:

The cumulative_shifts array tracks the net effect of all shifts at each position.
This reduces the complexity from O(m×n) (nested loops for each shift) to 
O(m+n), where m is the number of shifts and n is the length of the string.

Prefix Sum:
Using a prefix sum, we calculate the total shift for each character efficiently, avoiding the need for nested loops.
Output Management:

Removed print statements to avoid the excessive output issue.
Explanation of the Process:
Shift Initialization:

For each range [start, end], increment or decrement the cumulative shift in cumulative_shifts.
Apply Prefix Sum:

Iterate through cumulative_shifts to calculate the net shift for each character.
Shift Characters:

Use the calculated shift to update each character in s.
Return Result:

Convert the list back to a string and return it.
Complexity:
Time Complexity: O(m+n):
- O(m) for applying the shifts.
- O(n) for computing the prefix sum and updating the string.
Space Complexity: 
- O(n) for the cumulative_shifts array.
"""