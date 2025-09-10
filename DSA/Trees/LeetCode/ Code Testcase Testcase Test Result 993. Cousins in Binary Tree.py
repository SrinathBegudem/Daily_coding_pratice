#must do question covers both sibiling and cousin of a binary tree concept.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        intuition is depth = level i will keep a set called level and see if the both elemts are in same level but for diff parent we should probably carry the parents too 

        very important take care of unquie val statement.
        """

        return self.isCousins_dfs(root,x,y)
    
    #-------------------bfs--------
    def bfs(self,root,x,y):
        if not root: return False
         
        q = deque([(root,None)])
        while q:
            x_parent = y_parent = None
            for _ in range(len(q)):
                node,parent = q.popleft()
                if node.val == x: 
                    x_parent = parent
                if node.val == y:
                    y_parent = parent
                
                if node.left: q.append((node.left,node))
                if node.right: q.append((node.right,node))
            

            # CASE1: if you found out both x and  and check if they are cusns or sibiling 
            if x_parent and y_parent:
                return x_parent != y_parent #condition for cusns and for sibiling they would be equal

            #case2: if you found out x and not y or y and not x then return false because they are at diff depths. see how they are given a hint in the question saying that all nodes contains unquie values that means once we found out either of them in certain level there is gaurentee that there wont be in another level  
            if (x_parent and not y_parent) or (y_parent and not x_parent):
                return False
            
        return False

    #--------------------------dfs-------------------
    def isCousins_dfs(self,root,x,y):
        info = {} # this stores {node.val:(depth,parent)} 

        def dfs(node,parent,depth):
            if not node:
                return
            # if node.val == x or node.val == y:
            #     info[node.val] = (depth,parent)
            # the above can be written for edge cases 
            if node.val in (x,y):
                info[node.val] = (depth, parent.val if parent else None) # we can take val bcz all nodes are unquie
            #early return if both x and y are found 
            if x in info and y in info:
                return
            dfs(node.left,node,depth+1)
            dfs(node.right,node,depth+1)
        dfs(root,None,0)

        depth_x,parent_x = info[x]
        depth_y,parent_y = info[y]
        return depth_x == depth_y and parent_x != parent_y





            



        