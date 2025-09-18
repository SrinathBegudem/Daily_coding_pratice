# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            """
            ALways remeber for this problem we need to check if left exisit if yes then we need to do the pointer manuplication and if not right we can skip because we are cared to have all the pointer to be faltten(attached to right and point the left pointer to null). and also have parent node and child nodes(tails) during manuplication, so first attach the leftTail.right(node.left child node) to the node.right so what we did is detach the right node and attached it after node.left right node and then detahc the node.left and attach it to node.right and then point node.left to null.
            """
            if not node: return None

            leftTail = dfs(node.left)
            rightTail = dfs(node.right)
            if node.left:#or leftTail
                leftTail.right = node.right #either its a val or null diesnt matter attach the left next to the right node
                node.right = node.left
                node.left = None
            
            last = rightTail or leftTail or node
            return last
        # dfs(root)

        self.prev = None
        def dfs2_recur(node):
            """
            This recursion solution is not very intutive but draw the diagram you will undertsand how the prev pointer(head of faltten linked list) is attached to the node which is fallten to its right
            remeber the left should alwys be null so we need to attach to the node.right which is empty  
            """
            if not node: return None

            dfs2_recur(node.right)
            dfs2_recur(node.left)
            node.right = self.prev
            node.left = None
        #     self.prev = node
        # dfs2_recur(root)

        def dfs_iter(node):
            if not node: return None
            stack = [root]
            prev=None
            while stack:
                node = stack.pop()
                if prev:
                    prev.left = None
                    prev.right = node
                prev = node
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
        dfs_iter(root)


        