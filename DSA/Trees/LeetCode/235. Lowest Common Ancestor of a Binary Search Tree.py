# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #optimal iterative solution TIME = o(h) and space = o(1)

        def iter_sol(node):
            while node:
                if p.val < node.val and q.val < node.val:
                    node = node.left
                elif p.val > node.val and q.val > node.val:
                    node = node.right
                else:
                    return node
        return iter_sol(root)






        # below is the recursive sol which takes up stack space for recursion calls time = space = o(h)
        
        def dfs(node):
            #base case 1: if not node return 
            if not node: return None #or node
            #if p or q found 
            if p == node or q == node:
                return node
            
            #move left and right based on bst property

            #case 1: if both are less than root val, move left(both val lie in left subtree)
            if p.val < node.val and q.val < node.val:
                left = dfs(node.left)
                return left
                #or simply do  return dfs(node.left)
            #case 2: if both are greater than root val , move right(both val lie in right subtree)
            elif p.val > node.val and q.val > node.val:
                right = dfs(node.right)
                return right
                #simialr do dfs(node.right)
             #case 3: if both val lie in diff subtrees return the cur node 
            else:
                return node

        return dfs(root)



        