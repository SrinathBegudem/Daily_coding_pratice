# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def iter(node,res):
            """
            Key idea
            - we use stack to mimic recursion in iter sol 
            - concept remains same 
            - process the node first 
            - then check if node.right exisits if yes, process it first because we pop from the end so left should be added at the end 
            - then check if node.left exisits if yes. add it to the stack
            """
            #base
            if not node:
                return
            stack = [node] # adding the root node
            while stack:
                # process the node
                node = stack.pop()
                res.append(node.val)
                # check if the right node exsits 
                if node.right: stack.append(node.right)
                # check left node exsists
                if node.left: stack.append(node.left)
        res = []
        iter(root,res)
        return res

        def recur(node,res):
            """
            Root -> left -> right
            """
            if not node: return 

            #process the node first 
            res.append(node.val)
            #move left
            recur(node.left,res)
            #move right
            recur(node.right,res)
        res = []
        recur(root,res)
        return res
        