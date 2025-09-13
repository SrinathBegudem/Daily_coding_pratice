# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res1= []
        res2= []
        
        #------------------recursion(DFS)-------------------
        def recur_sol(node):
            """
            Intuition is we need to R->l->r (pre means root comes first), so simply append to the res at the beggining of recursion call thats it and traverse to the depths of left
            """
            #base condition:
            if not node: #or to be more explicit we can also keep if node is None:
                return #just return
            
            #-----core logic---------
            #add res first(pre)
            res1.append(node.val)
            #make recursion calls 
            #left first 
            recur_sol(node.left)
            #right next
            recur_sol(node.right)
        # recur_sol(root)
        # return res1

        def iter_sol(node):
            """
            Intution here is to use stack and build the tree and parelle we  append our res as we traverse 
            """
            stack = [node]
            while stack:
                #pop the node and append it to res 
                node = stack.pop()
                #base case:
                if node is None:
                    continue # we want to continue here not return if we return we do early exit
                res2.append(node.val)
                # push righ and then left so when you pop we get left first as it is expected to be before 
                if node.right: stack.append(node.right)
                if node.left : stack.append(node.left)
        iter_sol(root)
        return res2


        