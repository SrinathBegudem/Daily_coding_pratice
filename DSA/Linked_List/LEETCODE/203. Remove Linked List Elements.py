# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def my_sol():
            """
            The intuition here is 
            - traverse the array 
            - we need to have prev (dummy) node pointer and cur node pointer 
            - if the target val found 
            - skip that node by advancing the cur pointer until the non target node if found
            - once the non target pointer found set the prev.next to that node and advance prev node to cur node and cur to cur.next
            key points:
            - have prev and cur pointer make things easily 
            -we have to traverse till the end and remove all target node not just once
            time and space 
            - time = o(n)
            -sapce = o(1)
            """
            dummy = ListNode(0,head)
            prev = dummy
            cur = head
            while cur:
                if cur.val == val:
                    # if cur val == target val, advance the pointer to next node and cotinue until non target val is found 
                    cur = cur.next
                    continue
                #once the non target val found then point the prev.next to that node
                prev.next = cur 
                #move the prev to cur node 
                prev = cur 
                #and cur node to next node
                cur = cur.next
            prev.next = cur
            return dummy.next

#------------------claude sol and standard approch -------------------
        def claude_sol():
            """
            ✅ CLEANEST SOLUTION
            
            Key insight: Check curr.next instead of curr
            This way we can easily remove curr.next by skipping it
            
            Time: O(n) | Space: O(1)
            """
            dummy = ListNode(0, head)
            curr = dummy  # ✅ Start from dummy
            
            while curr.next:  # ✅ Check next node
                if curr.next.val == val:
                    # ✅ Remove next node by skipping it
                    curr.next = curr.next.next
                    # ✅ DON'T move curr - check new next node
                else:
                    # ✅ Keep next node, move forward
                    curr = curr.next
            
            return dummy.next

