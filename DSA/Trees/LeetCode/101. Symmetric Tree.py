# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition is same as same tree lc 100 question a slight modification instead if left lef twe do left right and here they gave us one tree but we gonna pass them twice 
        """
    #-----------------dfs---------------------
        def dfs(t1,t2):
            #lets pass the same root as tree1 and tree2 or else you can skip the root and pass the children directly 
            #edge case1 : if both are None then return True
            if not t1 and not t2: return True
            #edgecase2 : if one of the sub tree is absent then we return False
            if not t1 or not t2: return False

            #core logic 
            #t1.left should be equal to t2.right and vice versa and there vals should be equal
            return (t1.val == t2.val) and dfs(t1.left,t2.right) and dfs(t1.right,t2.left)
        #pass root left and right children
        # return dfs(root.left,root.right)

    #------------------bfs--------------------
        def bfs(t1,t2):
            q = deque([(t1,t2)])
            while q:
                n1,n2=q.popleft()
                #case1: there is a chance of getting both None at leaf nodes so in that case we just continue because in lvl order we append from left to right if we return the first instance where we get both none then we might miss out the other nodes check for ex in ex1 if we retrun at 3 then we might miss checking 4 ( early return == bug)
                if not n1 and not n2:
                    continue
                #case2: one of the node is missing then we are sure that it is not symmentric so we can early return 
                if not n1 or not n2 :
                    return False
                
                #core logic
                if n1.val != n2.val:
                    return False
                q.append((n1.left,n2.right))
                q.append((n1.right,n2.left))
            
            # if everything is passed and while loop is exhausted then return True
            return True
        return bfs(root,root) #or u can pass (root.left,root.right) 


        
        
        