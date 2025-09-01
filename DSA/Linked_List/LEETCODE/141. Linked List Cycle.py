# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.optimal_sol(head)


    def optimal_sol(self,head):
        """
        L = length of the non-cyclic “tail” (from head to first node in cycle)

        C = length of the cycle

        n = total number of distinct nodes

        Phase 1 (entering the cycle):
        In at most L steps, either fast hits None (no cycle) or both pointers enter the cycle.
        Phase 2 (meeting inside the cycle):
        Inside the cycle, the relative speed is 1 node/step (fast gains 1 on slow each loop).
        Starting with some gap g (0 ≤ g < C), they meet in ≤ C steps.
        Total steps ≤ L + C ≤ n + C ≤ 2n ⇒ O(n).
        That’s why it’s efficient: linear time, constant passes (just one traversal loop).
        """
        if not head:
            return False
        fast = head
        slow = head
        while fast and fast.next:
            #check if fast = slow
            fast = fast.next.next
            slow = slow.next
            # if fast == slow: wrong == comparse val we should check the node object (memory adress refernce)
            #     return True
            if fast is slow:
                return True
        return False
    def brute_force_sol(self,head):
        #base condition 
        if not head:
            return False
        # we will have a set that store the object refernce (not just val) so we can lookup in set to see that have we visited that location in memory ever, if yes we are gonna return True as it says us we have linkedlist cycle.
        seen = set()
        cur = head
        while cur:
            #check if we have visited this node 
            if cur in seen:
                return True
            #add the cur to seen
            seen.add(cur)
            #if not move to next node
            cur = cur.next
        #once the loop is terminated it means it doesnot have cycle so return False
        return False