# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        The concept here is very clear
        questions: are the array elements are streaming?? or they are giving you a array with fix len and no adds on 
        - if the array len is increasing then you should probably use avl or (red balck tree).
        - if the array len stays constant and then you have to build a binary search tree (balance) then sorting and build from middle recursivly always work! the only problem is if you have strict duplicates go to one side policy then you should be little more careful to choose the right most eleemnt of duplicate so that it ends up in left most of every node.
        """
        # for this particular problem it is given that vals are strictly in increasing order.
        def dfs(lo, hi):
            if lo > hi:
                return None
            
            mid = lo + (hi-lo)//2
            node = TreeNode(nums[mid])
            node.left = dfs(lo,mid-1)
            node.right = dfs(mid+1,hi)
            return node
        return dfs(0,len(nums)-1)     

    #with occasinal duplicatest the below tree will garnutee to give u a balance tree if there are so many duplicates lets a an array full of duplciates then the tree becaomes linked list adn its unaviodable for binary search tree and its is also considered as flaw so we loose balance but stil lcan build binary search tree with unbalnce height so the below code gives balance hieght with close to 3 or 4 duplciates after that you might build a binary tree but doesnot guarantee a balanced bst
    def arrayToBST_dups_right(self,nums):
        if not nums:
            return None
        nums.sort()
        return self._build_dups_right(nums,0,len(nums)-1) 
    
    def _build_dups_right(self,a,lo,hi):
        if lo > hi: return None

        mid = lo + (hi - lo)//2
        i = mid 
        # traverse as left as possible for duplicates so that the duplicated always end up in node.right
        while i > lo and a[i-1] == a[i]:
            i -= 1
        node = TreeNode(a[i])
        node.left = self._build_dups_right(a,lo,i-1)
        node.right = self._build_dups_right(a,i+1,hi)
        return node


    
    def arrayToBST_dups_left(self,nums):
        if not nums:
            return None
        nums.sort()
        return self._build_dups_left(nums,0,len(nums)-1) 
    
    def _build_dups_left(self,a,lo,hi):
        if lo > hi: return None

        mid = lo + (hi - lo)//2
        i = mid 
        # traverse as right as possible for duplicates so that the duplicated always end up in node.left
        while i < hi and a[i+1] == a[i]:
            i += 1
        node = TreeNode(a[i])
        node.left = self._build_dups_left(a,lo,i-1)
        node.right =self._build_dups_left(a,i+1,hi)
        return node
    