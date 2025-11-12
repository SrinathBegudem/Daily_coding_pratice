# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        Hurray i solved this non imp medium question all by myself in less than 15 mins 
        - the key idea is to used recursion and bfs is not possible here ( because in bfs we go level by level which is not what wanted in this question)

        """
        freq_count = {} # used to count each number freq
        self.max_freq = 0  # is to store the max_freq used to return res with max_freq
        res = []
        def dfs(node):
            """
            I think we have to do post order traversal first traverse all the way till the end and start counting upwards 
            """
            if not node: return 0
            count = node.val + dfs(node.left) + dfs(node.right)
            if count in freq_count:
                freq_count[count] += 1
            else:
                freq_count[count] = 1
            self.max_freq = max(self.max_freq,freq_count[count])
            return count 
        
        dfs(root)
    
        for k,v in freq_count.items():
            if v == self.max_freq:
                res.append(k)
        return res
            

        