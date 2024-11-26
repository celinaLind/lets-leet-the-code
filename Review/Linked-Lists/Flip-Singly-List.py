# Imagine you are working with a sequence of data represented as a singly linked list, and you're required to rearrange this sequence in reverse order.
# Your task is to write a function that takes the first element (head) of this list, reverses the entire sequence of elements, and returns the head of the newly reversed list.
 
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
 
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
 
# Example 3:
# Input: head = []
# Output: []
 
# Please note that the number of elements within the list can range from 0 to 5000, and the value of each node falls between -5000 and 5000.

# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    #Initialize pointers for current position and previous position
    currentPos = head #starts on the head node
    previousPos = None # None so the last node in the reversed list will point to None
    
    #currentPos is going to be the current linked list tracker
    # previousPos is going to be the new reversed linked list

    while currentPos is not None:
        # temporarily store the next node for modification done to currentPos.next
        temp = currentPos.next
        currentPos.next = previousPos 
        previousPos = currentPos 
        currentPos = temp

    return previousPos

    # Time Complexity O(n)
    # Space Complexity O(1)