# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        plan is to check height of left node and right node and check if the diff is more than 1 if yes return False
        """
        def dfs(node):
            if not node: return 0 

            #Lets traverse as deep left as possible 
            left = dfs(node.left)
            #at the end leaf node left = 0 so the below will be skipped and only excuted when the tree became unbalanced 
            if left == -1 : return -1
            right = dfs(node.right)
            #similar if right becomes unabalence then -1 will be passed to futur functions 
            if right == -1: return -1
# this approch is tricky but doable undertsand by drawing a tree if once the -1 is triggered it will automatically pass it to the top node 
            if abs(left - right) > 1 : return -1 

        #     return 1+max(left,right)
        # return dfs(root) != -1 

        def dfs2(node):
            #watch need code version this is more intuitive and easy to undertsnad 
            if not node: return [True,0]

            left = dfs2(node.left)
            right = dfs2(node.right)
            balanced = (left[0] and right[0]    
                                and abs(left[1]-right[1]) <=1)
            return [balanced, 1+max(left[1],right[1])]
        return dfs2(root)[0]



        