# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

#two-pointer switching technique.
        def optimal_sol():
            """
            The idea here is same as good sol but instead of finding len of both node we do something more brave and less intuitive
            both of optimal and good sol have same time and space complexity but its just way we code 
            - we have 2 pointers one at A ll head and other at b linked list head
            - now we traverse both ll and the short linked list is the one which run out of the list and when it happen we set its last node to the head of the Bigger linkedlist 
            - and the bigger linked list goes on until its None the next pointers once it reached , then we set the next node to small node head and in mean time the small ll pointer which we made to point to bigger linked ll head will now we at the same len of bigger pointer which is now at the head of the smaller linked list
            - so its simple once we ran out of smaller linked list we move the last pointer to bigger and skip until the bigger is done and points it self to the head of small now both big and small are at same len apart from interesection if exisits if not they will both meet at the end of the LL which is None.
            Time and Space 
            time - o(m+n) same we traverse the linkedlist twice 
            space - o(1) same as good sol but very less intutive than good_Sol
            """
            # two pinters 
            cur_a = headA
            cur_b = headB
            
            #we traverse until both node match or become None. None is a singleton in python means there is exactly one instance of it in all of the python runtime.
            # and never set cur.next = headB this mutates the linked list creating infinite loop
            while cur_a != cur_b: 
                # set cur to next node if cur_a exisit other wise to the head of another node
                cur_a = cur_a.next if cur_a else headB
                # likewise 
                cur_b = cur_b.next if cur_b else headA
            # they either meet at match or None 
            return cur_a #or cur_b

        return optimal_sol()


        def good_sol():
            """
            The intuition here is 
            - traverse both the ll and find out the len of both
            -now traverse the big ll until it matchs the len of small (i.e traverse until len(big) - len(small))
            -now point ll are at the same len to its intersection point if exists 
            - now increase both pointer until match 
            - if not match return None 
            Time and Space 
            - time = o(m+n)
            - space = o(1)
            """
            a_len = 0  #5
            b_len = 0 # 6
            cur = headA
            #step1: find the len of ll A
            while cur:
                a_len+= 1
                cur = cur.next

            #step2: find the len of ll B
            cur = headB
            while cur:
                b_len += 1
                cur = cur.next
            
            #step3 traverse the big linked list until they both ahve same start point len 

            big_ll,small_ll = (headA,headB) if a_len > b_len else (headB,headA) # (headB,headA)
            skip_len = abs(a_len - b_len) 
            for _ in range(skip_len): # range of 1 
                big_ll = big_ll.next # skipped it once so now ur at node 2 
            
            #step4 now both big_ll and small_ll are at same point so we traverse both until match

            while big_ll and small_ll:
                # checking the obj refernce to find the match 
                if big_ll is small_ll:
                    return big_ll # or smal_ll this is the first matched node
                
                #else increase both pointers 
                big_ll = big_ll.next
                small_ll = small_ll.next
            return None # if no match 
        # return good_sol()



        def brute_force():
            """
            The intuition here is 
            - have a set traverse the ll A and save all nodes in that set 
            - and when you traverse ll B and chekcif node already exisit in set 
            - if yes we found the first intersection point ,return the node
            - if not no intersection return None
            time and space 
            -time = o(n+m)
            -space = o(no of node in ll A)
            """
            seen =set()
            curA = headA
            while curA:
                seen.add(curA)
                curA = curA.next
            curB = headB
            while curB:
                if curB in seen:
                    return curB
                curB = curB.next
            return None
        # return brute_force()