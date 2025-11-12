# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        # lets have a instance var so we can move around it inside and outside function 
        self.max = 0
        #if you dont want to do instance var declare max_dia and put nonlocal max_dia inside the dfs function so it doesnt throw error. 
        #concept understand the scope of var
        """
        If you have immutable type and then create the var in parent function(diameterofBinaryTree) and then without passing it into function, if you try to use it in nested function (child function in this ex dfs) then it will throw you local var not declared error. its because when you use immutable types it always create a new var but when your doing the mutable types like list this out throw you an error. so for this problem we do self.var (for immutable) so it can be used across function which has self as parameter and if you dont want to use self hen you can declare nonlocal inside dfs 
        """
        def dfs2(node):
            if not node: return 0

            left = dfs2(node.left)
            right = dfs2(node.right)
            #upate global dia (this makes things easier)
            cur_dia = left+right
            self.max = max(self.max,cur_dia)
            #return the height
            return 1 + max(left,right)
        dfs2(root)
        return self.max




        # solution without using global self.max (non local) var pure recursion but confusing
        def dfs(node):
            """
            In this approch i used a approch where i propogate the max val to the prev function
            - return both height and max
            """
            #if no node max_dia = 0 and height = 0
            if not node: return (0,0)
            # recursvly traverse to the lef most node and start building max_dia
            left,l_max_dia = dfs(node.left)
            #simialrly to right 
            right,r_max_dia = dfs(node.right)
            # so at the cur node we cal the sum of both right and left subtrees for dia of that node
            # use hieght of left sub tree and right sub tree to cal dia but pass one max of left and right to prev function
            cur_max = left + right 
            # update the max based one every node dia (its not gauntree that root node has max dia)
            max_dia = max(cur_max,l_max_dia,r_max_dia)
            # whiling return i wont return cur_dia i return the max of left or right bcz that is what only matters to dia of the above node in simple terms i return hieght up until that node
            return (1 + max(left,right),max_dia)
        return dfs(root)[1]



        