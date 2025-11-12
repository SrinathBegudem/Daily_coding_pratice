# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        I would say the bfs solution would be more easy to code for this question
        - i think we need to have a helper funciton when the root of tree is equal to the subroot, then we check for sametree
        - so bfs or dfs the idea remains same , just know the tiny optimisation for not searchign whole tree once the subtree is found
        """
        # base case if not root and sub
        if not root and not subRoot:
            return True

        def is_same_dfs(node1,node2):
            # base cases 
            if not node1 and not node2:
                return True
            if not node1 or not node2: 
                return False
            if node1.val != node2.val:
                return False
            return is_same_dfs(node1.left,node2.left) and is_same_dfs(node1.right,node2.right)
        
        # the dfs solution is bit tricky we traverse the tree until the node.val == subnode.val condition triggers once it triggers we check and early return and the key points are if we move to the leaf nodes and None node we need to return False not true if we return true we are using or statement, this will early cut if we return true so thats why we return false, and the or statment is used so if we find early subroot we root and wont traverse whole tree
        def dfs(node,subnode):
            #base cases 
            if not node: # important return False not true because of the or statement 
                return False
            if node.val == subnode.val and is_same_dfs(node,subnode): # vall the same tree function if and only if vals match
                return True
            return dfs(node.left,subnode) or dfs(node.right,subnode) # return early when one of the left or right subtree met the condition 
        return dfs(root,subRoot)
            

        # the bfs approch is very straight forward , we will have a helper funciton and a checker if it turns true we early return else we traverse whole tree
        def is_same_bfs(node1,node2):
            q = deque([(node1,node2)])
            while q:
                n1,n2 = q.popleft()
                if not n1 and not n2:
                    continue
                if not n1 or not n2:
                    return False
                if n1.val != n2.val:
                    return False
                q.append((n1.left,n2.left))
                q.append((n1.right,n2.right))
            return True
        

        def bfs():
            q = deque([(root)])
            check = False
            while q:
                node = q.pop()
                if node.val == subRoot.val:
                    check = is_same(node,subRoot)
                if check:
                    return check
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            return check
        return bfs()

        






#---------------previous try sol--------------------------------
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.flag = False
        def sameTree(t1,t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            return (t1.val == t2.val) and sameTree(t1.left,t2.left) and sameTree(t1.right,t2.right)

        def dfs(node,subnode):
            if not node: return 
            if node.val == subnode.val and sameTree(node,subnode):
                self.flag = True
                # return
            dfs(node.left,subnode)
            dfs(node.right,subnode)
        dfs(root,subRoot)
        # return self.flag





        # with out flag
        # this is more optimal because this wont traverse. the entire tree and return when the first truth value in or met, if sameTree is true then it wont exceute the left or right sub node return true to prev function cal and more optimal version is dfs3 here we call sameTree for everynode to avoid it we got dfs3 
        def dfs2(node):
            if not node: return False # dont return true bcz of or statement if you return true no matter what the code alwasy return true bcz every tree eventually reachs to its leaf and returns true soo this condition should be flase and if same tree is false then the funtion checks for next true in or so if this are put as false then we wil lget the expected results 

            return sameTree(node,subRoot) or dfs2(node.left) or dfs2(node.right)
        # return dfs2(root)
        
        # most optimal 
        def dfs3(node):
            if not node: return False

            if node.val == subRoot.val and sameTree(node,subRoot):
                return True

            return dfs3(node.left) or dfs3(node.right)
        return dfs3(root)

