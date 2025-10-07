class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Definetly draw recurive tree to undertsand 
        """
        n = len(nums)
        # we have res to store the copy 
        res = []
        # to store the path
        path = []
        # to see if we visited it or not 
        used = [False]*n # we use flag because agter every dfs call for loop start from indx 0 to directly go to the index we needed we set flag and skip already visied
        def dfs():
            #base condition 
            if len(path) == n:
                #copy ( make sure to know the diff btw deep and shallow copy)
                res.append(path[:]) #or res.append(path.copy())
                return
            for i in range(n):
                if used[i]: # not gonna go there since its already appended to the path 
                    continue
                used[i] = True
                #core algo of back track
                # append 
                path.append(nums[i])
                #recurse
                dfs()
                #backtrack
                path.pop()
                # set the flag to false so it can be visitied again
                used[i] = False
        dfs()
        return res
            




        