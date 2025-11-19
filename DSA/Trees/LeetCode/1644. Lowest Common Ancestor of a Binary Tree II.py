# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        The Key diff for lca(236) and lca 2(1644) is that 
        lca 1 :
        - the check condition comes before exploring children 
        - as it is gaurenteed that both p and q exists we return once p or q is found this is premature return 
        - and this works for only lca 1
        lca 2:
        - here your not gauntreed to have p and q 
        - so you should check all nodes before returning 
        - so check should come after the recurse ( visitng both children)
        - this gauntree to visit all the nodes in the tree and checking if node exists 
        """
        self.p_found = False
        self.q_found = False
        def dfs(node):
            if not node: return None

            left = dfs(node.left)
            right = dfs(node.right)
            if node == p:
                self.p_found = True
                return node
            if node == q:
                self.q_found = True
                return node
            
            if left and right: 
                return node
            
            return left if left else right
        lca = dfs(root)
        return lca if self.p_found and self.q_found else None







        # # two pass sol non optimal lets do it in single pass 
        # self.p_found = False
        # self.q_found = False
        # def is_exist(node,p,q):
        #     if not node: return 
        #     if p == node: self.p_found = True
        #     if q == node: self.q_found = True
        #     is_exist(node.left,p,q)
        #     is_exist(node.right,p,q)
        #     return self.p_found and self.q_found
        
        # def dfs(node):
        #     if not node: return node #/None

        #     if p == node or q == node:
        #         return node
            
        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     if left and right: 
        #         return node
            
        #     return left if left else right 

        # return dfs(root) if is_exist(root,p,q) else None

