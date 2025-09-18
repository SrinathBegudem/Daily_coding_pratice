# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # lets have a instance var so we can move around it inside and outside function 
        self.max_dia = 0
        #if you dont want to do instance var declare max_dia and put nonlocal max_dia inside the dfs function so it doesnt throw error. 
        #concept understand the scope of var
        """
        If you have immutable type and then create the var in parent function(diameterofBinaryTree) and then without passing it into function, if you try to use it in nested function (child function in this ex dfs) then it will throw you local var not declared error. its because when you use immutable types it always create a new var but when your doing the mutable types like list this out throw you an error. so for this problem we do self.var (for mutable) so it can be used across function which has self as parameter and if you dont want to use self hen you can declare nonlocal inside dfs 
        """

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            dia = left + right
            self.max_dia = max(self.max_dia,dia)
            return 1 + max(left,right)
        dfs(root)
        return self.max_dia

            