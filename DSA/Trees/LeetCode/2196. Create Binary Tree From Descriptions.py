# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        The key idea here is 
        i will use hash map and hash set to store the nodes created in hash map and children node in hash set
        - so when i traverse the input 2d array i will create the parent node add it to the hashmap like node[par] = treenode(par), so i can have access to this parent node to add its left and right children later 
        - similar when i create the child node i will add it to the hash map and after that i will add the par node left or right node by looking up the hash map 
        - finally the [i][1] index denotes the children so i will maintain an hash set to track this all and at the end i will run a for loop to find the root as the problem requires us to return the root
        """
        node = {} # to keep track of node val -> tree node 
        children = set() # to keep track of all children and find the root
        for par,child,is_left in descriptions:
            # add the children to children set for children tracking 
            children.add(child)
            #check if the parent node exist if not create 
            if par not in node:
                node[par] = TreeNode(par) # create the treenode and add to map
            #check if the child node exists if not create 
            if child not in node:
                node[child] = TreeNode(child)
            
            #now as we added the par and child to hash map now we will retrieve them and link left or right child 
            if is_left:
                node[par].left = node[child] # see how we are using hashmap and fetching the actual tree node and attaching it 
            else:
                node[par].right = node[child]
        # once the above loop done we are constructed a whole tree but the problem is to return the root thats why we kept the track of children 
        #now lets run the loop and find the root and return it 
        for p,c,l in descriptions:
            #we only care about the par, because thats where we find the root, in child and is left we wont find because root is never a child of any node.
            if p not in children:
                return node[p] # we dont return p bcz its just a val we return tree node that we created in hashmap 
        
        