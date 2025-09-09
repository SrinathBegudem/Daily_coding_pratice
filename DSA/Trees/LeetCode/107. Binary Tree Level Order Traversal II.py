# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        intuition is do level order and then return .reverse() and another would be insert at 0th index always instead of append 
        or else we can create res as dequeu and do appendleft 
        """
        if not root:
            return []

        def level_order_reverse(root):
            #time = o(n),space= o(n)
            res = []
            q = deque([root])
            while q: #------> o(n)
                level = []
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(level)
            res.reverse() #------->o(l)where l = levels  l < n (since we have list of list elements we are not reversing all n elements)
            return res
        
        def deque_sol(root):
            #time = space = o(n)
            res = deque([])
            q = deque([root])
            while q:
                level = []
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.appendleft(level)
            return list(res) #O(L) to copy each level reference into a new list. where l = level
    
        def insert_sol(root):
            # time = o(n**2),space = o(n)
            res = []
            q = deque([root])
            while q: #------> o(n)
                level = []
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.insert(0,level)# i guess this is by far worst we move all elemts right for m times 
            return res
        return level_order_reverse(root)
        


