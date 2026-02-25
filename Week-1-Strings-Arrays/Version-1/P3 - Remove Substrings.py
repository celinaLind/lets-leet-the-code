"""
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
	pass
Example Usage:

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
Example Output:

"r"
"eplan"
"Chor"
"""

"""
Substring NOTES:
    word[1:3] - returns the substring from index 1 to index 2 (the 3 is excluded)
    word[:3] - returns the substring from the start of the word string to index 2 (the same as saying word[0:2])
    word[2:] - returns the substring from index 2 to the end of the word string
    word[::2] - returns the substring from index 1 until the end of the word string BUT increments by only returning every 2 characters
        Example: word = "Cheese" 
                 word[::2] = "Ces"
    word[:] - returns a copy of the ENTIRE string

String Built-in Functions:
    in - returns true if substring is found in string
        Ex. if "py" in "python"
    
    find() - returns the starting index in string where substring is found (the first instance), returns -1 if substring NOT found

    index() - returns the starting index like find() BUT returns a ValueError if substring is NOT found

"""

"""
Understand: Create the tiggerfy() function and find the final string after removing all provided substrings from word
    input: word [string to search]
    output: final_word [remaining string value]
    wwk:
        1. Substring list = ['t', 'i', 'gg', 'er']
        2. Substrings are CASE-iNsEnSiTiVE

Plan:
    set sub equal to the list of substrings to find

    iterate over each substring
        set found equal to -10
        while found != -1:
            set found equal to the value returned from the built in find function when called on the word to find the current substring
            if found > -1
                set new_ind equal to the new index
                if found > 0:
                    set word equal to the concatentation of substring word[new_ind:found] and substring word[found+(len(substring)-1)::]
                if found == 0:
                    set word equal to the substring word[found+(len(substring)-1)::]
    return word

Implement:
    See Code Below
"""

def tiggerfy(word): 
    subs = ['t', 'i', 'gg', 'er']

    for sub in subs: 
        found = -10
        if len(word) < 1:
            break
        while found != -1: 
            if len(word) < len(sub):
                break
            found = word.lower().find(sub) # found = 2
            new_end_st = found + (len(sub)) # 4
            if found > 0:
                if new_end_st < len(word)-1:
                    word = word[:found] + word[new_end_st:] # word = "Trer"
                else:
                    word = word[:found]
            elif found == 0:
                if new_end_st < len(word)-1:
                    word = word[new_end_st:] 
                else:
                    word = ""
                    break
                
        
    return word

# Test 1
word = "Trigger"
print(tiggerfy(word))

# Test 2
word = "eggplant"
print(tiggerfy(word))

# Test 3
word = "Choir"
print(tiggerfy(word))