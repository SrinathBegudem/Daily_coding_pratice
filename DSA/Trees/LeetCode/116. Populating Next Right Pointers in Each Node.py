#new attempt
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
        I think this sum can be solved by bfs level order traversal and level by level version not just normal bfs 
        """
        def bfs():
            """
            The below is standard bfs without acutally pushing list of levels whic his unnecesary and prev pointer 
            """
            if not root:
                return None
            q = deque([root])
            while q:
                level_size = len(q)
                prev = None
                for _ in range(level_size):
                    node = q.popleft()
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    if prev:
                        prev.next = node
                    prev = node
                # last node in level
                # prev.next = None # this is not required as the next is intialized as None anyways
            return root
        return bfs()
        def bfs_complicated():
            """
            I solved this question on my own but it is very complicated to udnerstand i pushed level by level list and tried index and using i + 1 concpet, it worked and passed but one bug that i fixed is i appended levels without checkign that gives me infinite looping is not children empty list gets append and it repeats forever so we need to check before pushing levels 
            """
        if not root:
            return None
        q = deque([[root]])
        while q:
            cur_level = q.popleft()
            levels = []
            n = len(cur_level)
            for i in range(n):
                if cur_level[i].left: levels.append(cur_level[i].left)
                if cur_level[i].right: levels.append(cur_level[i].right)
                if i + 1 < n: cur_level[i].next = cur_level[i+1]
            # q.append(levels) if you do something liek this then it will be infite loop as the leaf node has no levels we push empty list pop it and again push empty list pop it and continue forever 
            if levels: q.append(levels)
        return root




#old attempt
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
            





        