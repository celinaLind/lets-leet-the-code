# Imagine you're maintaining a dynamically updating list of tasks to complete stored in a linked list, where each node represents a task.
# Your goal is to selectively remove a task based on its position from the end of the list to update your schedule.
# Specifically, given the head of a linked list as your starting point, eliminate the task/node that is 'n' positions from the list's end and then return the updated list's head.
 
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
 
# Example 2:
# Input: head = [1], n = 1
# Output: []
 
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
 
# Constraints:
# The total number of tasks/nodes in the list is given by sz.
# Each task/node's value ranges between 0 and 100, inclusively.
# The size of the list, 'sz', will be at least 1 and no more than 30.
# 'The position 'n' to remove from the end must satisfy 1 <= n <= sz.

# Definition of singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def trimListFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Two-pointer technique
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # while the position for deletion is > 0 and right is not null
    while n > 0 and right:
        # this is setting the position of right to validate when the end of the list is where left will be at the node right before the node meant for deletion
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # delete node
    # since left is equal to the dummy list it will update the dummy list nodes as well
    left.next = left.next.next # connects the prevNode to the afterNode

    return dummy.next

    #Ex. a -> b -> c would become a -> c

    # Time Complexity O(n)
    # Space Complexity O(1)