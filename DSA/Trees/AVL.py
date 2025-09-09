class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.h = 1 # node-height: None = 0, leaf = 1

def height(n):
    return n.h if n else 0

def update(n):
    # recompute node height from children.
    lh = height(n.left)
    rh = height(n.right)
    n.h = 1 + (lh if lh > rh else rh)

def balance(n):
    #balance factor: height(left) - height(right)
    return height(n.left) - height(n.right) if n else 0

#-----------------rotations----------------------
def right_rotate(y):
    """
        y                            x
       / \                          / \
      x   T3     rightRotate(y)    T1  y
     / \        -------------->        / \
    T1 T2                              T2 T3
    """

    x = y.left
    T2 = x.right
    #rotate 
    x.right = y 
    y.left = T2

    #update the child hieght first and then parent 
    update(y)
    update(x)

    return x #rotated parent

def left_rotate(x):
    """
      x                               y
     / \                             / \
    T1  y        leftRotate(x)      x  T3
       / \      -------------->     / \
      T2 T3                        T1 T2
    """

    y = x.right
    T2 = y.left
    #rotate 
    y.left = x
    x.right = T2

    # update heights
    update(x)
    update(y)
    return y

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None: # we can also do if not node but here we need to specific so node is None
            return AVLNode(key)
        
        #1) classic bst insert
        #check the key if less than or equal to or greater than the parent node if less than insert to left else insert to right
        if key < node.val:
            node.left = self._insert(node.left,key)
        else: #duplicates go to right
            node.right = self._insert(node.right,key)
        
        #2) update height 
        update(node)
        #3) reblance if needed
        b = balance(node)

        #------detect and fix the 4 cases------
        #LL case: left-heavy and key < node.left.val
        if b > 1 and key < node.left.val:
            return right_rotate(node)
        
        #LR case: left heavy and key >= node.right.val
        if b > 1 and key >= node.left.val:
            node.left = left_rotate(node.left)
            return right_rotate(node)
        
        #RR case: right heavy and key >= node.right.val
        if b < -1 and key >= node.right.val:
            return left_rotate(node)
        
        #RL case: right heavy and key < node.left.val
        if b < -1 and key < node.right.val:
            node.right = right_rotate(node.right)
            return left_rotate(node)
        
        #already balanced 
        return node
    


    



    