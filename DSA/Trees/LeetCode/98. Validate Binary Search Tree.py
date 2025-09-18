# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        if you do immediate comparision if left.val < node.val and then right val > node.val then your in the pitfall they created there is a reason why this is a medium problem. so undertsand what is binary search tree if root val is 5 then left side val sub tree are no matter what are less than the 5 and right side is more than 5 
if you have somewhere deep down left val greater than 5 and it is right side of that particular node it is not a bst.
        """
        def valid(node,left,right):
            #we use boundaries 
            if not node: return True

            if not (left < node.val< right):
                return False
            #left will be constant which is -infinyt for node.left but right will be the value of cur node so that the next node val is striclty less than the parent node val 
            #right will be constant in second recursion call which is +infinity but the left val will be the cur node.val so that the next node val will be definately greater than that.so we maintian the condition 
            return valid(node.left,left,node.val) and valid(node.right,node.val,right)
        return valid(root,float('-inf'),float('inf'))
