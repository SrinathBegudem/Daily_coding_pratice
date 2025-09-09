from collections import deque

#tree node
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        input_arr = []

        while True:
            s = input("please enter a num to build or blank space to stop: ")
            if s.strip() == "":
                break
            try:
                input_arr.append(int(s))
            except ValueError:
                print("please only enter valid integer num")
                continue
        print("your input arr: ",input_arr)
        
        if not input_arr:
            print("empty BST created.")
            return 
        
        self.root = TreeNode(input_arr[0])
        for val in input_arr[1:]:
            self._insert_iter(val)
    
    def insert(self,val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_iter(val)

    def _insert_iter(self,val,node):
        # if node is None:
        #     return TreeNode(val)
        cur = node
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    return
                cur = cur.right


    def _insert_recur(self, val, node):
        if not node: 
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_recur(val, node.left)
        else:
            node.right = self._insert_recur(val, node.right)
        return node


#lets start with bfs (level order traversal)
# iterative bfs
class TreeTraversal:
    def __init__(self, root=None):
        self.root = root

    
    #-----------bfs(level order)------------------------------
        
    def iter_level_order(self):
        if not self.root:
            return []
        res = []
        q = deque([self.root])
        
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

    # def recur_level_order(self): very non intuitive so for now we can skip mostly will never ask in interviews
    #     if not self.root:
    #         return []
        
    #-------------------dfs-------------------------
    #----------------preorder (R->L->R)-------------
    def iter_preorder(self):
        res = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
    
    def recur_preorder(self):
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            dfs(self.root)
        return res
    
    #-----------inorder-----------------
    def iter_inorder(self):
        
    
            
        

            
