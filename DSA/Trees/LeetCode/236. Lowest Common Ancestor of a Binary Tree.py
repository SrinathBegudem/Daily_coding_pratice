# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            #base case 1 : if not node
            if not node: return node 
            #base case 2 ; if p or q found return that node 
            if p == node or q == node:
                return node # return that node 

            #recurse left and right classic dfs
            left = dfs(node.left)
            right = dfs(node.right)

            #case1: p and q are found in differrent subtrees -> node is LCA
            if left and right: return node

            #case2: both are on left subtree or right subtree return the node of that subtree
            return left if left else right
        return dfs(root)
