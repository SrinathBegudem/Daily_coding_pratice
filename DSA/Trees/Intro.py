#binary tree implementation
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left 
        self.right = right

class BinaryTree:
    def __init__(self):
        self.val = int(input("please enter the root value: "))
        self.root = TreeNode(self.val)
        self.populate(self.root)

    def populate(self,node):
        left = input("do you want to insert in left node? y/n: ").lower()
        if left == "y":
            left_val = int(input("please enter the val: "))
            node.left = TreeNode(left_val)
            self.populate(node.left)

        right = input("do you want to insert in right node? y/n: ").lower()
        if right == "y":
            right_val = int(input('please enter the val: '))
            node.right = TreeNode(right_val)
            self.populate(node.right)
        return 
    def __str__(self):
        """Return a simple level-order traversal string."""
        if not self.root:
            return "[]"
        out = []
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                out.append("None")
        # trim trailing Nones for cleaner output
        while out and out[-1] == "None":
            out.pop()
        return "[" + ", ".join(out) + "]"


#---------------binary search tree---------------
# BST Invariant (rule) for every node 'x':
#   - all values in x.left subtree are strictly LESS than x.val
#   - all values in x.right subtree are GREATER than or EQUAL to x.val 
#   (this "duplicates go right" policy keeps the tree consistent)
# Notes:
# - Insertion/search follow the invariant by going left if val < node.val,
#   else going right.
# - A plain BST does NOT rebalance itself (worst-case height can be O(n)).
# - Height here is defined in EDGES: empty tree = -1, single node = 0.
class BST:

    def __init__(self):
        self.root: Optional[TreeNode] = None
        # lets ask user for choice
        choice = input("do you want to enter an array or interactive input? (array/interactive): ").lower().strip()
        
        if choice == "array":
            arr_str = input("enter the list of numbers with space: ").strip()
            if not arr_str:
                print("No values provided. Empty BST created.")
                return 
            
            try:
                arr = list(map(int, arr_str.split()))
            except ValueError:
                print("Invalid input. Empty BST created.")
                return

            # build: set root from first, insert the rest
            self.root = TreeNode(arr[0])
            for val in arr[1:]:
                self.iter_insert(val)   # choose iterative or recursive here
            
        else:
            root_str = input("please enter the root val: ")
            # checking if they dont enter root val so we can safely return
            try:
                root_val = int(root_str)
            except ValueError:
                print("Invalid root value. Empty BST created.")
                return  # always remeber in init we should only return None
            self.root = TreeNode(root_val)
            self._insert_loop()


    def _insert_loop(self):
        print("Enter values to insert (blank to stop).")
        while True:
            val = input("> ").strip()
            if not val:
                break
            try:
                val = int(val)
            except ValueError:
                print("please enter valid int number")
                continue
            self.recur_insert(val)


    def iter_insert(self,val):
        if self.root is None:
            self.root = TreeNode(val)
            return
        cur = self.root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return
                cur = cur.left
            
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return
                cur = cur.right
        
    def recur_insert(self,val,cur=None):
        if not self.root:
            self.root = TreeNode(val)
            return 
        if not cur:
            cur = self.root
        
        if val < cur.val:
            if not cur.left:
                cur.left = TreeNode(val)
                return 
            self.recur_insert(val,cur.left)
        else:
            if not cur.right:
                cur.right = TreeNode(val)
                return 
            self.recur_insert(val,cur.right)
        
    def height(self):
        def dfs(node):
            if not node:
                return -1
            return 1 + max(dfs(node.left),dfs(node.right))
        return dfs(self.root)
        
# traversal pending:




            

            
        




    