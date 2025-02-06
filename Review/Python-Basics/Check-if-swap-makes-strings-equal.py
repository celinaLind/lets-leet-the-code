

# Successful Solution

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff = 0
        if sorted(s1) != sorted(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if diff >2:
                    return False

        return True if diff == 2 or diff == 0 else False
    

# Better Solution with time complexity

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        c = 0
        arr = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                arr.append(s1[i])
                arr.append(s2[i])
                c += 1
        if c == 2 and len(set(arr)) == 2 and arr[0] == arr[3] and arr[1] == arr[2]:
            return True
        return False
