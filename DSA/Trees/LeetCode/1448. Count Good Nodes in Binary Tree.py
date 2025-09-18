# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:


#------------my own try-----------------------
        self.count = 1
        def dfs(node,m=root.val):
            if not node: return
            if node.val >= m:
                m = node.val
                self.count += 1
            dfs(node.left,m)
            dfs(node.right,m)
        # dfs(root.left)
        # dfs(root.right)
        # return self.count
#---------------chatgpt way of solving-----------
        def dfs2(node,path_max):
            if not node : return 0
            good_node = 1 if node.val >= path_max else 0
            new_max = node.val if node.val > path_max else path_max
            return good_node + dfs2(node.left,new_max) + dfs2(node.right,new_max)
        
        # return dfs2(root,float('-inf'))

        def iter_sol(node):
            if not node: return 0
            cnt =0
            path_max = float('-inf')

            stack = [(node,node.val)]
            while stack:
                cur_node,path_max = stack.pop()
                if cur_node.val >= path_max:
                    cnt +=1
                new_max = cur_node.val if cur_node.val > path_max else path_max
                if cur_node.left: stack.append((cur_node.left,new_max))
                if cur_node.right: stack.append((cur_node.right,new_max))
            return cnt
        return iter_sol(root)
                
                


            





        