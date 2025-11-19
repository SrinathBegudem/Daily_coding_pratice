# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        The key idea here is 
        - we return 2 values the LCA and depth 
        - so at a particular level we check the depth 
        - case 1: if both depths are eq the parent node can be LCA so we return it
        - case 2: if one depth is more than another then we make sure the depth is more is the LCA we return that node by increasing the depth 
        """
        def dfs(node):
            if not node:
                return None,0 #height 0 for null node
            
            left_node,left_height = dfs(node.left)
            right_node,right_height = dfs(node.right)
            #case 1 : if both depths/heights are eq
            if left_height == right_height:
                return node,left_height + 1 #you can return either depths/height as the are eq
            #case2 : if at cur level left node depth is greater that means lca lies in leftnode
            elif left_height > right_height:
                return left_node,left_height + 1
            #case3 : if at cur level right node depth is greater that means lca lies in rightnode
            else:
                return right_node,right_height + 1
        node,depth = dfs(root)
        return node
            

        