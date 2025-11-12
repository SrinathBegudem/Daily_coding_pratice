# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        The idea is simple
        - run dfs and collect the leaf nodes for 2 diff tree for 2 diff res 
        - comapre them.
        """
        res1 = []
        res2 = []

        def dfs(node,res):
            if not node: return 
            if not node.left and not node.right: res.append(node.val)
            dfs(node.left,res)
            dfs(node.right,res)
        dfs(root1,res1)
        dfs(root2,res2)
        # print(res1,res2)
        if len(res1) != len(res2): return False
        for i in range(len(res1)):
            if res1[i] != res2[i]:
                return False
        return True

        