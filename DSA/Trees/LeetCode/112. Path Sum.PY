# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curSum):
            if not node:
                return False #base case  ( and we are gonna use or statement so using true will early stop it bymistakely)
            
            #add node val to curSum
            curSum += node.val
            #check if we are at left node, if we are then check if cur_sum ==targetsum
            if not node.left and not node.right:
                return curSum == targetSum
            
            # recurse left or right
            return dfs(node.left,curSum) or dfs(node.right,curSum) # if any where it return true it will early stop and return true
        return dfs(root,0)






        # i came up with the backtracking solution all by myself, thats an achievement but thats not optimal we are overkilling and make the time complexity worst, when we can do better
        # self.flag = False
        # path = []
        # if not root:return self.flag
        # def is_leaf(node):
        #     if not node.left and not node.right:
        #         return True
        #     return False

        # def backtrack(node):
        #     print(path)
        #     if not node:
        #         return        
        #     # if self.flag: return self.flag
            
            
        #     path.append(node.val)
        #     backtrack(node.left)
        #     # stack.pop()
        #     backtrack(node.right)
        #     if is_leaf(node) and sum(path) == targetSum:
        #         self.flag = True
        #     path.pop()
        # backtrack(root)
        # return self.flag

        