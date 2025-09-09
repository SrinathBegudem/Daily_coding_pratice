# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        intution: for level order traversal we use deque and pop left to print level wise and when they ask the level in arr then thats tricky we need another for loop where we pop the elements in q to print level.
        """
        if not root:
            return []
        
        res = []
        q = deque([root])
        while q:

            level = []
            size = len(q)
            # the size of q = len of all nodes in that particular level this is the key idea
            for _ in range(size):
                #while we loop we add all the next level nodes to q and then when size is found for next level it will have all the elemts in that particular level and we continue doing it.
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
        

        