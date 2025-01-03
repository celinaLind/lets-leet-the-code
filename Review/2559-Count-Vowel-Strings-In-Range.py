"""
DESCRIPTION:

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
 

Constraints:

1 <= words.length <= 105
1 <= words[i].length <= 40
words[i] consists only of lowercase English letters.
sum(words[i].length) <= 3 * 105
1 <= queries.length <= 105
0 <= li <= ri < words.length

"""

# Version-1 Solution (Success)
# Error: Output Limit Exceeded
# This means that the solution is correct but the output is too large.

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        returnVowelStrings = []
        print("length queries", len(queries)-1)
        for i in range(0,len(queries)):
            print("i = ", i)
            count = 0
            for j in range(queries[i][0], queries[i][1]+1):
                print("Word:", words[j])
                charList = list(words[j])
                print("CharList:", charList, "CharLength:", len(charList)-1)
                if charList[0] in vowels and charList[len(charList)-1] in vowels:
                    count += 1
                    print("First Char:", charList[0], "LastChar:", charList[len(charList)-1])
                    print("Count:", count)
            returnVowelStrings.append(count)
            print("Appended Count:", count)
        return returnVowelStrings
            

# Version-2 Solution (Success)
# Error: Time Limit Exceeded
# This means that the solution is correct but the time taken to execute is too large.

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        returnVowelStrings = []
        for i in range(0,len(queries)):
            count = 0
            for j in range(queries[i][0], queries[i][1]+1):
                word = words[j]
                if word[0] in vowels and word[len(word)-1] in vowels:
                    count += 1
            returnVowelStrings.append(count)
        return returnVowelStrings

# Version-3 Solution (Success)
# Error: Time Limit Exceeded

class Solution:
    def findVowels(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if word[0] in vowels and word[len(word)-1] in vowels:
            return True
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        returnVowelStrings = []
        for i in range(0,len(queries)):
            count = 0
            # Two pointer
            startWordIndex = queries[i][0]
            endWordIndex = queries[i][1]
            while startWordIndex <= endWordIndex:
                startWord = words[startWordIndex]
                if startWordIndex == endWordIndex:
                    count += 1 if self.findVowels(startWord) else 0
                else:
                    count += 1 if self.findVowels(startWord) else 0
                    count += 1 if self.findVowels(words[endWordIndex]) else 0
                startWordIndex += 1
                endWordIndex -= 1
            returnVowelStrings.append(count)
        return returnVowelStrings

# Time Complexity: O(m*k) 
# (where k is the average range size) to O(m) (where m is the number of queries).

"""
    NOTES:
    - When the function is within a class, you must set self parameter. The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
"""

# Version-4 Solution (Success)
# NO ERRORS
class Solution:
    def findVowels(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return word[0] in vowels and word[-1] in vowels

    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        # Step 1: Precompute a boolean list for words that start and end with vowels
        is_vowel_string = [self.findVowels(word) for word in words]
        
        # Step 2: Compute prefix sums for quick range sum queries
        prefix_sum = [0] * (len(words) + 1)
        for i in range(len(words)):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if is_vowel_string[i] else 0)
        
        # Step 3: Process queries using the prefix sums
        result = []
        for start, end in queries:
            result.append(prefix_sum[end + 1] - prefix_sum[start])
        
        return result

# Runtime: 31ms
# Time Complexity O(N+M)
# An O(N) precomputation step to compute the boolean list is_vowel_string, an O(N) precomputation step to compute the prefix sum array, and an O(M) query processing step to compute the result list.

"""
Explanation of Optimizations:
1. Precompute Whether Words Start and End with Vowels:
    Instead of repeatedly checking if each word starts and ends with vowels for every query, this computation is done once for all words using a list comprehension. This results in an O(n) operation, where n is the number of words.
2. Prefix Sum Array:
    To efficiently calculate the count of valid words in any range [start, end], we use a prefix sum array. This array stores the cumulative count of valid words up to each index. By calculating the difference between the prefix sum at the end index and the prefix sum at the start index, we can obtain the count of valid words in the range [start, end]. The prefix sum array is computed in O(n) time. (This remov)
3. Efficient Data Structures:
    Using a set ({'a', 'e', 'i', 'o', 'u'}) for vowels lookup instead of a list improves the time complexity of membership checks from O(n) to O(1).

    Time Complexity:
- Preprocessing:
    - Checking vowels for all words: O(n)
    - Constructing the prefix sum array: O(n)
- Query Processing:
    - Each query is processed in O(1) due to the prefix sum, resulting in O(m) for m queries.

Total Space Complexity:
    Input Storage: 
        O(n+𝑚)
    Auxiliary Storage: 
        O(n+n+1)=O(n)
        O(n+n+1)=O(n)
    Overall:
        O(n+𝑚)

    O(n+m), where n is the number of words and m is the number of queries.



"""