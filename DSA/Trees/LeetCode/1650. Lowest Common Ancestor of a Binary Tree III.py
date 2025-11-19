"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        this sum is exactly equal to linked list intersection lc 160
        https://www.youtube.com/watch?v=iaOceNnKIQQ
        if you turn tree over 90 degrees this becomes ditoo linked list sum instead of next pointer we use parent pointer
        refer my own linked list guthub code for detail explantion
        """
        a,b = p, q
        while a!=b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a #or b


        #optimal time but not optimal space

        # seen = set()
        # def dfs(node):
        #     if not node: return
        #     if node in seen:
        #         return node
        #     seen.add(node)
        #     return dfs(node.parent)
        # dfs(p)
        # lca = dfs(q)
        # return lca










        # # seen = set()
        # # seen_val = set()
        # # def dfs(node):
        # #     if not node:
        # #         return 
        # #     seen.add(node)
        # #     seen_val.add(node.val)
        # #     dfs(node.parent)
        
        # # def lca(node):
        # #     if node in seen:
        # #         return node
        #     return lca(node.parent)
        # dfs(p)
        # # print(seen_val)
        # return lca(q)