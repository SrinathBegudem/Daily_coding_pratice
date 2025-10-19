#2nd sol 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def brute_force():
            """
            The basic simple intuition is 
            - have set 
            - traverse along the linked list and append eeach node into set
            - check if the cur node is already in set 
            - if yes then we have a linked list cycle 
            key points 
            - if you add a node into set, the obj reference (address will be added like obj at <xoas19239r> not the node val or rthe whole next linked list), so even if you change the val it will be able still identify the node.
            - time = o(n)
            -space = o(n)
            """
            seen = set()
            cur = head 
            while cur: 
                #check if cur is in seen 
                if cur in seen:
                    return True
                seen.add(cur)
                cur = cur.next
            #if not returned inside the loop no linked list cycle 
            return False
        # return brute_force()
        def optimal_sol():
            """
            The intuition here is 
            - instead of having a seen there is imprtant pattern or concept in linked list called tortise and hare also known as slow and faster pointer 
            - In this concept slow pointer moves one node at a time 
            - faster pointer moves two nodes at a time 
            - so if there is cycle the faster pointer can quickly able to catch the slow pointer.
            - time = o(n)
            -space = o(1)
            """
            #edge case if no head then fast.next will throw an eroor
            if not head: return False
            
            slow = head
            fast = head
            while fast and fast.next:
                #The loop condition is evaluated left → right with short-circuit.
                #We only enter the body if both are true:
                        # fast is not None
                        # fast.next is not None
                       #Since we already guaranteed fast.next exists, accessing fast.next.next is safe.
           # fast.next.next may be None, and that’s fine—we simply set fast = None. We are not doing None.next; we’re assigning    None to fast.
                
                #increment slow pointer by one node
                slow = slow.next
                #fast pointer by two by nodes 
                fast = fast.next.next
                if fast is slow: # is operator checks the obj address that is exactly what we want here not just node.val comparision
                    return True # linked list cycle exisits 
            #once the while loops break there is no linked list cyle
            return False
        return optimal_sol()











#1st sol
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