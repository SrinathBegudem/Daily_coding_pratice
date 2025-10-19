#-------------------second attempt -----------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def brute_force():
            """
            The intution here is 
            -have 2 pointers l1 and l2 
            -compare vals and move the pointers 
            - while comapring create a new linked list and copy those values 
            - we are creating a new linked list 
            - time = o(n+m)
            -space = o(n+m)
            """
            dummy = ListNode(0)
            cur = dummy 
            l1 = list1
            l2 = list2
            while l1 and l2:
                #comapre 
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
                cur = cur.next
            # after one of the l1 and l2 breaks add the rest to the cur 
            #if l1 is left off lets add it to end of cur 
            #dont do the below because we are trying ot create a new linked list but we just attached the new to old l1 and l2 so its mix of half new and half old .
            # if l1: cur.next = l1 
            # if l2: cur.next = l2 
            while l1:
                cur.next = Listnode(l1.val)
                l1 = l1.next
                cur = cur.next
            while l2:
                cur.next = ListNode(l2.val)
                l2 = l2.next
                cur = cur.next
            return dummy.next
        # return brute_force()

        def optimal_sol():
            """
            now lets try to do inplace merging if possible to optimse space.
            The rule

            Inside a function body, if a name is assigned anywhere (e.g., x = ..., x += 1, x: int = 0), Python treats that name as a local variable for the entire function, unless you declare it with:

            global x (to use the module-level variable), or

            nonlocal x (to use a variable from an enclosing non-global function).
            example so if i do 
            while list1 and list2: #(the error unbound local.)
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = lisst1.next # now this is a problem we get unboundlocal error now this list 1 is treated as local and it will through eroor at while loop 
            
            and the above problem arise only when we use nested loop and inner function does not have para declared in function aurg
            The error happens when an inner function both reads a name from an outer scope and assigns to that same name inside itself. Python then marks that name as local to the inner function, so the earlier read becomes a read-before-assign → UnboundLocalError.

If you give the inner function its own parameters (e.g., pass list1, list2 in), then those names are locals to the inner function, so reading and reassigning them is fine. You just won’t modify the outer variables unless you return something or use nonlocal.
            
            time = o(n+m)
            space = o(1)
            """
            dummy = ListNode(0)
            cur = dummy 
            l1 = list1 
            l2 = list2
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 if l1 else l2
            return dummy.next
        return optimal_sol()
                












#----------------------- first attempt----------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time = o(n+m)
        space = o(1)
        Time complexity is O(m + n), which is equivalent to O(max(m, n)), but I’ll use O(m + n) to emphasize we traverse both lists fully.
        """
        # this is overly verbose base case the simple and brilliant way is below
        # if not list1 and not list2:
        #     return None
        # if not list1  and list2:
        #     return list2
        # if list1 and not list2:
        #     return list1
        # simple base case
        if not list1:
            return list2 # so if both are empty ultimately None will be returned
        if not list2:
            return list1

        dummy = ListNode(0)
        cur = dummy
        # print(list1,list2)
        # Merging
        while list1 and list2:
            # print(cur)
            #check if the val of lst1 < lst2
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        # the below code is overly complicated so this is linked list so we can just change the pointer no need for while loop like arrays 
        #now lets add the left over to the end 
        # while list1:
        #     cur.next = list1
        #     list1 = list1.next
        #     cur = cur.next
        # while list2:
        #     cur.next = list2
        #     list2 = list2.next
        #     cur = cur.next
        # print("d",dummy.next)
        #pythonic single liner 
        cur.next = list1 if list1 else list2
        # or we can also write 
        # if list1:
        #     cur.next = list1
        # else:
        #     cur.next = list2
        return dummy.next


        