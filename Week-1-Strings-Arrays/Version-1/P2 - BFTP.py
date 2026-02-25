"""
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

def final_value_after_operations(operations):
	pass
Example Usage:

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
Example Output:

2
4
"""

"""
Understand: create the final_value_after_operations() function along with its subset methods: bouncy(), flouncy(), trouncy(), pouncy()
    input: list of "operation" strings for the main function to complete
    output: integer value received after completing all operations listed
    what we know [wwk]: 
        1. initial tigger value is 1
        2. bouncy and flouncy ++ tigger value
        3. trouncy and pouncy -- tigger value
    
Plan:
    set tigger value equal to 1

    Iterate over each item in operations list
        if item is equal to "bouncy" or "flouncy" 
            increment tigger variable by 1
        if item is equal to "trouncy" or "pouncy"
            decrement tigger variable by 1
    
    return final tigger value found

Implement:
    See code below
"""

def final_value_after_operations(operations):
    tigger = 1

    for op in operations:
        op = op.lower()
        if op == "bouncy" or op == "flouncy":
            tigger += 1
        elif op == "trouncy" or op == "pouncy":
            tigger -= 1

    return tigger

# test 1 
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

# test 2
operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))