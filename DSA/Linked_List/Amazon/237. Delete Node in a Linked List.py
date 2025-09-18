# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # wonderful concept just copy the next val to the cur node and then point the cur.next to point towards cur.next.next, so what happens is the cur.next node is entierly skipped so one less node in linked list and the cur node val is eliminated.
        cur = node
        cur.val = cur.next.val
        cur.next = cur.next.next