# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def iter(node,res):
            """
            Its evident that we use stack for iter sol as recursion can be mimiked with stack data structure.
            THe key idea is 
            - we traverse as left as possible 
            - then process the node 
            - move right 
            - and continue.
            """
            stack = []
            cur = node # this variable is use to traverse as left as posiible
            while cur or stack:
                # move/ traverse as left as possible 
                while cur:
                    stack.append(cur)
                    cur = cur.left

                # when the above loop breaks we are at one node pass left most leaf node
                # process that node
                cur = stack.pop() # this will pop left most leaf first 
                res.append(cur.val)
                cur = cur.right # add the right node and continue 
            return res 
        res = []
        iter(root,res)
        return res


        
        def recur(node,res):
            """
            Left -> Root -> right
            """
            if not node: return 
            #go as left as possible 
            recur(node.left,res)
            #append the root 
            res.append(node.val)
            #then traverse the right node
            recur(node.right,res)
        res = []
        recur(root,res)
        return res

 