# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        level order traversal(bfs) + max_var for that particular level instead of having whole level list have this var adn end of cur level push this max_var to res
        """

        def bfs(node):
            if not node:return []
            res = []
            q = deque([node])
            while q:
                size = len(q) # cur_level size
                max_val = float("-inf") # need smallest val as possible for intial val
                for _ in range(size):
                    #process the node
                    node = q.popleft()
                    # check if the cur node val is max val, and update
                    if node.val > max_val: max_val = node.val 
                    # add the child node to the queue
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                #ater the cur_lvl is done push the max_val to res
                res.append(max_val)
            return res
        return bfs(root)


        