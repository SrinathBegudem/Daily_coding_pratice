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


        