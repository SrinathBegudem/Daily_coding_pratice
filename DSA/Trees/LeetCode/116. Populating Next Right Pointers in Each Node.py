"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque 
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Try to solve follow up question of how do we solve in constant space with queue ??? linked list concept solve next time 
        """
        return self.basic_simplified_sol(root) # time = o(n)=space 


    def basic_sol(self,root):
        if not root:
            return None
        q = deque([root])
        while q:
            level = deque()
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for _ in range(len(level)):
                n = level.popleft()
                if level:
                    n.next = level[0]
                else:
                    n.next = None
        return root
    
    def basic_simplified_sol(self,root):
        # the intiution is the node.next are already pointer to null
        if not root:
            return None 
        q = deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node 
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            # last node in level naturally has next = None
        return root
            





        