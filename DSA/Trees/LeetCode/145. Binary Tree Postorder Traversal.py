# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        #------------------iter_sol(DFS)-------------------
        def iter_sol(node):
            """
            Intuition is just rememeber that we need 2 stacks, in stack one we just do the pre order code but just change is that we first push left and then right but in pre order we push right and then left, so the inutition for this is in stack 2 we get reversed of res because we are pushing right first so we reverse the stack 2.
            """
            # space = o(n)+o(n) (because we build res 2 while pop s2 so total both together takes o(N)), time = o(n)
            if not node : return []
            s1 = [node]
            s2 = []
            res = []
            while s1:
                node = s1.pop()
                s2.append(node.val)
                # how we push left node first that is why we get reverse order in s2
                if node.left: s1.append(node.left)
                if node.right: s1.append(node.right)
            #run a loop to build res by poping the s2 
            while s2:
                last_element = s2.pop()
                res.append(last_element)
        #     return res 
        # return iter_sol(root)

        def iter_sol_reverse(node):
            """
            instead of 2 stack just store the res and reverse it not that it makes much of differrence as space and time remains same
            """
            # space = o(n)+o(n) (because we build res 2 while pop s2 so total both together takes o(N)), time = o(n)
            if not node : return []
            s1 = [node]
            # s2 = [] # instead of 
            res = []
            while s1:
                node = s1.pop()
                res.append(node.val)
                # how we push left node first that is why we get reverse order in s2
                if node.left: s1.append(node.left)
                if node.right: s1.append(node.right)
            
            # case 1 : fails
            # return res.reverse() #inplace reverse() bug this return None as .reverse will reverse the list inplace and returns None
            # case2 : fails 
            # return reversed(res) bcz reversed() return list_iterator ( like transformer not yet reverse list its lazy operator we need action to get the result like list )
            #we can do something like
            #casae 3: works
            # return reversed(list(res))
            #case4: works 
            # res.reverse()
            # return res 
            #case5: works
        #     return res[::-1]
        # return iter_sol_reverse(root)

#------------------------recursion(dfs)-------------------
        res = []
        def recur_sol(node):
            if not node: return

            recur_sol(node.left)
            recur_sol(node.right)
            res.append(node.val)
        
        recur_sol(root)
        return res


    
