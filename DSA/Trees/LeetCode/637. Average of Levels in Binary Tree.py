# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def bfs(node):
            """
            level order traversal(bfs) + cur_level_sum / size_level , append it to the res after endo f cur level
            """
            q = deque([node])
            res = [] 
            while q:
                level_size = len(q)
                level_sum = 0 
                for _ in range(level_size):
                    #prcoess the node
                    node = q.popleft()
                    # add to the cur_level sum
                    level_sum += node.val
                    #add its children 
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                avg_level = level_sum/level_size
                res.append(avg_level)
            return res
        return bfs(root)



        