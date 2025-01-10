"""
Medium Problem

DESCRIPTION:

"""

# Solution

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # create hashmap by setting defaultdict()
        count_word2 = defaultdict(int)

        # Go through and count how many characters are in each word2
        for w in words2:
            count = Counter(w) # Counter is a function provided by python
            for val, count in count.items(): #use .items() to view data in hash
                # get max count and merge into count_word2 hash
                count_word2[val] = max(count_word2[val], count)
        result = []
        # now count char in word1
        for w in words1:
            count_1 = Counter(w)
            flag = True
            for val, count in count_word2.items():
                if count > count_1[val]:
                    flag = False
                    break
            if flag:
                result.append(w)

        return result


"""
Learned:

    Counter() - this function takes in a string and returns a hash of each character and there count within the string
    Ex. Counter("apple") => ({a: 1, p: 2, l: 1, e: 1})

    - To Use:

    1. items()
    for key, countValue in variable.items(): ....
    2. keys() => returns the key or in this case character being counted
    3. values() => returns the count

    - Can make a list of ALL using the keys() of values() functions
    x_keys = list(x.keys())
    x_values = list(x.values())


    defaultdict(dataType)
    - this is how you can initialize a hash


"""

# Better Alternative
# Runtime: 73ms

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = set(words1)
        letters = {}
        for i in words2:
            for j in i:
                count = i.count(j)
                if j not in letters or count > letters[j]:
                    letters[j] = count
        for i in words1:
            for j in letters:
                if i.count(j) < letters[j]:
                    ans.remove(i)
                    break
        return list(ans)