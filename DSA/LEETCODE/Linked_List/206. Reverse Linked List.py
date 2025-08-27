from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Pick any one to return:
        # return self.iter_brute(head)
        # return self.iter_optimal(head)
        # return self.tail_recursion_sol(head)
        return self.true_recur(head)

    # --- Approach 1: Stack (build new list). O(n) time, O(n) space.
    def iter_brute(self,head):
        """
        In the most easiest way we are gonna use stack to store all the node vals
        from the linkedlist and pop to construct a new linked list which is the 
        reverse of the orginal linked list
        Time = O(2N) = O(n) (since its a two pass algorithm)
        Space = O(N) because of val stored in stack.
        """
        # This part also works as utilities to convert LL to List
        if head is None:
            return None

        stack = []
        cur = head 
        while cur:
            stack.append(cur.val)
            cur = cur.next
        # now stack has all the val from listed list 
        # we build a LL using the stack
        new_head = ListNode(stack.pop()) # first node
        tail = new_head
        while stack: # rest of the nodes
            tail.next = ListNode(stack.pop())
            tail = tail.next
        return new_head


    # --- Approach 2: Iterative pointer flip. O(n) time, O(1) space.
    def iter_optimal(self, head):
        """
        we use two pointer approch to optimse the iter sol this approch will reduce the space complexity from O(N) to O(1)
        """
        prev = None 
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt
        head = prev
        return head

    # --- Approach 3: Tail recursion (mirror of iterative). O(n) time, O(n) stack.
    def tail_recursion_sol(self,head):
        """
        Tail recursion is not a true recursion but it is a recursion fucntion calling it self and tail recursion here closely mimic the iter approch but by using the recursion concept, Time = O(n), space = O(n)
        """
        def helper(cur,prev):
        # base case 
            if cur is None:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt
            return helper(cur,prev)
        return helper(head,None)
    
    # --- Approach 4: Post-order recursion (“true recursion”). O(n) time, O(n) stack.
    #post-order-recursion (a.k.a True recursion)
    def true_recur(self,head):
        if head is None or head.next is None:
            return head # returns the last node or empty 
        # lets make post recursion calls (i.e) lets first divide the problem into 
        #subproblem and solve the smallest possible unbreable problem.
        new_head = self.true_recur(head.next)
        # once we reach the last node that is divided the problem which cannot be futhur divided we do the below 
        # the head is last before node and the head.next is last node and the head.next.next is last nodes next we are pointing towards the head which is the last before node 
        head.next.next = head #to undertsand solve an example 
        # this is imp because the last before node pointing towards the last node and the above line we made last node to point towards the last before node so it formed a cycle so we need to point the last befoer node to None
        head.next = None
        return new_head



        