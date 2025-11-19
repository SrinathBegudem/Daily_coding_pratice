# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        """
        The key optimisation is convert the list to set, which makes look up o(1)
        rest all is the same code as lca 1
        """
        nodes = set(nodes) # this takes one o(n) to build the set and from then o(1) lookups if not we directly use lsit then it gonna makes mutiple iteration of o(n) to find single element every single time 
        def dfs(node):
            if not node: return None

            if node in nodes: #this is o(1) if set else mutiple times o(n) if list
                return node 
            left = dfs(node.left)
            right = dfs(node.right)

            if right and left:
                return node
            return left if left else right
        return dfs(root)
