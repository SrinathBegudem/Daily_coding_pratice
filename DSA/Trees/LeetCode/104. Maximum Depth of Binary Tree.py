# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Key point:
        - in trees and in leetcode both height of the tree and depth of the tree are same code
        - the only diff is that depth is cal from the root node
        - height is cal from the leaf node 
        - ex depth of root is 0 and height of root is 3 
        - and depth of leaf is 3 and height of lead is 0 
        - apart from that the code remains same.
        are they asking heigh??
        yep they are asking hieght of a BT, so simple traverse to left depth and then right and for that particular node update the max of left and right and back track
        """
        def dfs(node):
            if not node: return 0 
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left,right)
        return dfs(root)
        