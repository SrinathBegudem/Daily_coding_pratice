# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return

        # def dfs(t1,t2):
        #     if not t1 and not t2: return 

        #     dfs(t1.left,t2.right)
        #     dfs(t1.right,t2.left)
        #     t1.left, t2.right = t2.right, t1.left
        #     t1.right, t2.left = t2.left, t1.right
        #     return 
        
        # dfs(root,root)
        # return root
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            node.left,node.right = node.right,node.left
            return node
        return dfs(root)


# # pass ,next     ,waiting      ,return 

# (2,7)  (1,9)     (3,6)              
# (1,9)   (n,n)    (n,n)  -------- 
# n,n---------------------------
# n,n --------------------------
# 3,6