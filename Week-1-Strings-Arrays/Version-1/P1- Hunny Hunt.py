"""
Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in items. Do not use any built-in functions.

def linear_search(items, target):
	pass
Example Usage:

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)


Example Output:
3
-1
"""

"""
UPI Method:

    -- Understand --
        Input: items (list of strings), target (string value to find)
        Output: Return the FIRST index where target is found 
        Criteria/Restrictions: Do NOT use built in functions [len, find, etc]
    -- Plan -- 
        Set 'count' variable equal to zero
        Create a for loop for every item in items list
            add one to the 'count' variable on each iteration
        create a for loop using index values starting at 0 through the value of count found above
            compare the string at current index of list to the target string
                if the values are the same return the index
                else continue loop

        if the code gets here, that means there is no value in the items list equal to the target string
        return -1

    
    -- Implement --
        See code below
"""

def linear_search(items, target):
    count = 0

    for item in items:
        count += 1
    
    if count != 0:
        for i in range(count):
            if items[i] == target:
                return i
    
    return -1


# Test 1
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

# Test 2
items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))