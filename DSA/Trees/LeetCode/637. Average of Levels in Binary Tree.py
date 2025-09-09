# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """similar concept as level order traversal expect that here we are not printing level of arr but sum and taking avg and appending that to the res."""
        if not root:
            return []
        
        res = []
        q = deque([root])

        while q:
            level_sum = 0
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(round((level_sum/size),5))
        return res
        
        