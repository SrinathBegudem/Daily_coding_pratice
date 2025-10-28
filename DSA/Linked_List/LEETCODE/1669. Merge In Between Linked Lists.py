# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        """
        The intuition here is 
        - I will first traverse the list2 to find the tail pointer and have both head and tail pointers read 
        - Then i will traverse until the range of b 
        - In the process i will have a check once the len of a is reached i will save it as a_before node 
        - then traverse till b to find b_after node 
        - now i will attach a_before to the head of list2 and then tail of list2 is attached to b_after
        Time and Space
        time = o(m+n)
        space = o(1)
        """
        #step 1 traverse the list2 to find the tail poitner 
        cur = list2
        tail = None
        while cur:
            tail = cur
            cur = cur.next
        #step 2 traverse till range of point b and store both a before and b after nodes
        a_before = None
        b_after = None
        cur = list1
        for i in range(1,b+1): #runs 4 times for ex 1 
            if i == a: 
                a_before = cur
            cur = cur.next 
        #now we are at bth node but we need b+1th node 
        b_after = cur.next
        #step 3 is to attch the pointers
        #attach a_after to list2 head
        a_before.next = list2
        #tail of list 2 to b_after
        tail.next = b_after
        return list1
            
    