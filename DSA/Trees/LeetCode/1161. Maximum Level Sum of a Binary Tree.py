# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        The key idea here is 
        - level order traversal and we will do cur level sum
        - we will have max_val and max_level var set
        case1: if cur_level_sum becomes greater than max_val we directly update the max_level (straigth forward case)
        case2: if cur_level_sum becomes eq to the max_val we have currently (not greater) then we dont update the max_level as we need the smallest level, so the prev level will be the smallest and remains.
        The edge case is : we should also take care of case where there is no node
        """
        def bfs(node):
            q = deque([node])
            #global var only update if cond trigrred
            max_sum = float("-inf") #lowest possible val
            max_level = 0 #intially set to 0 val< since root level is 1
            level = 0 #started with 0
            while q:
                #cur level 
                level += 1
                size = len(q)
                cur_sum = 0
                for _ in range(size):
                    node = q.popleft()
                    cur_sum += node.val 
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                #once processed the cur_level
                #check maxsum cond
                if cur_sum > max_sum: #if and only if greater then only update, so we can parelly conincedncly get rid of the eq case too 
                    max_sum = cur_sum 
                    max_level = level 
            return max_level
        return bfs(root)
