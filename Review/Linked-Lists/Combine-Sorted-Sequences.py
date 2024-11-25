# Imagine you are working with two databases that store user information in ascending order based on user IDs.
# Your task is to integrate these databases into a single, organized database, while maintaining the ascending order of user IDs.
# Represent each database as a sorted linked list, where each node contains a user ID.
# You are required to merge these lists into one sorted list without altering the original databases' structures, effectively creating a new list that combines the elements from the original lists in ascending order.
# Return the head of this newly merged list.
 
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
 
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
 
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
 
# Constraints:
# Each list's size may range from 0 to 50 nodes.
# Node values may range from -100 to 100.
# Both list1 and list2 are sorted in non-decreasing order.

# Definition of a singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeDatabases(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a new ListNode to act as the head of the merged list.
    head = ListNode()
    # 'current' is used to keep track of the current node in the merged list.
    current = head

    # Continue looping as long as both lists have nodes to process.
    while list1 and list2:
        # Compare the values of the current nodes in both lists.
        if list1.val < list2.val:
            # If list1's current node is smaller, append it to the merged list.
            current.next = list1
            # Move to the next node in list1.
            list1 = list1.next
        else:
            # If list2's current node is smaller or equal, append it to the merged list.
            current.next = list2
            # Move to the next node in list2.
            list2 = list2.next
        # Move to the next node in the merged list.
        current = current.next

    # At this point, at least one of the lists is empty.
    # If there are remaining nodes in list1, append them to the merged list.
    if list1:
        current.next = list1
    # Otherwise, append the remaining nodes of list2 to the merged list.
    else:
        current.next = list2

    # Return the next node of the 'head' node, which is the start of the merged list.
    return head.next


