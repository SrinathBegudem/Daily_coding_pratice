# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        This sum is similar to pathsum 
        The key idea is 
        - we add the curSum bfr checking whether its leaf or not and returning 
        and at the end we call both nodes reecursively 
        """

#code without self.res var
        def dfs(node, curSum):
            #base case : this will onlu excute if the root is None, if confusing you can place this outside the dfs too something if not root:return0
            if not node:
                return 0
            curSum = curSum*10 + node.val
            # all other cases the return statement will be here 
            if not node.left and not node.right:
                return curSum
            # curSum = curSum*10 + node.val
            return dfs(node.left,curSum) + dfs(node.right,curSum)
        return dfs(root,0)



# with self.res var 
        self.res = 0
        def dfs(node, curSum):
            #base case : this will onlu excute if the root is None, if confusing you can place this outside the dfs too something if not root:return0
            if not node:
                return 0
            curSum = curSum*10 + node.val
            # all other cases the return statement will be here 
            if not node.left and not node.right:
                self.res += curSum
                print(self.res)
                return 
            # curSum = curSum*10 + node.val
            dfs(node.left,curSum)
            dfs(node.right,curSum)
        dfs(root,0)
        return self.res

        # self.res = 0
        # path = []
        # def dfs(node,path):
        #     # if not node:
        #     #     self.res += int("".join(path))
        #     #     return
        #     if not node.left and not node.right:
        #         print(path)
        #         path.append(str(node.val))
        #         self.res += int("".join(path))
        #         return
        #     path.append(str(node.val))
        #     dfs(node.left,path)
        #     path.pop()
        #     dfs(node.right,path)
        #     path.pop()
        # dfs(root,path)
        # return self.res


        