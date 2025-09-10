# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Intuition : we see that something is happening in level so definetly we should use level order traversal but with slight modification. my intial idea that we want everything from right side view and in level order traversal the last element we push in the deque is the right most element be it the true right of the tree or left_right of the tree ( when true right have no nodes).
        """
        return self.rightSideViewDFS(root)

    #-------------bfs----------------------------
    def first_try(self,root):
        if not root:
            return []
        # i am just doing classical level order trasversal using deque 
        res = []
        q = deque([root])
        while q:
            # append the right most element in the queue which it the element in -1 index
            res.append(q[-1].val) # instead of this follow the below this is crct nothin wrng but more cleaner approch is below.
            #now let me append the next level 
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return res
    
    def optimal_code(self,root):
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                rightmost = node.val # so right most is update until we reach the last ele in q which is the right most
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(rightmost)
        return res
    
    #------------------dfs-------------
    def rightSideViewDFS(self,root):
        """
        Intuition: the idea here is to use right to reach the rightmost first also update the depth 
        so when the first time you reach the depth your at the right most as we recur from right node first
        """
        if not root: return []
        res = []

        def dfs(node,depth):
            if not node: return 

            #append the right most val to the res once we reached the depth 
            if depth == len(res):
                res.append(node.val)
            
            #move right first so we cal the depth the first time we reach right and append it to res and when we reahc the same depth with left we dont really append it. and the idea is that the second them that is when we reach the depth with left we have one element more in the list that is added at the deppest of right so same depth on left will not be added.
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        dfs(root,0)
        return res
        






        