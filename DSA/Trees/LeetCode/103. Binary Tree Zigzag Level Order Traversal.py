# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is optimal code there are other ways too sovle the qeustion with dfs and appendleft adn all stuff you can see aftr wards.
        # time = o(n) space = 0(n)
        # there is one more approch normal -> remove from front and add the elements in the end and when reverse order -> remove from back and add elements in front.
        if not root:
            return []
        def reverse(arr):
            left = 0
            right = len(arr) - 1
            while left < right:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
                right -= 1
            return arr
        res = []
        q = deque([root])
        flag = False
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag:
                res.append(reverse(level))
                flag = False
            else:
                res.append(level)
                flag = True
        return res



        