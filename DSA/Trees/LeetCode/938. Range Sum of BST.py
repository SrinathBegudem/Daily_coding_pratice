# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # def dfs(node,curSum,target):
        #     if not node: return 
        #     if node.val == target:
        #         return curSum + node.val
        #     elif target < node.val:
        #         if low<=node.val<=high:
        #             curSum += node.val
        #         return dfs(node.left,curSum,target)
        #     else:
        #         if low<=node.val<=high:
        #             curSum += node.val
        #         return dfs(node.right,curSum,target)
        # print(dfs(root,0,low),dfs(root,0,high))
        # return dfs(root,0,low) + dfs(root,0,high) - root.val


        def dfs_optimal(node):
            """
            In this we will go depper only in the explored and valid path cuttign down the subtree trees where the range is out of bound. this is optimal because we are now only exploring the path in given range and possible sol in that range but not going to each and every path
            """
            if not node: return 0
            # if the val is less than lower limit skip the whole left tree, we not gonna find anything there 
            if node.val < low:
                return dfs_optimal(node.right)
            # if the val is greater than upper limit skip the right tree
            if node.val > high:
                return dfs_optimal(node.left)
            # if both the above conditions failed that means we are in the range 
            return node.val + dfs_optimal(node.left) + dfs_optimal(node.right)
        return dfs_optimal(root)
        self.res = 0
        def dfs(node):
            """
            In this we will go to each and every path and we dont reallu use the property of binary search tree to optimsed, this code work even when given a randomised tree
            """
            if not node: return 

            if low <= node.val <= high:
                self.res += node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res

            
            
        