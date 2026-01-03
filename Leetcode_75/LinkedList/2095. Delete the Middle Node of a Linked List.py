# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse till mid -1 one node and smiply skip the middle 
        # have prev pointer helps a lot and cur pointer reachs mid  then we can attach directly
        # the above approch works if we know the n so we dont know , it means we definetly need to use tortise and  hare concept
        if not head or not head.next: return None
        slow = head
        fast = head 
        prev = None
        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast  = fast.next.next

        prev.next = slow.next if slow.next else None
        return head

