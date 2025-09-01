# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        For this question i can think of 2 approchs 
        first : traverse once to find the len of linked list and remove (len-n).next
 node --> time = two pass o(n+n) = 0(n) , space = o(1)

        second: reverse a linkedlist remove nth node and then return reversed linked list
        the main thing for above 2 sol to work is creating a dummy node.
        """
        return self.optimal_sol_1(head,n)

    def first_sol(self,head,n):
        # main point is to have dummy node other wise all trys will be in vain.
        dummy = ListNode(0,head)
        cur = head
        len_ll = 0
        #pass one to find the len of linkedlist
        while cur:
            len_ll += 1
            cur = cur.next
        #pass two to remove the nth node from last
        steps = len_ll - n
        prev = dummy
        for _ in range(steps):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next

    def second_sol(self,head,n):
        if not head:
            return None
        rev = self.reverse_ll(head)
        dummy = ListNode(0,rev)
        prev = dummy
        for _ in range(n-1):
            prev = prev.next
        prev.next = prev.next.next
        return self.reverse_ll(dummy.next)
            
    @staticmethod        
    def reverse_ll(head_ll):
        prev = None
        cur = head_ll
        while cur:
            nxt = cur.next
            cur.next = prev 
            prev = cur
            cur = nxt
        return prev
    def optimal_sol(self,head,n):
        """
        From basic of maths we can say that we first traverse to the node n and then from there we move both pointers to find the node beforet he node that to be remvoed
        offset (n) =fast - slow
        """
        # lets have a dummy node 
        dummy = ListNode(0,head)
        #slow pointer is pointing towards the dummy node so instead of we being at the node that to be deleted we can be at the before node same goes to above 2 questions too.
        slow = dummy 
        # and the fast ponter begin at head
        fast = head
        for _ in range(n):
            fast = fast.next
        # now once we are at the head + n node we move both pointer so when the fast runs out of linked list and points towards None the slow pointer will be at the node before the node that to be deleted 
        while fast:
            slow = slow.next 
            fast = fast.next
        # the slow pointer is now at before node 
        slow.next = slow.next.next
        return dummy.next

    # there are diff way to sol the optimal methods too 
    def optimal_sol_1(self,head,n):
        """
        🚨 Key takeaway

        Without dummy → you can only safely remove non-head nodes.

        With dummy → you can remove any node (including head) uniformly.

        So while not “mandatory” in theory, in practice dummy makes it robust and avoids edge-case errors.
        """
        dummy = ListNode(0,head)
        slow = fast = dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next