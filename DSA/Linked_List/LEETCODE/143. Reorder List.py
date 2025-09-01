# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        return self.optimal_approch(head)
    def My_first_attempt(self,head):
        #base case 
        if not head or not heat.next:
            return
     # Step 1: Find the middle of the linked list using fast/slow pointers
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

    # Step 2: Split the list into two halves
        # we found the middle node, now our goal is to reverse the second half of the ll 
        # created a new var for second half and then i will detach it with the first half
        new_head = slow.next # second half head 
        slow.next = None # detach the first half with second half
    # Step 3: Reverse the second half ( also create a reverse of ll helper function)
        # reverse the second half ( second half is now just like a new linekd list. so basic revrse ll concept)
        prev = None
        cur = new_head
        while cur:
            nxt = cur.next # storing the rest of the linkedlist before reverse the pointer of cur linked 
            cur.next = prev # turing the cur linked list to prev 
            prev = cur # moving the prev to cur before we change the cur to nxt node.
            cur = nxt # moving cur to the previously stored ll 
        # once while loop break prev will be on the last node which is the head of the reversed linked list
        new_head = prev
        # now lets merge join the two linked lists
        right = head
        left = new_head
        while right and left: 
            #before manipulating the pointer (reordering) left save the rest of both linkedlist to temp var 
            right_nxt = right.next
            left_next = left.next
            right.next = left 
            left.next = right_nxt
            right = right_nxt
            left = left_next 
        
    def optimal_approch(self,head):
        """
        This is a wonderful and must solve question that uses, fast and slow pointer for middle point, reverse a ll concept, merging ll concept.
        """
        #base case:
        if not head and not head.next:
            return 
        # step 1 : Find the middle of the linkelist using totrise and hare concept
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # note always do a dry run on a example to see where the slow pointer is 
        # we will have more nodes in the first half compared to the second half and it works for this problem 

        #step2: detach the first half and second half so we can rev the second half
        #before detaching store the second half in new var
        second_half = slow.next
        #detach
        slow.next = None

        #step3: reverse the second half (use helper function)
        second_half = Solution.reverse_ll(second_half)

        #step4: merge ( this is very imp step)
        first_half = head
        while first_half and second_half:
            # before manipluting pointers store the rest in temp vars
            temp1 = first_half.next
            temp2 = second_half.next
            #the first half next pointer points towards the second half (dry run to understand)
            first_half.next = second_half
            second_half.next = temp1
            # increment the pointers
            first_half = temp1
            second_half = temp2


    @staticmethod
    def reverse_ll(ll_head):
        # lets have a prev node pointing towards None and cur var to cur_head
        prev = None 
        cur = ll_head
        # run the loop until cur is None 
        while cur:
            # store cur.next in new var before we reverse the pointer of that node so we dont loose the rest of ll 
            nxt = cur.next
            #now reverse the cur node pointer to point towards prev 
            cur.next = prev 
            # then move the prev pointer to the cur and after that only change the cur to nxt
            prev = cur 
            # now change the cur to nxt
            cur = nxt 
        #at the end the new head is the prev node 
        return prev 

        


            
    







        

        