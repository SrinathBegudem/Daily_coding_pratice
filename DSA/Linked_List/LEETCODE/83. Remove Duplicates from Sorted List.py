# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Key points:
        - Given a sorted linked list, that means we can comapre the adjacent nodes
        The intuition here is:
        - same like arr we have two pointer prev and cur and compare them
        - if prev == cur , then move the cur var to nxt
        - join prev.next to cur when a non repeated element is encountered
        Time and space:
        - time = o(n)
        - space = o(1)
        """
        #edge case if not head then head is None so we return head (which is also None) and if head.next is none we return head ( so works for both cond)
        if not head or not head.next:
            return head
        #prev pointer pointing towards head
        prev = head 
        # so in edge case we must make sure tht head.next is not None if we didnt code the edge case at the top this might give None type not has .next error
        cur = head.next

        while cur:
            #check if cur == prev or not if yes move the pointer
            # i used while loop so we can skip all the duplicates and always check if cur is not none in first condition
            while cur and cur.val == prev.val:
                cur = cur.next
            # after the above loop breaks we attach prev.nect to cur
            prev.next = cur
            #move prev pointer
            prev = cur 
            #so from nested while loop there might be chance that cur is None so we have to check that with if cond to avoid None type .next error
            if cur: cur = cur.next
        return head

#-------chatgpt_sol--------
    #    cur = head                      # O(1)
    #     while cur and cur.next:         # O(n) total iterations
    #         if cur.val == cur.next.val: # O(1)
    #             cur.next = cur.next.next# O(1) skip duplicate node
    #         else:
    #             cur = cur.next          # O(1) advance when values differ
    #     return head    
        