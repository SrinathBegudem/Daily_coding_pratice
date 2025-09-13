# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.sameTree(p,q)



    def sameTree(self,p,q):
        def dfs(node1,node2):
            # Both are None → same
            if not node1 and not node2:
                return True
            # One is None, the other not → different
            if not node1 or not node2:
                return False

            return (node1.val == node2.val) and dfs(node1.left,node2.left) and dfs(node1.right,node2.right)
        return dfs(p,q)
            

    

    def bfs(self,p,q):
        q = deque([(p,q)])
        while q:
            node1,node2 = q.popleft()

            if not node1 and not node2: 
                continue
            if not node1 or not node2: 
                return False
            if node1.val != node2.val: 
                return False

            q.append((node1.left,node2.left))
            q.append((node1.right,node2.right))
        return True
                
        