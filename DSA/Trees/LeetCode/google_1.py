#level order sucessor of a node
# the question is you will be give a node val we need to return the next node in that particular level if not the next elements of that particular node 

# intuition: for this we will do bfs and then once we found the particular node we will add its children to the queue and then print the next element. 
# if confusion view this link Q3 : https://www.youtube.com/watch?v=9D-vP-jcc-Y&list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&index=55

from collections import deque

def level_order_bfs(root,target):
    if not root or not target: return None

    q = deque([root])
    while q:
        node = q.popleft()
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
        #now after adding the children lets check if the node is equal to the target
        if node is target: return q.popleft() if q else None # or we can also do q[0]
    return None




    