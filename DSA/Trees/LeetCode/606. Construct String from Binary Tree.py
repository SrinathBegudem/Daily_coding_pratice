# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ""

        res = []

        def dfs(node):
            if not node:
                return
            # pre order we process the node 1 
            res.append(str(node.val))
            # only case one or case 2 only one statement excetues
            #case1: if left node exists
            if node.left:
                # add the open par 
                res.append("(")
                #recurse
                dfs(node.left)
                # close 
                res.append(")")
            #case2: if not left node and only right node
            elif node.right:
                res.append("()")
            
            # no matter the above 2 this statement will again be checked
            #case3 : node.right only include if exists 
            if node.right:
                # add the open para
                res.append("(")
                #recurse
                dfs(node.right)
                # close para
                res.append(")")
        dfs(root)
        return "".join(res)

# neet code version simple but need to take care of edge cases 
        def dfs(node):
            if not node: return 

            #add the open para 
            res.append("(")
            #process the node 
            res.append(str(node.val))
            # check the condition 
            if not node.left and node.right:
                res.append("()")
            #recurse
            dfs(node.left)
            dfs(node.right)
            #add closing bracket 
            res.append(")")
        dfs(root)
        # as we added the start and end para remove it 
        return "".join(res)[1:-1]
                

        