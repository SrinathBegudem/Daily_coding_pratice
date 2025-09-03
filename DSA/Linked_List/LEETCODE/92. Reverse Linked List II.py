# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # we will have to code this question in 3 phrase and we are going to do only one pass. 
        #phrase 1:
        #  we intialize a dummy node most of the times this dummy node take cares of unseen edge cases and intialize 2 pointers one starts with dummy node and the other with the original head.
        dummy = ListNode(0,head)
        left_prev = dummy 
        cur = head
        # now let me run a loop till i reach the left position (here if we can see ex1 for our pointer to reach position 2 we need to make 1 jump, so we are goona run the loop till left -1)
        for _ in range(left-1):
            cur = cur.next
            left_prev = left_prev.next
        left_node = cur # be care dont assign to left because left is already there in args
        # Phrase2:
        #now lets reverse the ll from left to right. so we have cur pointer pointing towards the left position and we have prev_left node saved for future manplications now you can see from example 1 that there are 3 nodes to be reverse and if we do right - left 4-2 we get 2 so to handle this edge case we do right - left +1 
        prev = None
        for _ in range(right-left+1):
            #lets save the next node before we manuplicate the strings
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt
        right_node = prev
        right_nxt = cur # just assigned for clarity we can directly used cur too
        # so after this loop the prev will be on right node and cur will on right_nxt node.
        #phrase3 : pointer adjustments 
        # now final pointer adjustments
        # we have the left prev pointer stored in left_prev and right next pointer stored right_nxt and the right position pointer in right so left_prev.next should be attached to right and we have left position pointer stored in left so the left.next should be attached to right_nxt
        left_prev.next = right_node
        left_node.next = right_nxt
        return dummy.next

