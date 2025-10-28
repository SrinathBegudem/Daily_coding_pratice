# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def optimal_sol():
            """
            The idea here is instead of creating a new modified list lets use the same list and turn the zero to node_sum val
            time = o(n)
            space = o(1)
            """
            cur = head.next
            node_sum = 0
            last_zero = head # overwrite the firs zero
            while cur:
                if cur.val == 0 :
                    last_zero.val = node_sum 
                    last_zero.next = cur.next # we entierly skip the next zero  and catchs its next val and update that node with sum this will aloow us to skip the last zero in the orginal linked list other wise the last zero will always print in the new list  
                    last_zero = last_zero.next
                    cur = cur.next
                    node_sum = 0
                if cur:
                    node_sum += cur.val
                    cur = cur.next
            return head
        return optimal_sol()
            
                





        def brute_force():
            """
            The intuition here is 
            - create summy node to store the new modified linked list 
            - have a node_sum var to cal the sum from one 0 node to another 
            - if cur node val is zero then create a new node put the ndoe sum accumulated till then to that new node and add to our new list and set the node sum to zero for new sum cal
            Time and space 
            - time = o(n)
            -space = o(m)
            """
            dummy = ListNode(0)
            dummy_cur = dummy
            cur = head.next
            node_sum = 0
            while cur:
                if cur.val == 0:
                    dummy_cur.next = ListNode(node_sum)
                    dummy_cur = dummy_cur.next
                    node_sum = 0
                node_sum += cur.val
                cur = cur.next
            return dummy.next
        return brute_force()

                
                