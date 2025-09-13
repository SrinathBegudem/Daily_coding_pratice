# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res1= []
        res2 = []


        #--------recur_sol----------
        def recur_sol(node):
            """
            L->R->ri
            """
            if node is None: return 

            recur_sol(node.left)
            res1.append(node.val)
            recur_sol(node.right)
        # recur_sol(root)
        # return res1

        #------------iter sol----------
        def iter_sol(node):
            """
            The intution here is pretty clear we are just trying to mimic recursion by creating stack by over self so what happen in recursion we move as left as possible and then print it and back track exactly now also we move as left as possible store in stack and then pop from stack and print it and then move right. is it not wonderful??
            """
            res = []
            stack = []
            cur = node
            while cur or stack:
                #move as deep as possible left and then pop from stack and print and then mmove right once and move as left as possible same as recursion 
                while cur:
                    # move as left as possible once hit left bottom then come out and print the node and move right once and then again contineue to move as depp left as possible.
                    stack.append(cur)
                    cur = cur.left
                
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            return res
        return iter_sol(root)
                




        