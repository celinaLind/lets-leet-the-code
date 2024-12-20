## Lexicographical Order

A way of sorting strings, similar to alphabetical order but generalized to all kinds of characters.

When comparing two strings, s and t, we compare each pair of characters with equal indices (s[i] and t[i]), starting with i = 0:

if s[i] < t[i] or if s[i] is undefined, then we conclude that s < t,
if s[i] > t[i] or if t[i] is undefined, then we conclude that s > t,
if s[i] = t[i] then we repeat the process by comparing s[i + 1] to t[i + 1].
If the two strings have equal length and s[i] = t[i] for every character, then we conclude that s = t

Examples:

"snow" > "snoring" because the first string contains a greater character at index i = 3
"cat" < "caterpillar" because the first string is undefined at index i = 3
"9" < "A" because numbers are lexicographically smaller than uppercase English letters
"Z" < "a" because uppercase English letters are lexicographically smaller than lowercase English letters
