# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:


        #chatgpt code 
        if not root: return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
        return root





# -------my code ----------
        def dfs(node):
            if node is None: return 


            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return 
                return dfs(node.left)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return 
                return dfs(node.right)
        # dfs(root)
        # return root if root else TreeNode(val)

        