# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            """
            The key idea is 
            - divide the big from into small problem 
            - move to the bottom most sub tree 
            - swap the nodes ie node.right,node.left = node.left,node.right
            - and continue doing this till the root
            so the idea is clear
            - lets do post order traversal 
            - move to the bottom most left sub tree 
            - swap the nodes (trees are mutable in python)
            - once swapped we can return that node if there is some operation left but in this sum we can just leave it as is.
            """
            #base case 
            if not node: return 

            #move to the leaft node 
            dfs(node.left)
            dfs(node.right)
            #process the node
            node.left,node.right = node.right,node.left
            # return node 

        dfs(root)
        return root


            
        