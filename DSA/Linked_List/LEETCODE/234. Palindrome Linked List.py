# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def optimal_sol():
            """
            My intuition here is 
            - i will reverse the linked list up until mid point  
            - then from there i use two pointers to traverse one back to start and other to the end
            - check the vals as i traverse both directions
            key concepts 
            - to find the mid point we can use fast and slow pointers 
            -once the fast pointer run out of nodes then slow pointer is at mid  
            edge cases 
            - increase the fast pointer before rev of sow pointer 
            - take care of odd len, we have to move slow pointer by one in this case bfr we start comparing
            - time = o(n)
            -space = o(1)
            """
            prev = None
            slow = head
            fast = head

            while fast and fast.next:
                #increase the fast pointer by 2 pointer before reversing 
                fast = fast.next.next
                #applying in place rev logic and icnreamenting and parllely increasing the slow pointer by one

                nxt = slow.next
                slow.next = prev 
                prev = slow 
                slow = nxt
                #  #increase the fast pointer by 2 pointer before reversing 
                # fast = fast.next.next (wrong do not increase the fast pinter after rev the ll its a bug)
            #handling the odd len of linkedl ist cases 
            # case 1 if ll len is even the fast pointer directly points out to none and the above code works 
            #case 2 if the ll len is odd then we will have to move our slow pointe one node next so we can perverse the unquie mid val on both side, and to fidn the len of ll is odd we check is fast is at the end of the ll if yes then we have odd len we move one node next our slow pointer 
            if fast: # odd length
                slow = slow.next
            


            #now as the loop breaks the slow pointer goes to the right side till end (right start point)
            right_half = slow
            # PREV NODE is on left start point and goes to the start 
            left_half = prev 
            #now as we traverse we verify each node and proceed forward 
            while right_half and left_half:
                if left_half.val != right_half.val:
                    return False
                left_half = left_half.next
                right_half = right_half.next
            return True if not right_half and not left_half else False
        return optimal_sol()



        def brute_force():
            """
            The intuition here is 
            -traverse linked list and append the values into arr 
            - use two pointers to check if it is palandromic or not
            - time = o(n)
            -space = o(n)
            - same time and space complexity as below code but less complex.
            """
            arr = []
            cur = head
            #traversing and appending the linked list values 
            while cur:
                arr.append(cur.val)
                cur = cur.next
            #two pointer palndromic verification
            l = 0 
            r = len(arr) - 1
            while l < r:
                if arr[l] != arr[r]:
                    return False
                l += 1
                r -= 1
            return True 
        # return brute_force()

        def brute_force1():
            """
            The intuition here is 
            - create a new reversed linked list
            - check the new reversed and the cur linked list 
            - if same panlandromic if not False
            - time = o(n)
            -space = o(n)
            very complex we need to create a new reverse linked list (compelx topic must know but not efficent here)
            """
            def reverse_and_create_new_ll(head_ll):
                """
                We are taking the head of linked list and creating a new reverse linked list 
                """
                #create a new head and point it to null 
                new_head = None
                #point the cur pointer to the head of old ll
                cur = head
                while cur:
                    #create a new node
                    new_node = ListNode(cur.val)
                    #now point new_head.next to new_node ex: 1 (new_node)-> None(new_head)
                    new_node.next = new_head
                    #move the new head to new node ex: 1 (new_head)-> None
                    new_head = new_node
                    #move the cur pointer to next
                    cur = cur.next
                #understood we are moving back wards and returning the new_head, adding the elements in reverse direction
                return new_head
            
            reverse_head = reverse_and_create_new_ll(head)
            rev_cur = reverse_head
            cur = head
            # now i will traverse one by one and check if there is mismatch then i will return false
            while cur and rev_cur:
                if cur.val != rev_cur.val:
                    return False
                cur = cur.next
                rev_cur = rev_cur.next
            return True if not cur and not rev_cur else False
        # return brute_force()


            



                
        