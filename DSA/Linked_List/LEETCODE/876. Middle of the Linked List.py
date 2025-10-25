# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        The intuition here 
        - Is to use hare and tortise algo a.k.a slow and fast pointer
        - slow pointer move one node and fast moves 2 nodes at a time
        - once the fast pointer reachs the end node or outside the linked the slow pointer is at the middle of the linked list
        time and space 
        time = o(n)
        space = o(1)
        """
        # intiliaase slow and fast to point to the head node
        slow = head
        fast = head
        # we only care about fast and fast.next , if fast.next.next is None then its not a problem
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # we made sure fast.next is not none so no issues here
        return slow 


        