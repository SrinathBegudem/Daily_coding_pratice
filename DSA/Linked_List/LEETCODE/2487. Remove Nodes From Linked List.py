# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def optimal_sol():
            """
            The inutition here is instead of start from righ to left, start from left to right
            - have a max_pointer to update the max we have seen prevsly
            - i the cur node val is less than the max_val simple skip the node
            Time and Space 
            time = o(n)
            space = o(1)
            """
            def reverse(head_ll):
                prev = None
                cur = head_ll
                while cur:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur 
                    cur = nxt
                return prev
            
            # reverse the ll so we can traverse in opp dir 
            rev_head = reverse(head)
            cur = rev_head
            cur_max = cur.val
            # the last node always stays 
            while cur.next:
                if cur.next.val < cur_max:
                    #skip that node
                    cur.next = cur.next.next # for this reason we do while cur.next is not none
                else:
                    #we foudn another max val so update the max_val 
                    cur_max = cur.next.val
                    cur = cur.next
            return reverse(rev_head)

        return optimal_sol()

        def brute_force():
            """
            I think we can use monotonic stack for this problem
            _ the concept of monotic stakc is very interesting 
            - we add all the values to the right into the stakc until the greater element is found 
            - once found we pop elements from stack until stack[-1] > greater val we found 
            - in short Every time a bigger value appears, it eliminates all smaller ones before it (to its left).
            Time and Space 
            - time = O(n)
            - space = o(k)
            """
            stack = []
            cur = head
            stack.append(cur.val)
            cur = cur.next if cur.next else None
            while cur:
                while stack and cur.val > stack[-1]:
                    stack.pop()
                stack.append(cur.val)
                cur = cur.next
            
            dummy = ListNode(0)
            cur = dummy
            for val in stack:
                cur.next = ListNode(val)
                cur = cur.next
            return dummy.next
                
            





                