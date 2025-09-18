# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        The intuition here is very simple first just order the p and q into vars that makes things eaisy we can have 2 var and then have the var in ascending order and then we see if the biggest num is less that the root if yes it is sure that from bst property both the p and q are in the left side of the node similar if the smallest val is greater than node val then it is on the right side of the node and if both fails they are either side of the node so return the node simlple.
        """
        a = p.val
        b = q.val
        if a > b : 
            a,b = b,a # so no matter what a will be smallest and b will be the larger one 

        # check if the biggest val is less than the root.val is yes then both values lie in the left side of the root
        if b < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        #check if the smallest val is greater than the root.val is yes both lie to the right 
        if a > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        # for the smal node being one descendent and if either node be one either sides of the root then return the node this works for both coniditons and also will be the lowest common ancestor
        return root
    