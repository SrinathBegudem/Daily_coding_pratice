# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.flag = False
        def sameTree(t1,t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            return (t1.val == t2.val) and sameTree(t1.left,t2.left) and sameTree(t1.right,t2.right)

        def dfs(node,subnode):
            if not node: return 
            if node.val == subnode.val and sameTree(node,subnode):
                self.flag = True
                # return
            dfs(node.left,subnode)
            dfs(node.right,subnode)
        dfs(root,subRoot)
        # return self.flag





        # with out flag
        # this is more optimal because this wont traverse. the entire tree and return when the first truth value in or met, if sameTree is true then it wont exceute the left or right sub node return true to prev function cal and more optimal version is dfs3 here we call sameTree for everynode to avoid it we got dfs3 
        def dfs2(node):
            if not node: return False # dont return true bcz of or statement if you return true no matter what the code alwasy return true bcz every tree eventually reachs to its leaf and returns true soo this condition should be flase and if same tree is false then the funtion checks for next true in or so if this are put as false then we wil lget the expected results 

            return sameTree(node,subRoot) or dfs2(node.left) or dfs2(node.right)
        # return dfs2(root)
        
        # most optimal 
        def dfs3(node):
            if not node: return False

            if node.val == subRoot.val and sameTree(node,subRoot):
                return True

            return dfs3(node.left) or dfs3(node.right)
        return dfs3(root)

