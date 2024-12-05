# You're provided with the head node of a singly linked list.
# Your task is to determine whether the list contains a loop.
# A loop occurs when a node's next pointer points to a previously visited node, allowing for infinite traversal.
# Note, the list's tail may link to any node within the list, creating this loop; however, the exact position (pos) of this linkage is unknown to you and not directly provided.
# Your function should return true if a loop is detected within the list, otherwise false.
 
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: A loop is present, as the tail connects to the second node (1st in 0-based index).
 
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: The list forms a loop by linking the tail to the first node.
 
# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: No loop is present as the list's tail does not connect to any node within the list.
 
# Constraints:
# - The list's length ranges from 0 to 10^4 nodes.
# - Node values can range between -10^5 and 10^5.
# - The 'pos' value, representing the index of the tail's linkage, could either be -1 indicating no loop, or any valid index within the list.

# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head: Optional[ListNode], pos: int) -> bool:
    # If the list is empty or has only one node without a cycle, return False
    if not head or not head.next:
        return False

    # this allows us to verify our tortoise and hare method
    # by creating cycles for testing based on the position provided
    # Introduce the cycle using the pos parameter if pos is not -1
    if pos != -1:
        # Find the node at the position `pos` where the cycle should start
        cycle_entry = head
        for _ in range(pos):
            cycle_entry = cycle_entry.next

        # Traverse to the end of the list
        end = head
        while end.next:
            end = end.next

        # Create the cycle by linking the last node to the cycle entry node
        end.next = cycle_entry

    # Initialize two pointers, slow and fast, both starting at the head of the list
    slow = head
    fast = head

    # Traverse the list with the two pointers
    while fast and fast.next:
        # Move the slow pointer by one step
        slow = slow.next

        # Move the fast pointer by two steps
        fast = fast.next.next

        # If the slow pointer and fast pointer meet, a cycle exists
        if slow == fast:
            return True

    # If the fast pointer reaches the end of the list, there is no cycle
    return False