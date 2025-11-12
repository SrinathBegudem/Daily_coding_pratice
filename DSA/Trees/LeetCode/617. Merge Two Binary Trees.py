# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1,node2):
            """
            Firstly i tired creating a new tree and unable to create it 
            - so i started to modify the exisiting tree and it worked and its most optimal
            - so remeber whenever they ask to merge tree , replacing nodes or any tree would do the thing and its easy
            - but we can also create a new tree for btter conceptutal understading the code is below 
            """
            # if no node 1 and node 2 return none node
            if not node1 and not node2:
                return None
            # if any of the node is none return the other node so the below strucute and subtree also comes with it (this is the most imp edge case)
            if not node1 and node2:
                return node2
            if node1 and not node2:
                return node1
            
            #update the val of node1 tree
            node1.val = node1.val + node2.val
            #recurse to left and right node
            node1.left = dfs(node1.left,node2.left)
            node1.right = dfs(node1.right,node2.right)
            return node1
        # return dfs(root1,root2)

        def dfs_new_tree(t1,t2):
            if not t1 and not t2:
                return None
            # choose value from whichever exists
            val = (t1.val if t1 else 0) + (t2.val if t2 else 0)
            root = TreeNode(val)
            # thise if else condition is very imp for new tree creating and edge case handling, if you wonder why try uncommenting below faield code and see
            root.left = dfs_new_tree(t1.left if t1 else None,t2.left if t2 else None)
            root.right = dfs_new_tree(t1.right if t1 else None,t2.right if t2 else None)
            return root
        
        return dfs_new_tree(root1,root2)





        # failed code when i tried to create a new tree
            # if not node1 and node2:
            #     return node2.val
            # if node1 and not node2:
            #     return node1.val
            # if node1 and node2:
            #     return TreeNode(node1.val+node2.val)
        #     if not node1 and node2:
        #         node = TreeNode(node2.val)
        #         # return node
        #     elif node1 and not node2:
        #         node = TreeNode(node1.val)
        #         # return node
        #     else:
        #         node = TreeNode(node1.val + node2.val)
        #     node.left = dfs(node1.left,node2.left)
        #     node.right = dfs(node1.right,node2.right)
        #     return node
        # return dfs(root1,root2)
        