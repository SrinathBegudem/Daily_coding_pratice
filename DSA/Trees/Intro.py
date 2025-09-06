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
    
if __name__ == "__main__":
    MyTree = BinaryTree()
    print(MyTree)



        




