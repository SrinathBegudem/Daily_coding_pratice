# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def bfs(p,q):

            q = deque([(p,q)])
            while q:
                n1,n2 = q.popleft()
                if not n1 and not n2:
                    continue
                if not n1 or not n2:
                    return False
                if n1.val != n2.val:
                    return False
                q.append((n1.left,n2.left)) #key point is to append with the null nodes so we can verify the structure 
                q.append((n1.right,n2.right)) #same goes to this right subtree too, we want to check both val and structure
            return True
        bfs(p,q)



        
        def dfs(node1, node2):
            """
            The key idea here is to do pre order traversal where i comapred the node first and then and only then if they are equal i recurse 
            - This approch will helps us to short circuit the recursion calls once the node is diff making it efficent without check the whole tree

            """
            # Both are None → same
            if not node1 and not node2:
                return True
            # One is None, the other not → different
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return dfs(node1.left,node2.left) and dfs(node1.right,node2.right)
        return dfs(p,q)

