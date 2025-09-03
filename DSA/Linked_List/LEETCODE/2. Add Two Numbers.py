# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        The reverse linked list acutally helps us bcz anyways we are going to add from the right itself so and here we learn the important concept of carry.
        """
        # create a var carry 
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2 or carry:
            # key point is to store the val in var not directly added l1.val + l2.val
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            
            val = v1 + v2 + carry 
            carry = val // 10 
            val = val % 10 
            cur.next = ListNode(val)

            # increment pointers 
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


    
  